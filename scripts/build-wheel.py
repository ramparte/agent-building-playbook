#!/usr/bin/env python3
"""build-wheel.py - render patterns/ into a 3-tier "flavor wheel" taxonomy.

A tasting wheel is simple at the center (a few broad families) and grows finer
as you move outward. This projects the 113 patterns onto that shape:

    Ring 0 (center) : 6 broad FAMILIES        <- the "first taste"
    Ring 1 (middle) : 13 DIMENSIONS           <- sub-families
    Ring 2 (outer)  : individual PATTERNS      <- the fine detail

SOURCE  : patterns/*.md   (canonical frontmatter: title, one_liner, dimensions)
CONFIG  : the FAMILIES map below (curated design; edit to re-cut the wheel)
OUTPUT  : wheel/taxonomy.yaml   (canonical structured taxonomy - agent form)
          wheel/wheel.md        (human/agent-readable outline)
          wheel/wheel.dot       (Graphviz radial graph - agent form)
          wheel/wheel.svg       (the visual flavor wheel)

Each pattern gets ONE home on the wheel: its primary dimension. Default primary
is the first-listed dimension in the pattern's frontmatter (authors list the
most central dimension first); override per-pattern in PRIMARY_OVERRIDES.

Portable: Python stdlib only. No external deps. Fails loud.
"""

from __future__ import annotations

import colorsys
import html
import math
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# CONFIG (curated design). Re-cutting the wheel = editing this block.
# --------------------------------------------------------------------------

# The center of the wheel: 6 broad families, each grouping 2-3 dimensions.
# `hue` is the base colour (HSL degrees) used to shade that family's arc.
FAMILIES: dict[str, dict] = {
    "Mindset":       {"hue": 275, "dimensions": ["meta-principles", "taste"]},
    "Context":       {"hue": 205, "dimensions": ["context-engineering", "knowledge"]},
    "Tooling":       {"hue": 145, "dimensions": ["tool-design", "cost-routing"]},
    "Orchestration": {"hue": 35,  "dimensions": ["orchestration", "workflow-discipline"]},
    "Trust":         {"hue": 352, "dimensions": ["verification", "reliability", "observability"]},
    "People":        {"hue": 305, "dimensions": ["human-factors", "intent"]},
}

# Optional per-pattern home override: {slug: dimension}. Empty by default;
# default primary is the first-listed dimension in the frontmatter.
PRIMARY_OVERRIDES: dict[str, str] = {}

# One-line gloss per family, shown in the outline / tooltips.
FAMILY_GLOSS: dict[str, str] = {
    "Mindset": "How to think and what to value before you build.",
    "Context": "What the model sees and remembers.",
    "Tooling": "The model's hands, and what they cost.",
    "Orchestration": "How work is shaped, decomposed, and run.",
    "Trust": "Making the result correct, reliable, and observable.",
    "People": "Human intent, attention, and leverage.",
}

# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PATTERNS_DIR = REPO_ROOT / "patterns"
WHEEL_DIR = REPO_ROOT / "wheel"

DIM_TO_FAMILY = {
    d: fam for fam, cfg in FAMILIES.items() for d in cfg["dimensions"]
}


def parse_patterns() -> list[dict]:
    files = sorted(PATTERNS_DIR.glob("*.md"))
    if not files:
        raise SystemExit(f"ERROR: no pattern files found in {PATTERNS_DIR}")
    out = []
    for path in files:
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---", raw, re.DOTALL)
        if not m:
            raise SystemExit(f"ERROR: {path} is missing a frontmatter block.")
        front = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                front[k.strip()] = v.strip()
        for req in ("title", "one_liner", "dimensions"):
            if not front.get(req):
                raise SystemExit(f"ERROR: {path} missing frontmatter field: {req}")
        dims = [d.strip() for d in front["dimensions"].split(",") if d.strip()]
        for d in dims:
            if d not in DIM_TO_FAMILY:
                raise SystemExit(
                    f"ERROR: {path} uses dimension '{d}' not mapped to any family. "
                    f"Add it to a family in FAMILIES."
                )
        slug = path.stem
        primary = PRIMARY_OVERRIDES.get(slug, dims[0])
        if primary not in dims:
            raise SystemExit(
                f"ERROR: override primary '{primary}' for {slug} is not one of its "
                f"dimensions {dims}."
            )
        out.append(
            {
                "slug": slug,
                "title": front["title"],
                "one_liner": front["one_liner"],
                "dimensions": dims,
                "primary": primary,
                "family": DIM_TO_FAMILY[primary],
            }
        )
    return out


def build_tree(patterns: list[dict]) -> dict:
    """family -> dimension -> [patterns], preserving config + title order."""
    tree: dict[str, dict[str, list[dict]]] = {}
    for fam, cfg in FAMILIES.items():
        tree[fam] = {d: [] for d in cfg["dimensions"]}
    for p in patterns:
        tree[p["family"]][p["primary"]].append(p)
    for fam in tree:
        for d in tree[fam]:
            tree[fam][d].sort(key=lambda x: x["title"].lower())
    return tree


# ---------- colour helpers ----------

def hsl_hex(h: float, s: float, ll: float) -> str:
    r, g, b = colorsys.hls_to_rgb(h / 360.0, ll / 100.0, s / 100.0)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


# ---------- YAML emitter (stdlib, no pyyaml) ----------

def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_yaml(tree: dict, patterns: list[dict]) -> str:
    lines = [
        "# Agent-Building Playbook - flavor-wheel taxonomy",
        "# GENERATED by scripts/build-wheel.py from patterns/. Do not hand-edit.",
        f"# {len(patterns)} patterns, {len(FAMILIES)} families, "
        f"{len(DIM_TO_FAMILY)} dimensions.",
        "wheel:",
    ]
    for fam, cfg in FAMILIES.items():
        fam_patterns = sum(len(tree[fam][d]) for d in cfg["dimensions"])
        lines.append(f"  - family: {yaml_str(fam)}")
        lines.append(f"    gloss: {yaml_str(FAMILY_GLOSS.get(fam, ''))}")
        lines.append(f"    pattern_count: {fam_patterns}")
        lines.append("    dimensions:")
        for d in cfg["dimensions"]:
            lines.append(f"      - dimension: {yaml_str(d)}")
            lines.append(f"        pattern_count: {len(tree[fam][d])}")
            lines.append("        patterns:")
            for p in tree[fam][d]:
                lines.append(f"          - slug: {yaml_str(p['slug'])}")
                lines.append(f"            title: {yaml_str(p['title'])}")
                lines.append(f"            one_liner: {yaml_str(p['one_liner'])}")
                also = [x for x in p["dimensions"] if x != p["primary"]]
                if also:
                    lines.append(
                        "            also: [" + ", ".join(yaml_str(a) for a in also) + "]"
                    )
    return "\n".join(lines) + "\n"


