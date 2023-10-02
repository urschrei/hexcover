"""
Tests for Hexcover

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

import unittest

from shapely.geometry import Point
from hexcover.util import hexagon_coverage
from array import array


class HexcoverTests(unittest.TestCase):
    """Tests for hexcover"""

    def setUp(self):
        """make these available to all tests"""
        self.c = Point(0.0, 0.0)

    def testCoverage(self):
        """Test that numpy arrays can be consumed and returned"""
        coverage = hexagon_coverage(self.c, 10)
        self.assertEqual(
            coverage.centre.centroid.xy,
            (
                array("d", [-2.9172056160841026e-16]),
                array("d", [5.834411232168205e-16]),
            ),
        )
