import unittest

from src import cpi


class TestSeries(unittest.TestCase):
    def test_covers_the_project_era(self):
        for year in (1913, 1960, 1980, 2000, 2020):
            self.assertIn(year, cpi.CPI)

    def test_base_year_present(self):
        self.assertIn(cpi.BASE_YEAR, cpi.CPI)

    def test_values_are_positive(self):
        self.assertTrue(all(v > 0 for v in cpi.CPI.values()))

    def test_spot_check_known_annual_averages(self):
        # CPI-U annual averages, 1982-84 = 100. Loose tolerances: these pin the
        # series to the right scale and shape, not to a specific vintage.
        self.assertAlmostEqual(cpi.CPI[1960], 29.6, delta=0.5)
        self.assertAlmostEqual(cpi.CPI[1980], 82.4, delta=1.0)
        self.assertAlmostEqual(cpi.CPI[2000], 172.2, delta=1.5)
        self.assertAlmostEqual(cpi.CPI[2020], 258.8, delta=2.0)

    def test_broadly_increasing(self):
        # Deflation years exist (1930s, 2009), so require the trend rather than
        # strict monotonicity.
        self.assertLess(cpi.CPI[1950], cpi.CPI[1970])
        self.assertLess(cpi.CPI[1970], cpi.CPI[1990])
        self.assertLess(cpi.CPI[1990], cpi.CPI[2010])


class TestNominalThreshold(unittest.TestCase):
    def test_base_year_threshold_is_the_constant_amount(self):
        self.assertAlmostEqual(cpi.nominal_threshold(cpi.BASE_YEAR),
                               float(cpi.THRESHOLD_CONSTANT), delta=1.0)

    def test_1960_threshold_is_roughly_a_tenth(self):
        # $10M constant 2026 dollars was around $0.9-1.1M nominal in 1960.
        value = cpi.nominal_threshold(1960)
        self.assertGreater(value, 700_000)
        self.assertLess(value, 1_400_000)

    def test_older_years_need_smaller_nominal_revenue(self):
        self.assertLess(cpi.nominal_threshold(1960),
                        cpi.nominal_threshold(1990))
        self.assertLess(cpi.nominal_threshold(1990),
                        cpi.nominal_threshold(2020))

    def test_accepts_a_custom_constant_amount(self):
        # The acq50 threshold is $50M constant, five times rev10's.
        self.assertAlmostEqual(cpi.nominal_threshold(1980, 50_000_000),
                               5 * cpi.nominal_threshold(1980), delta=1.0)

    def test_unknown_year_raises(self):
        with self.assertRaises(KeyError):
            cpi.nominal_threshold(1800)


class TestToConstant(unittest.TestCase):
    def test_round_trip(self):
        nominal = cpi.nominal_threshold(1960)
        self.assertAlmostEqual(cpi.to_constant(nominal, 1960),
                               float(cpi.THRESHOLD_CONSTANT), delta=1.0)

    def test_1960_dollars_are_worth_more(self):
        self.assertGreater(cpi.to_constant(1_000_000, 1960), 8_000_000)


if __name__ == "__main__":
    unittest.main()
