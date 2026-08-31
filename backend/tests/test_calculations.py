import unittest

from app.calculations.heat_duty import calculate_qs, calculate_qt
from app.calculations.heat_transfer import (
    approach_temperature,
    calculate_adeltln,
    calculate_u_shell,
    calculate_u_tube,
)
from app.calculations.lmtd import corrected_lmtd


class HeatDutyTests(unittest.TestCase):
    def test_shell_side_heat_duty(self):
        self.assertAlmostEqual(calculate_qs(1000, 4200, 150, 100), 210)

    def test_tube_side_heat_duty(self):
        self.assertAlmostEqual(calculate_qt(1000, 4200, 50, 100), 210)


class HeatTransferTests(unittest.TestCase):
    def test_corrected_lmtd(self):
        self.assertAlmostEqual(corrected_lmtd(50, 0.85), 42.5)

    def test_area_temperature_product(self):
        self.assertAlmostEqual(calculate_adeltln(100, 42.5), 4250)

    def test_overall_heat_transfer_coefficients(self):
        self.assertAlmostEqual(calculate_u_shell(2.125, 4250), 500)
        self.assertAlmostEqual(calculate_u_tube(2.125, 4250), 500)

    def test_approach_temperature(self):
        self.assertEqual(approach_temperature(150, 120), 30)


if __name__ == "__main__":
    unittest.main()
