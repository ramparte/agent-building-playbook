# The Agent-Building Playbook Wheel

A "flavor wheel" projection of the pattern library: simple at the center (a few
broad **families**), finer toward the edge (**dimensions**, then individual
**patterns**). One canonical home per pattern (its primary dimension); every
other tag it carries is preserved as a cross-reference.

## Regenerate

```sh
python3 scripts/build-wheel.py
```

Everything is derived from `patterns/*.md`. Re-cut the wheel by editing the
`FAMILIES` config block at the top of `scripts/build-wheel.py` (family names,
groupings, colors) — no other code changes needed.

## Outputs

| File | Form | Tracked? |
|------|------|----------|
| `taxonomy.yaml` | Canonical structured taxonomy (family → dimension → pattern) | yes |
| `wheel.md` | Human/agent-readable outline | yes |
| `wheel.dot` | Graphviz radial graph | yes |
| `wheel.svg` | Static flavor-wheel image | no (build output) |
| `wheel.png` | Rasterized wheel | no (build output) |
| `explore.html` | Interactive zoomable-sunburst explorer | no (build output) |

The rendered visual/interactive files are regenerable build artifacts (like the
generated wiki HTML) and are git-ignored; they are published to the live site.

## Explore it live

The interactive explorer ships on the site as `explore.html` (linked from the
pattern list). Zoom by clicking wedges, click the center to zoom out, search,
switch between the wheel and an outline lens, toggle a density heat-map, and
deep-link any view via the URL.
