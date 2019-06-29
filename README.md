# Hexcover
A small utility package which calculates a regular hexagonal tiling for an area, given a centroid as a Shapely [Point](https://shapely.readthedocs.io/en/latest/manual.html#Point), and a side length.

# Example
```python

from shapely.geometry import Point
from hexcover.util import hexagon_coverage

# centroid
c = Point(0.0, 0.0)
coverage = hexagon_coverage(c, 10)

# coverage is a List of seven polygons. The first entry is the central polygon.
# Subsequent entries begin directly above the central polygon, and proceed clockwise.
```

There's also an example [notebook](hexcover.ipynb)

# Requirements
`Shapely` >= 1.6.3

# License
[The Blue Oak Model License 1.0](LICENSE.md)

# DOI
[![DOI](https://zenodo.org/badge/194419900.svg)](https://zenodo.org/badge/latestdoi/194419900)