# ---------- Markdown outline ----------

def emit_md(tree: dict, patterns: list[dict]) -> str:
    out = [
        "# The Agent-Building Playbook Wheel",
        "",
        "> Simple at the center, finer toward the edge. "
        f"{len(FAMILIES)} families &rarr; {len(DIM_TO_FAMILY)} dimensions &rarr; "
        f"{len(patterns)} patterns.",
        "",
        "GENERATED by `scripts/build-wheel.py`. Do not hand-edit; regenerate.",
        "",
    ]
    for fam, cfg in FAMILIES.items():
        fam_patterns = sum(len(tree[fam][d]) for d in cfg["dimensions"])
        out.append(f"## {fam} ({fam_patterns})")
        out.append("")
        out.append(f"*{FAMILY_GLOSS.get(fam, '')}*")
        out.append("")
        for d in cfg["dimensions"]:
            out.append(f"### {d} ({len(tree[fam][d])})")
            for p in tree[fam][d]:
                also = [x for x in p["dimensions"] if x != p["primary"]]
                tail = f"  _(also: {', '.join(also)})_" if also else ""
                out.append(f"- **{p['title']}** — {p['one_liner']}{tail}")
            out.append("")
    return "\n".join(out)


# ---------- Graphviz ----------

def emit_dot(tree: dict) -> str:
    out = [
        "// Agent-Building Playbook wheel - GENERATED by scripts/build-wheel.py",
        "digraph wheel {",
        "  layout=twopi; ranksep=2.2; overlap=false; splines=true;",
        '  node [shape=oval, style=filled, fontname="Helvetica"];',
        '  root [label="Agent-Building\\nPlaybook", fillcolor="#1b1b1f", '
        'fontcolor=white, shape=circle];',
    ]

    def nid(s: str) -> str:
        return '"' + s.replace('"', '') + '"'

    for fam, cfg in FAMILIES.items():
        col = hsl_hex(cfg["hue"], 55, 45)
        out.append(f'  {nid(fam)} [fillcolor="{col}", fontcolor=white];')
        out.append(f"  root -> {nid(fam)};")
        for d in cfg["dimensions"]:
            dcol = hsl_hex(cfg["hue"], 50, 62)
            out.append(f'  {nid(d)} [fillcolor="{dcol}"];')
            out.append(f"  {nid(fam)} -> {nid(d)};")
            for p in tree[fam][d]:
                pcol = hsl_hex(cfg["hue"], 58, 84)
                lbl = p["title"].replace('"', "'")
                out.append(
                    f'  {nid(p["slug"])} [label="{lbl}", fillcolor="{pcol}", '
                    f"fontsize=9];"
                )
                out.append(f"  {nid(d)} -> {nid(p['slug'])};")
    out.append("}")
    return "\n".join(out)


# ---------- SVG flavor wheel ----------

SIZE = 1180
CX = CY = SIZE / 2
R_HUB = 96
R_FAM = 188          # family ring outer
R_DIM = 286          # dimension ring outer
R_PAT = 560          # pattern ring outer


def pol(r: float, ang: float) -> tuple[float, float]:
    """Angle in degrees, 0 at top (12 o'clock), increasing clockwise."""
    th = math.radians(ang - 90)
    return (CX + r * math.cos(th), CY + r * math.sin(th))


def fmt(p: tuple[float, float]) -> str:
    return f"{p[0]:.2f},{p[1]:.2f}"


def sector(r_in: float, r_out: float, a0: float, a1: float) -> str:
    large = 1 if (a1 - a0) > 180 else 0
    p1, p2 = pol(r_out, a0), pol(r_out, a1)
    p3, p4 = pol(r_in, a1), pol(r_in, a0)
    return (
        f"M{fmt(p1)} A{r_out:.2f},{r_out:.2f} 0 {large} 1 {fmt(p2)} "
        f"L{fmt(p3)} A{r_in:.2f},{r_in:.2f} 0 {large} 0 {fmt(p4)} Z"
    )


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def tangential_label(text: str, r: float, a0: float, a1: float,
                     color: str, size: float, weight: str = "600") -> str:
    mid = (a0 + a1) / 2
    x, y = pol(r, mid)
    rot = mid
    if 90 < mid < 270:
        rot += 180
    return (
        f'<text x="{x:.2f}" y="{y:.2f}" transform="rotate({rot:.2f} {x:.2f} {y:.2f})" '
        f'text-anchor="middle" dominant-baseline="central" fill="{color}" '
        f'font-size="{size}" font-weight="{weight}">{esc(text)}</text>'
    )


def radial_label(text: str, r_in: float, r_out: float, mid: float,
                 color: str, size: float) -> str:
    if len(text) > 40:
        text = text[:39] + "\u2026"
    pad = 6
    if mid <= 180:  # right half - read outward, no flip
        x, y = pol(r_in + pad, mid)
        rot = mid - 90
        anchor = "start"
    else:           # left half - start at outer, flip 180 so upright
        x, y = pol(r_out - pad, mid)
        rot = mid + 90
        anchor = "start"
    return (
        f'<text x="{x:.2f}" y="{y:.2f}" transform="rotate({rot:.2f} {x:.2f} {y:.2f})" '
        f'text-anchor="{anchor}" dominant-baseline="central" fill="{color}" '
        f'font-size="{size}">{esc(text)}</text>'
    )


