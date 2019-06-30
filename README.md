# Hexcover
A small utility package which calculates a regular hexagonal tiling for an area, given a centroid as a Shapely [Point](https://shapely.readthedocs.io/en/latest/manual.html#Point), and a side length.

# Installation
`Hexcover` is available on PyPI:  
`pip install hexcover`

# Usage
```python

from shapely.geometry import Point
from hexcover.util import hexagon_coverage

# centroid
c = Point(0.0, 0.0)
coverage = hexagon_coverage(c, 10)

# coverage is a namedtuple of seven polygons. The first entry is the central polygon.
# Subsequent entries begin directly above the central polygon, and proceed clockwise.
```
The returned `namedtuple` has seven fields:

- `centre`
- `top`
- `topright`
- `bottomright`
- `bottom`
- `bottomleft`
- `topleft`

## Examples
There's an example [notebook](hexcover.ipynb), and a sample output [GeoJSON file](coverage.geojson) showing the result of covering the [Crystal Palace Transmitting Station]() with 100-metre hexagons.

# Requirements
`Shapely` >= 1.6.3

# License
[The Blue Oak Model License 1.0](LICENSE.md)

# DOI
[![DOI](https://zenodo.org/badge/194419900.svg)](https://zenodo.org/badge/latestdoi/194419900)
