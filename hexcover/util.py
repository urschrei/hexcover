"""
util.py

Created by Stephan Hügel on 2019-06-28

This file is part of hexcover.

Copyright (c) 2019 Stephan Hügel

Blue Oak Model License Version 1.0.0

Purpose
This license gives everyone as much permission to work with this
software as possible, while protecting contributors from liability.

Acceptance
In order to receive this license, you must agree to its rules. The
rules of this license are both obligations under that agreement and conditions
to your license. You must not do anything with this software that triggers a
rule that you cannot or will not follow.

Copyright
Each contributor licenses you to do everything with this software that
would otherwise infringe that contributor’s copyright in it.

Notices
You must ensure that everyone who gets a copy of any part of this
software from you, with or without changes, also gets the text of this license
or a link to https://blueoakcouncil.org/license/1.0.0.

Excuse
If anyone notifies you in writing that you have not complied with
Notices, you can keep your license by taking all practical steps to comply
within 30 days after the notice. If you do not do so, your license ends
immediately.

Patent
Each contributor licenses you to do everything with this software that
would otherwise infringe any patent claims they can license or become able to
license.

Reliability
No contributor can revoke this license.

No Liability
As far as the law allows, this software comes as is, without any
warranty or condition, and no contributor will be liable to anyone for any
damages related to this software or this license, under any kind of legal claim.

"""

__author__ = "Stephan Hügel <shugel@tcd.ie>"
__version__ = "0.5.0"

from shapely.geometry import Polygon
from shapely.affinity import translate
import math
from collections import namedtuple


Hexagons = namedtuple(
    "Hexagons",
    ["centre", "top", "topright", "bottomright", "bottom", "bottomleft", "topleft"],
)


def _flat_hex_coords(centre, size, i):
    """Return the point coordinate of a flat-topped regular hexagon.
    points are returned in counter-clockwise order as i increases
    the first coordinate (i=0) will be:
    centre.x + size, centre.y

    """
    angle_deg = 60 * i
    angle_rad = math.pi / 180 * angle_deg
    return (
        centre.x + size * math.cos(angle_rad),
        centre.y + size * math.sin(angle_rad),
    )


def _flat_hex_polygon(centre, size):
    """Return a flat-topped regular hexagonal Polygon, given a centroid Point and side length"""
    return Polygon([_flat_hex_coords(centre, size, i) for i in range(6)])


def hexagon_coverage(centre, size):
    """Tile an area having a Shapely Point centroid _centre_ with regular flat-topped
    hexagonal polygons having side-length _size_.
    The returned namedtuple has seven entries:
    0 is the central polygon, 1 - 6 are surrounding polygons, beginning directly
    above 0, progressing clockwise.

    """
    cp = _flat_hex_polygon(centre, size)
    width = 2 * size
    height = math.sqrt(3) * size
    horizontal_distance = width * 0.75
    vertical_distance = height * 0.5
    # second hex is directly above central_polygon, progresses clockwise
    return Hexagons(
        cp,
        translate(cp, 0, vertical_distance * 2),
        translate(cp, horizontal_distance, vertical_distance),
        translate(cp, horizontal_distance, -vertical_distance),
        translate(cp, 0, vertical_distance * -2),
        translate(cp, -horizontal_distance, vertical_distance),
        translate(cp, -horizontal_distance, -vertical_distance),
    )
