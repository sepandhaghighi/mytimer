# -*- coding: utf-8 -*-
"""Regression test: --set-on with out-of-range clock values must exit cleanly."""
import unittest

from mytimer.functions import update_set_on_params
from mytimer.params import DEFAULT_PARAMS


class TestSetOnValidation(unittest.TestCase):
    def _params(self, **overrides):
        params = DEFAULT_PARAMS.copy()
        params.update(overrides)
        return params

    def test_hour_out_of_range_exits_cleanly(self):
        with self.assertRaises(SystemExit) as ctx:
            update_set_on_params(self._params(hour=25, minute=0, second=5))
        self.assertEqual(ctx.exception.code, 1)

    def test_minute_out_of_range_exits_cleanly(self):
        with self.assertRaises(SystemExit) as ctx:
            update_set_on_params(self._params(hour=10, minute=70, second=0))
        self.assertEqual(ctx.exception.code, 1)

    def test_second_out_of_range_exits_cleanly(self):
        with self.assertRaises(SystemExit) as ctx:
            update_set_on_params(self._params(hour=10, minute=30, second=99))
        self.assertEqual(ctx.exception.code, 1)

    def test_boundary_values_are_accepted(self):
        # Must not raise; diff to the next 23:59:59 is a valid countdown.
        params = update_set_on_params(self._params(hour=23, minute=59, second=59))
        self.assertTrue(0 <= params["hour"] <= 23)
        self.assertTrue(0 <= params["minute"] <= 59)
        self.assertTrue(0 <= params["second"] <= 59)


if __name__ == "__main__":
    unittest.main()