def emit_svg(tree: dict, patterns: list[dict]) -> str:
    n = len(patterns)
    per = 360.0 / n  # degrees per pattern - proportional arcs
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">',
        f'<rect width="{SIZE}" height="{SIZE}" fill="#fbfbfd"/>',
    ]

    ang = 0.0
    for fam, cfg in FAMILIES.items():
        hue = cfg["hue"]
        fam_start = ang
        fam_n = sum(len(tree[fam][d]) for d in cfg["dimensions"])
        if fam_n == 0:
            continue
        # dimensions within this family
        for d in cfg["dimensions"]:
            plist = tree[fam][d]
            if not plist:
                continue
            dim_start = ang
            # pattern segments (outer ring)
            for i, p in enumerate(plist):
                a0, a1 = ang, ang + per
                shade = 84 if (i % 2 == 0) else 89
                fill = hsl_hex(hue, 60, shade)
                mid = (a0 + a1) / 2
                tip = esc(f"{p['title']}  \u2014  {p['one_liner']}")
                parts.append(
                    f'<path d="{sector(R_DIM, R_PAT, a0, a1)}" fill="{fill}" '
                    f'stroke="#fbfbfd" stroke-width="0.6"><title>{tip}</title></path>'
                )
                parts.append(
                    radial_label(p["title"], R_DIM, R_PAT, mid, "#26262b", 9.2)
                )
                ang = a1
            dim_end = ang
            # dimension ring segment
            dcol = hsl_hex(hue, 52, 60)
            parts.append(
                f'<path d="{sector(R_FAM, R_DIM, dim_start, dim_end)}" fill="{dcol}" '
                f'stroke="#fbfbfd" stroke-width="1.2"/>'
            )
            parts.append(
                tangential_label(d, (R_FAM + R_DIM) / 2, dim_start, dim_end,
                                 "#ffffff", 12.5, "600")
            )
        fam_end = ang
        # family ring segment
        fcol = hsl_hex(hue, 55, 44)
        parts.append(
            f'<path d="{sector(R_HUB, R_FAM, fam_start, fam_end)}" fill="{fcol}" '
            f'stroke="#fbfbfd" stroke-width="1.6"><title>{esc(FAMILY_GLOSS.get(fam, ""))}</title></path>'
        )
        parts.append(
            tangential_label(fam, (R_HUB + R_FAM) / 2, fam_start, fam_end,
                             "#ffffff", 17, "700")
        )

    # hub
    parts.append(f'<circle cx="{CX}" cy="{CY}" r="{R_HUB}" fill="#1b1b1f"/>')
    parts.append(
        f'<text x="{CX}" y="{CY - 10}" text-anchor="middle" fill="#ffffff" '
        f'font-size="20" font-weight="700">Agent-Building</text>'
    )
    parts.append(
        f'<text x="{CX}" y="{CY + 15}" text-anchor="middle" fill="#ffffff" '
        f'font-size="20" font-weight="700">Playbook</text>'
    )
    parts.append(
        f'<text x="{CX}" y="{CY + 40}" text-anchor="middle" fill="#9a9aa8" '
        f'font-size="11">{n} patterns</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts)


# ---------- Interactive zoomable-sunburst explorer (single HTML file) ----------

# Where full pattern pages live, so the detail panel can link to them. Relative
# so it works wherever the site is served (explore.html sits beside patterns/).
SITE_BASE = ""

# Self-contained: vanilla JS, no CDN, data embedded. Placeholders (__DATA__ etc.)
# are substituted by emit_html(). Braces are literal JS (no .format / f-string).
EXPLORER_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent-Building Playbook — Explore the Wheel</title>
<style>
  :root { --fg:#1b1b1f; --muted:#63636e; --line:#e6e6ec; --bg:#fbfbfd; --accent:#3858a6; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--fg);
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
  .app { display:flex; flex-wrap:wrap; gap:10px; max-width:1260px; margin:0 auto; padding:16px; }
  .stage { flex:1 1 560px; min-width:320px; position:relative; }
  .side { flex:0 1 380px; min-width:300px; }
  h1 { font-size:1.35rem; margin:.2rem 0 .1rem; }
  .sub { color:var(--muted); font-size:.9rem; margin:0 0 .6rem; }
  .controls { display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin:0 0 .5rem; }
  .seg { display:inline-flex; border:1px solid var(--line); border-radius:9px; overflow:hidden; }
  .seg button { border:0; background:#fff; padding:.4rem .8rem; font:inherit; cursor:pointer; color:var(--muted); }
  .seg button.on { background:var(--accent); color:#fff; }
  .toggle { display:inline-flex; align-items:center; gap:.35rem; font-size:.85rem; color:var(--muted);
    border:1px solid var(--line); border-radius:9px; padding:.35rem .6rem; background:#fff; cursor:pointer; }
  #wheel { width:100%; height:auto; display:block; -webkit-tap-highlight-color:transparent; }
  #wheel path { cursor:pointer; }
  #wheel path:hover { stroke:#1b1b1f; stroke-width:1.8; }
  #wheel text { pointer-events:none; user-select:none; }
  #map { position:absolute; top:44px; right:4px; width:150px; height:150px;
    background:rgba(255,255,255,.72); border:1px solid var(--line); border-radius:10px; }
  #map path { cursor:pointer; }
  #outline { display:none; background:#fff; border:1px solid var(--line); border-radius:12px;
    padding:.6rem .9rem; max-height:76vh; overflow:auto; }
  #outline details { margin:.15rem 0; }
  #outline summary { cursor:pointer; padding:.2rem .1rem; font-weight:600; }
  #outline summary::marker { color:var(--muted); }
  #outline .dim > summary { font-weight:500; color:#3a3a44; }
  #outline .badge { color:var(--muted); font-weight:400; font-size:.8rem; }
  #outline .leaf { padding:.2rem .3rem .2rem 1.3rem; cursor:pointer; border-radius:7px; }
  #outline .leaf:hover { background:#f0f2fa; }
  #outline .leaf .ol { color:var(--muted); font-size:.8rem; }
  #outline .swatch { display:inline-block; width:9px; height:9px; border-radius:2px; margin-right:.4rem;
    vertical-align:middle; }
  .crumb { font-size:.9rem; margin:0 0 .5rem; min-height:1.4em; }
  .crumb a { color:var(--accent); text-decoration:none; cursor:pointer; }
  .crumb a:hover { text-decoration:underline; }
  .crumb .sep { color:var(--muted); margin:0 .35rem; }
  .search { width:100%; padding:.55rem .7rem; font-size:.95rem; border:1px solid var(--line);
    border-radius:9px; background:#fff; }
  .panel { background:#fff; border:1px solid var(--line); border-radius:12px; padding:1rem 1.15rem;
    margin-top:.7rem; }
  .panel h2 { font-size:1.05rem; margin:0 0 .3rem; }
  .panel .ol { color:var(--muted); }
  .chips { margin:.6rem 0 0; }
  .chip { display:inline-block; font-size:.72rem; padding:.12rem .55rem; margin:0 .3rem .35rem 0;
    background:#eef1fa; color:var(--accent); border-radius:999px; cursor:pointer; }
  .chip.home { background:var(--accent); color:#fff; cursor:default; }
  .chip.plain { background:#f0f0f4; color:var(--muted); cursor:default; }
  .lbl { font-size:.72rem; text-transform:uppercase; letter-spacing:.04em; color:var(--muted);
    margin:.85rem 0 .2rem; }
  .readmore { display:inline-block; margin-top:.7rem; color:var(--accent); font-weight:600; text-decoration:none; }
  .readmore:hover { text-decoration:underline; }
  .results { list-style:none; margin:.3rem 0 0; padding:0; max-height:52vh; overflow:auto; }
  .results li { padding:.4rem .5rem; border-radius:8px; cursor:pointer; }
  .results li:hover { background:#f0f2fa; }
  .results .rt { font-weight:600; }
  .results .rd { color:var(--muted); font-size:.8rem; }
  .hint { color:var(--muted); font-size:.82rem; margin-top:.6rem; }
  kbd { font:inherit; font-size:.75rem; background:#f0f0f4; border:1px solid var(--line);
    border-bottom-width:2px; border-radius:5px; padding:0 .3rem; }
  .count-pill { color:var(--muted); font-size:.8rem; }
</style>
</head>
<body>
<div class="app">
  <div class="stage">
    <h1>The Agent-Building Playbook Wheel</h1>
    <p class="sub">__COUNT__ patterns · __FAMILIES__ families · __DIMS__ dimensions —
      click to zoom in, click the center to zoom out. ·
      <a href="index.html" style="color:var(--accent)">List view ↗</a></p>
    <div class="controls">
      <span class="seg" id="viewseg">
        <button data-view="wheel" class="on">◉ Wheel</button>
        <button data-view="outline">☰ Outline</button>
      </span>
      <label class="toggle"><input type="checkbox" id="heat"> Density heat</label>
    </div>
    <svg id="wheel" viewBox="0 0 900 900" role="img" aria-label="Zoomable pattern wheel"></svg>
    <svg id="map" viewBox="0 0 164 164" aria-label="Overview minimap"></svg>
    <div id="outline"></div>
  </div>
  <div class="side">
    <div class="crumb" id="crumb"></div>
    <input class="search" id="q" type="search" placeholder="Search patterns…  (press / )" autocomplete="off">
    <div id="detail"></div>
  </div>
</div>
<script>
const DATA = __DATA__;
const SITE_BASE = "__SITE_BASE__";
const SVGNS = "http://www.w3.org/2000/svg";
const CX = 450, CY = 450, R_HUB = 90, R1 = 214, R2 = 356;
const svg = document.getElementById("wheel");
const mapSvg = document.getElementById("map");
const outlineEl = document.getElementById("outline");
const crumbEl = document.getElementById("crumb");
const detailEl = document.getElementById("detail");
const qEl = document.getElementById("q");

// ---- layout: leaf-count weighting, [x0,x1] in [0,1], depth ----
function layout(root){
  (function count(n){
    if(n.children && n.children.length){ n.value = n.children.reduce((s,c)=>s+count(c),0); }
    else { n.value = 1; }
    return n.value;
  })(root);
  root.x0=0; root.x1=1; root.depth=0; root.parent=null;
  (function part(n){
    if(!n.children) return;
    let x=n.x0; const w=n.x1-n.x0;
    for(const c of n.children){
      const cw = w * (c.value/n.value);
      c.x0=x; c.x1=x+cw; c.depth=n.depth+1; c.parent=n; x+=cw; part(c);
    }
  })(root);
}
layout(DATA);

const nodes=[];
(function walk(n){ nodes.push(n); (n.children||[]).forEach(walk); })(DATA);
nodes.forEach((n,i)=>{ n.id=i; });
const leaves = nodes.filter(n=>n.kind==="pattern");
const families = DATA.children;

// ---- lookups + relatedness index ----
const famByName={}, dimByKey={}, patBySlug={};
for(const f of families){
  famByName[f.name]=f;
  for(const d of f.children){
    dimByKey[f.name+"/"+d.name]=d;
    for(const p of d.children){ patBySlug[p.slug]=p; p.dims=[p.dimension].concat(p.also||[]); }
  }
}
const dimIndex={};  // dimName -> [patterns that carry it as home or also]
for(const p of leaves){ for(const dn of p.dims){ (dimIndex[dn]=dimIndex[dn]||[]).push(p); } }
function relatedTo(p){
  const score=new Map();
  for(const dn of p.dims){ for(const q of (dimIndex[dn]||[])){ if(q!==p) score.set(q,(score.get(q)||0)+1); } }
  return [...score.entries()].sort((a,b)=> b[1]-a[1] || a[0].name.localeCompare(b[0].name))
    .slice(0,6).map(e=>e[0]);
}

// heat ranges (per ring)
const famVals=families.map(f=>f.value);
const dimVals=[]; for(const f of families) for(const d of f.children) dimVals.push(d.value);
const famMin=Math.min(...famVals), famMax=Math.max(...famVals);
const dimMin=Math.min(...dimVals), dimMax=Math.max(...dimVals);

// ---- geometry helpers ----
function pol(r,a){ const t=(a-90)*Math.PI/180; return [CX+r*Math.cos(t), CY+r*Math.sin(t)]; }
function arcPath(a0,a1,rIn,rOut,cx,cy){
  cx=cx===undefined?CX:cx; cy=cy===undefined?CY:cy;
  if(a1-a0 < 0.0001) return "";
  const large=(a1-a0)>180?1:0;
  const P=(r,a)=>{ const t=(a-90)*Math.PI/180; return [cx+r*Math.cos(t), cy+r*Math.sin(t)]; };
  const p1=P(rOut,a0), p2=P(rOut,a1), p3=P(rIn,a1), p4=P(rIn,a0);
  return "M"+p1+" A"+rOut+","+rOut+" 0 "+large+" 1 "+p2+" L"+p3+" A"+rIn+","+rIn+" 0 "+large+" 0 "+p4+" Z";
}
function clip(s,m){ return s.length>m ? s.slice(0,m-1)+"\u2026" : s; }
function esc(s){ return (s||"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function lerp(a,b,t){ return a+(b-a)*t; }
function heatColor(v,min,max){
  const t=Math.max(0,Math.min(1,(v-min)/((max-min)||1)));
  const stops=[[255,247,214],[254,196,79],[227,120,40],[189,0,38]];
  const s=t*(stops.length-1); const i=Math.min(stops.length-2,Math.floor(s)); const f=s-i;
  const c=[0,1,2].map(k=>Math.round(lerp(stops[i][k],stops[i+1][k],f)));
  return "rgb("+c[0]+","+c[1]+","+c[2]+")";
}
function nodeFill(n){
  if(heatOn && (n.kind==="family"||n.kind==="dimension")){
    return n.kind==="family" ? heatColor(n.value,famMin,famMax) : heatColor(n.value,dimMin,dimMax);
  }
  return n.color;
}

// ---- build main-wheel DOM: one path + one label per node ----
const gArcs=document.createElementNS(SVGNS,"g"), gLabels=document.createElementNS(SVGNS,"g");
svg.appendChild(gArcs); svg.appendChild(gLabels);
nodes.forEach(n=>{
  if(n.kind==="root") return;
  const path=document.createElementNS(SVGNS,"path");
  path.setAttribute("stroke","#fbfbfd");
  path.setAttribute("stroke-width", n.kind==="pattern" ? "0.7" : "1.3");
  path.setAttribute("opacity","0");
  const tip=document.createElementNS(SVGNS,"title");
  tip.textContent = n.kind==="pattern" ? (n.name+" — "+n.one_liner) : (n.name+(n.gloss?" — "+n.gloss:""));
  path.appendChild(tip);
  path.addEventListener("click",e=>{ e.stopPropagation(); onClick(n); });
  gArcs.appendChild(path); n.el=path;
  const lbl=document.createElementNS(SVGNS,"text");
  lbl.setAttribute("opacity","0"); lbl.setAttribute("dominant-baseline","central");
  lbl.setAttribute("fill", n.kind==="pattern" ? "#26262b" : "#ffffff");
  lbl.setAttribute("font-size", n.kind==="family" ? "17" : n.kind==="dimension" ? "12.5" : "9.2");
  lbl.setAttribute("font-weight", n.kind==="family" ? "700" : n.kind==="dimension" ? "600" : "400");
  lbl.textContent = n.kind==="pattern" ? clip(n.name,40) : n.name;
  gLabels.appendChild(lbl); n.lbl=lbl;
});

// center hub
const hub=document.createElementNS(SVGNS,"circle");
hub.setAttribute("cx",CX); hub.setAttribute("cy",CY); hub.setAttribute("r",R_HUB);
hub.setAttribute("fill","#1b1b1f"); hub.style.cursor="pointer";
hub.addEventListener("click",()=>{ if(focus.parent) setFocus(focus.parent); });
svg.appendChild(hub);
function mkHubText(y,size,weight,fill){
  const t=document.createElementNS(SVGNS,"text");
  t.setAttribute("x",CX); t.setAttribute("y",y); t.setAttribute("text-anchor","middle");
  t.setAttribute("font-size",size); t.setAttribute("font-weight",weight); t.setAttribute("fill",fill);
  t.style.pointerEvents="none"; svg.appendChild(t); return t;
}
const hubL1=mkHubText(CY-8,"17","700","#ffffff");
const hubL2=mkHubText(CY+14,"11","400","#9a9aa8");
const hubL3=mkHubText(CY+34,"10","400","#6f6f7d");

// ---- minimap (families + dimensions, absolute geometry) ----
const MC=82, MR_HUB=16, MR1=40, MR2=66;
function buildMap(){
  for(const f of families){
    for(const d of f.children){
      const p=document.createElementNS(SVGNS,"path");
      p.setAttribute("d",arcPath(d.x0*360,d.x1*360,MR1,MR2,MC,MC));
      p.setAttribute("fill",d.color); p.setAttribute("stroke","#fff"); p.setAttribute("stroke-width","0.5");
      p.addEventListener("click",e=>{ e.stopPropagation(); onClick(d); });
      mapSvg.appendChild(p); d.mapEl=p;
    }
    const pf=document.createElementNS(SVGNS,"path");
    pf.setAttribute("d",arcPath(f.x0*360,f.x1*360,MR_HUB,MR1,MC,MC));
    pf.setAttribute("fill",f.color); pf.setAttribute("stroke","#fff"); pf.setAttribute("stroke-width","0.7");
    pf.addEventListener("click",e=>{ e.stopPropagation(); onClick(f); });
    mapSvg.appendChild(pf); f.mapEl=pf;
  }
  const you=document.createElementNS(SVGNS,"text");
  you.setAttribute("x",MC); you.setAttribute("y",MC+3); you.setAttribute("text-anchor","middle");
  you.setAttribute("font-size","7"); you.setAttribute("fill","#6f6f7d"); you.textContent="you are here";
  mapSvg.appendChild(you);
}
function isAncestor(a,d){ while(d){ if(d===a) return true; d=d.parent; } return false; }
function inBranch(n){ return n===focus || isAncestor(n,focus) || isAncestor(focus,n); }
function updateMinimap(){
  for(const f of families){
    if(f.mapEl){ f.mapEl.setAttribute("opacity", (focus===DATA||inBranch(f))?1:0.28);
      f.mapEl.setAttribute("fill", heatOn?heatColor(f.value,famMin,famMax):f.color); }
    for(const d of f.children){ if(d.mapEl){ d.mapEl.setAttribute("opacity",(focus===DATA||inBranch(d))?1:0.28);
      d.mapEl.setAttribute("fill", heatOn?heatColor(d.value,dimMin,dimMax):d.color); } }
  }
}

// ---- focus / target geometry (progressive: 2 rings from focus) ----
let focus=DATA, query="", heatOn=false, view="wheel", selected=null;
let highlight=new Set(), _silent=false;

function computeTargets(f){
  const span=f.x1-f.x0;
  for(const n of nodes){
    if(n.kind==="root"){ n.tgt={a0:0,a1:0,rIn:0,rOut:0,op:0}; continue; }
    const rel=n.depth-f.depth;
    let x0=(n.x0-f.x0)/span, x1=(n.x1-f.x0)/span;
    x0=Math.max(0,Math.min(1,x0)); x1=Math.max(0,Math.min(1,x1));
    let rIn=0,rOut=0,vis=false;
    if(rel===1){ rIn=R_HUB; rOut=R1; vis=true; }
    else if(rel===2){ rIn=R1; rOut=R2; vis=true; }
    if(x1-x0<1e-4) vis=false;
    n.tgt={ a0:x0*360, a1:x1*360, rIn, rOut, op: vis?1:0 };
  }
}
function draw(){
  for(const n of nodes){
    if(n.kind==="root"||!n.cur) continue;
    const c=n.cur;
    if(c.op<=0.004 && (!n.tgt||n.tgt.op<=0.004)){ n.el.setAttribute("opacity","0"); n.lbl.setAttribute("opacity","0"); continue; }
    n.el.setAttribute("d", arcPath(c.a0,c.a1,c.rIn,c.rOut));
    n.el.setAttribute("fill", nodeFill(n));
    let op=c.op; if(query){ op *= n.matchAny?1:0.12; }
    n.el.setAttribute("opacity", op.toFixed(3));
    if(highlight.has(n.id)){ n.el.setAttribute("stroke","#1b1b1f"); n.el.setAttribute("stroke-width","2.6"); }
    else { n.el.setAttribute("stroke","#fbfbfd"); n.el.setAttribute("stroke-width", n.kind==="pattern"?"0.7":"1.3"); }
    positionLabel(n,c,op);
  }
}
function positionLabel(n,c,op){
  const wdeg=c.a1-c.a0, mid=(c.a0+c.a1)/2, isLeaf=(n.kind==="pattern");
  const minW=isLeaf?2.6:5;
  if(op<0.45||wdeg<minW){ n.lbl.setAttribute("opacity","0"); return; }
  let x,y,rot,anchor;
  if(isLeaf){
    if(mid<=180){ [x,y]=pol(c.rIn+6,mid); rot=mid-90; anchor="start"; }
    else { [x,y]=pol(c.rOut-6,mid); rot=mid+90; anchor="start"; }
  } else { [x,y]=pol((c.rIn+c.rOut)/2,mid); rot=mid; if(mid>90&&mid<270) rot+=180; anchor="middle"; }
  n.lbl.setAttribute("x",x.toFixed(2)); n.lbl.setAttribute("y",y.toFixed(2));
  n.lbl.setAttribute("transform","rotate("+rot.toFixed(2)+" "+x.toFixed(2)+" "+y.toFixed(2)+")");
  n.lbl.setAttribute("text-anchor",anchor);
  n.lbl.setAttribute("opacity", Math.min(1,(op-0.45)/0.4).toFixed(3));
}
function setFocus(f,opts){
  opts=opts||{};
  focus=f; computeTargets(f);
  for(const n of nodes){
    if(n.kind==="root") continue;
    if(!n.cur) n.cur={a0:n.tgt.a0,a1:n.tgt.a1,rIn:n.tgt.rIn,rOut:n.tgt.rOut,op:0};
    if(n.cur.op<=0.004){ n.cur.a0=n.tgt.a0; n.cur.a1=n.tgt.a1; n.cur.rIn=n.tgt.rIn; n.cur.rOut=n.tgt.rOut; }
  }
  const from=nodes.map(n=> n.cur?{...n.cur}:null), start=performance.now(), dur=620;
  function frame(t){
    let k=Math.min(1,(t-start)/dur), e=k<0.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2;
    nodes.forEach((n,i)=>{ if(n.kind==="root"||!from[i]) return; const a=from[i],b=n.tgt;
      n.cur={a0:a.a0+(b.a0-a.a0)*e,a1:a.a1+(b.a1-a.a1)*e,rIn:a.rIn+(b.rIn-a.rIn)*e,rOut:a.rOut+(b.rOut-a.rOut)*e,op:a.op+(b.op-a.op)*e}; });
    draw(); if(k<1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  updateHub(); updateCrumb(); updateMinimap();
  if(!opts.keepDetail){ selected=null; highlight.clear(); }
  if(!opts.silent) syncHash();
}
function updateHub(){
  if(focus===DATA){ hubL1.textContent="Playbook"; hubL2.textContent="__COUNT__ patterns"; hubL3.textContent="click a wedge"; }
  else { hubL1.textContent=clip(focus.name,16); hubL2.textContent=focus.value+" pattern"+(focus.value===1?"":"s"); hubL3.textContent="\u2190 back"; }
}
function chain(n){ const c=[]; while(n){ c.unshift(n); n=n.parent; } return c; }
function updateCrumb(){
  crumbEl.innerHTML="";
  chain(focus).forEach((n,i,arr)=>{
    if(i){ const s=document.createElement("span"); s.className="sep"; s.textContent="›"; crumbEl.appendChild(s); }
    if(i<arr.length-1){ const a=document.createElement("a"); a.textContent=(n===DATA?"Home":n.name); a.onclick=()=>setFocus(n); crumbEl.appendChild(a); }
    else { const b=document.createElement("strong"); b.textContent=(n===DATA?"Home":n.name); crumbEl.appendChild(b); }
  });
}

function onClick(n){
  if(n.kind==="pattern"){ if(n.parent!==focus && n.parent.parent!==focus) setFocus(n.parent,{silent:true}); openDetail(n); }
  else { setFocus(n); showFamilyOrDim(n); }
}

function openDetail(p){
  selected=p;
  // cross-links: highlight this pattern's home + its other-home dimensions (and their families)
  highlight=new Set();
  for(const dn of p.dims){
    for(const f of families) for(const d of f.children) if(d.name===dn){ highlight.add(d.id); highlight.add(f.id); }
  }
  draw();
  const also=(p.also||[]).map(x=>'<span class="chip" data-go="'+esc(x)+'">'+esc(x)+' \u2197</span>').join("");
  const rel=relatedTo(p).map(q=>'<li data-k="'+q.id+'"><span class="rt">'+esc(q.name)+'</span><br>'+
    '<span class="rd">'+esc(q.family)+' › '+esc(q.dimension)+'</span></li>').join("");
  detailEl.innerHTML=
    '<div class="panel"><h2>'+esc(p.name)+'</h2>'+
    '<p class="ol">'+esc(p.one_liner)+'</p>'+
    '<div class="lbl">Homes</div><div class="chips"><span class="chip home">'+esc(p.dimension)+'</span>'+also+'</div>'+
    (rel?'<div class="lbl">Related patterns</div><ul class="results">'+rel+'</ul>':'')+
    '<a class="readmore" target="_blank" rel="noopener" href="'+SITE_BASE+'patterns/'+encodeURIComponent(p.slug)+'.html">Read the full pattern \u2197</a>'+
    '<p class="hint">Family: '+esc(p.family)+'</p></div>';
  detailEl.querySelectorAll("li[data-k]").forEach(li=>{ li.onclick=()=>{ const t=nodes[+li.dataset.k]; onClick(t); }; });
  detailEl.querySelectorAll("[data-go]").forEach(ch=>{ ch.onclick=()=>{ const d=findDim(ch.dataset.go); if(d){ setFocus(d,{silent:true,keepDetail:true}); openDetail(p); } }; });
  syncHash();
}
function findDim(name){ for(const f of families) for(const d of f.children) if(d.name===name) return d; return null; }

function showFamilyOrDim(n){
  if(!n || n.kind==="root"){ showHome(); return; }
  const kids=n.children||[];
  const label=n.kind==="family"?"dimensions":"patterns";
  const list=n.kind==="family"
    ? kids.map(d=>'<li data-k="'+d.id+'"><span class="rt">'+esc(d.name)+'</span> <span class="rd">'+d.value+'</span></li>').join("")
    : kids.map(p=>'<li data-k="'+p.id+'"><span class="rt">'+esc(p.name)+'</span><br><span class="rd">'+esc(clip(p.one_liner,90))+'</span></li>').join("");
  detailEl.innerHTML='<div class="panel"><h2>'+esc(n.name)+'</h2>'+(n.gloss?'<p class="ol">'+esc(n.gloss)+'</p>':'')+
    '<p class="count-pill">'+kids.length+' '+label+'</p><ul class="results">'+list+'</ul></div>';
  detailEl.querySelectorAll("li[data-k]").forEach(li=>{ li.onclick=()=>{ const t=nodes[+li.dataset.k]; onClick(t); }; });
}

// ---- search ----
function applyQuery(){
  query=qEl.value.trim().toLowerCase();
  for(const n of nodes) n.matchAny=false;
  if(query){
    for(const p of leaves){
      const hay=(p.name+" "+p.one_liner+" "+p.dims.join(" ")).toLowerCase();
      p.match=hay.indexOf(query)>=0;
      if(p.match){ let a=p; while(a){ a.matchAny=true; a=a.parent; } }
    }
    const hits=leaves.filter(p=>p.match).slice(0,60);
    detailEl.innerHTML='<div class="panel"><h2>'+hits.length+' match'+(hits.length===1?"":"es")+'</h2><ul class="results">'+
      hits.map(p=>'<li data-k="'+p.id+'"><span class="rt">'+esc(p.name)+'</span><br><span class="rd">'+esc(p.family)+' › '+esc(p.dimension)+'</span></li>').join("")+'</ul></div>';
    detailEl.querySelectorAll("li[data-k]").forEach(li=>{ li.onclick=()=>{ const t=nodes[+li.dataset.k]; setFocus(t.parent,{silent:true}); openDetail(t); }; });
  } else { showHome(); }
  draw(); filterOutline(); syncHash();
}
qEl.addEventListener("input", applyQuery);

function showHome(){
  detailEl.innerHTML='<div class="panel"><h2>Explore</h2>'+
    '<p class="ol">Start at the center. Click a family to open its dimensions, then a dimension to see its patterns. '+
    'Click the dark center (or press <kbd>Esc</kbd>) to zoom out. Search to jump to any pattern.</p>'+
    '<div class="chips">'+families.map(f=>'<span class="chip" data-k="'+f.id+'" style="background:'+f.color+';color:#fff">'+esc(f.name)+'</span>').join("")+'</div>'+
    '<p class="hint"><kbd>←</kbd><kbd>→</kbd> siblings · <kbd>↑</kbd>/<kbd>Esc</kbd> out · <kbd>↓</kbd> in · <kbd>/</kbd> search</p></div>';
  detailEl.querySelectorAll("[data-k]").forEach(el=>{ el.onclick=()=>{ const t=nodes[+el.dataset.k]; setFocus(t); showFamilyOrDim(t); }; });
}

// ---- outline lens ----
function buildOutline(){
  let html="";
  for(const f of families){
    html+='<details class="fam" data-fam="'+esc(f.name)+'"><summary><span class="swatch" style="background:'+f.color+'"></span>'+esc(f.name)+' <span class="badge">'+f.value+'</span></summary>';
    for(const d of f.children){
      html+='<details class="dim" data-dim="'+esc(f.name+"/"+d.name)+'"><summary>'+esc(d.name)+' <span class="badge">'+d.value+'</span></summary>';
      for(const p of d.children){
        html+='<div class="leaf" data-k="'+p.id+'"><span class="rt">'+esc(p.name)+'</span><br><span class="ol">'+esc(clip(p.one_liner,110))+'</span></div>';
      }
      html+='</details>';
    }
    html+='</details>';
  }
  outlineEl.innerHTML=html;
  outlineEl.querySelectorAll(".leaf").forEach(el=>{ el.onclick=()=>{ const t=nodes[+el.dataset.k]; selected=t; openDetail(t); }; });
}
function filterOutline(){
  if(view!=="outline") return;
  outlineEl.querySelectorAll(".fam").forEach(fam=>{
    let famVis=false;
    fam.querySelectorAll(".dim").forEach(dim=>{
      let dimVis=false;
      dim.querySelectorAll(".leaf").forEach(leaf=>{
        const p=nodes[+leaf.dataset.k];
        const show=!query || p.match;
        leaf.style.display=show?"":"none"; if(show) dimVis=true;
      });
      dim.style.display=dimVis?"":"none"; if(dimVis) famVis=true;
      if(query && dimVis) dim.open=true;
    });
    fam.style.display=famVis?"":"none";
    if(query && famVis) fam.open=true;
  });
}
function setView(v){
  view=v;
  document.querySelectorAll("#viewseg button").forEach(b=>b.classList.toggle("on", b.dataset.view===v));
  const wheelOn=(v==="wheel");
  svg.style.display=wheelOn?"":"none";
  mapSvg.style.display=wheelOn?"":"none";
  outlineEl.style.display=wheelOn?"none":"block";
  if(v==="outline" && !outlineEl.dataset.built){ buildOutline(); outlineEl.dataset.built="1"; }
  if(v==="outline") filterOutline();
  syncHash();
}
document.querySelectorAll("#viewseg button").forEach(b=>{ b.onclick=()=>setView(b.dataset.view); });

// ---- density heat ----
const heatEl=document.getElementById("heat");
function setHeat(on){ heatOn=on; heatEl.checked=on; draw(); updateMinimap(); syncHash(); }
heatEl.addEventListener("change",()=>setHeat(heatEl.checked));

// ---- keyboard nav ----
document.addEventListener("keydown",e=>{
  if(e.target===qEl){ if(e.key==="Escape"){ qEl.blur(); } return; }
  if(e.key==="/"){ e.preventDefault(); qEl.focus(); return; }
  if(e.key==="Escape"||e.key==="ArrowUp"){ if(focus.parent){ setFocus(focus.parent); showFamilyOrDim(focus); } e.preventDefault(); }
  else if(e.key==="ArrowDown"){ if(focus.children&&focus.children.length){ const c=focus.children[0]; setFocus(c); showFamilyOrDim(c); } e.preventDefault(); }
  else if(e.key==="ArrowLeft"||e.key==="ArrowRight"){
    if(focus.parent){ const sib=focus.parent.children, i=sib.indexOf(focus);
      const j=(i+(e.key==="ArrowRight"?1:-1)+sib.length)%sib.length; const c=sib[j]; setFocus(c); showFamilyOrDim(c); }
    e.preventDefault();
  }
});

// ---- deep-linkable URL state ----
function focusPath(f){ const c=chain(f).filter(n=>n!==DATA); return c.map(n=>n.name).join("/"); }
function syncHash(){
  if(_silent) return;
  const p=new URLSearchParams();
  const fp=focusPath(focus); if(fp) p.set("focus",fp);
  if(selected) p.set("p",selected.slug);
  if(query) p.set("q",query);
  if(view!=="wheel") p.set("view",view);
  if(heatOn) p.set("heat","1");
  const h=p.toString();
  history.replaceState(null,"", h?("#"+h):location.pathname+location.search);
}
function resolveFocus(fp){
  if(!fp) return DATA;
  const parts=fp.split("/");
  if(parts.length===1) return famByName[parts[0]]||DATA;
  return dimByKey[parts[0]+"/"+parts[1]]||famByName[parts[0]]||DATA;
}
function applyHash(){
  _silent=true;
  const p=new URLSearchParams(location.hash.replace(/^#/,""));
  setHeat(p.get("heat")==="1");
  setView(p.get("view")==="outline"?"outline":"wheel");
  const f=resolveFocus(p.get("focus")||"");
  setFocus(f,{silent:true});
  const q=p.get("q")||""; qEl.value=q;
  const slug=p.get("p"); const pat=slug?patBySlug[slug]:null;
  _silent=false;
  if(q){ applyQuery(); }
  else if(pat){ openDetail(pat); }
  else if(f!==DATA){ showFamilyOrDim(f); }
  else { showHome(); }
}
window.addEventListener("hashchange",()=>{ applyHash(); });

// ---- boot ----
buildMap();
if(location.hash.length>1){ applyHash(); }
else { setFocus(DATA,{silent:true}); showHome(); }
</script>
</body>
</html>
"""


def build_nested(tree: dict) -> dict:
    """Nested {name, kind, color, children} tree for the JS sunburst."""
    root = {"name": "Agent-Building Playbook", "kind": "root", "children": []}
    for fam, cfg in FAMILIES.items():
        hue = cfg["hue"]
        fnode = {
            "name": fam,
            "kind": "family",
            "gloss": FAMILY_GLOSS.get(fam, ""),
            "color": hsl_hex(hue, 55, 44),
            "children": [],
        }
        for d in cfg["dimensions"]:
            dnode = {
                "name": d,
                "kind": "dimension",
                "color": hsl_hex(hue, 52, 60),
                "children": [],
            }
            for i, p in enumerate(tree[fam][d]):
                dnode["children"].append(
                    {
                        "name": p["title"],
                        "kind": "pattern",
                        "slug": p["slug"],
                        "one_liner": p["one_liner"],
                        "also": [x for x in p["dimensions"] if x != p["primary"]],
                        "family": fam,
                        "dimension": d,
                        "color": hsl_hex(hue, 60, 85 if i % 2 == 0 else 90),
                    }
                )
            fnode["children"].append(dnode)
        root["children"].append(fnode)
    return root


def emit_html(tree: dict, patterns: list[dict]) -> str:
    import json

    data = json.dumps(build_nested(tree), ensure_ascii=False)
    return (
        EXPLORER_TEMPLATE.replace("__DATA__", data)
        .replace("__COUNT__", str(len(patterns)))
        .replace("__FAMILIES__", str(len(FAMILIES)))
        .replace("__DIMS__", str(len(DIM_TO_FAMILY)))
        .replace("__SITE_BASE__", SITE_BASE)
    )


def main() -> None:
    patterns = parse_patterns()
    tree = build_tree(patterns)
    WHEEL_DIR.mkdir(parents=True, exist_ok=True)
    (WHEEL_DIR / "taxonomy.yaml").write_text(emit_yaml(tree, patterns), encoding="utf-8")
    (WHEEL_DIR / "wheel.md").write_text(emit_md(tree, patterns), encoding="utf-8")
    (WHEEL_DIR / "wheel.dot").write_text(emit_dot(tree), encoding="utf-8")
    (WHEEL_DIR / "wheel.svg").write_text(emit_svg(tree, patterns), encoding="utf-8")
    (WHEEL_DIR / "explore.html").write_text(emit_html(tree, patterns), encoding="utf-8")
    fam_counts = ", ".join(
        f"{fam} {sum(len(tree[fam][d]) for d in cfg['dimensions'])}"
        for fam, cfg in FAMILIES.items()
    )
    print(
        f"OK: {len(patterns)} patterns -> {len(FAMILIES)} families "
        f"({fam_counts}) -> wheel/",
        file=sys.stderr,
    )
    print(
        "Wrote wheel/taxonomy.yaml, wheel/wheel.md, wheel/wheel.dot, wheel/wheel.svg",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
