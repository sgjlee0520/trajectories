import unittest

from src import allocate
from src import schema


class TestApportion(unittest.TestCase):
    def test_sums_to_total(self):
        result = allocate.apportion(25, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 25)

    def test_exact_at_100(self):
        result = allocate.apportion(100, schema.BUCKET_SHARES)
        self.assertEqual(result["software_internet"], 25)
        self.assertEqual(result["trade_import_logistics"], 5)

    def test_zero_total(self):
        result = allocate.apportion(0, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 0)

    def test_largest_remainder_favours_biggest_share(self):
        # 10 items across the frame: software (25%) must get the most.
        result = allocate.apportion(10, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 10)
        self.assertEqual(max(result, key=lambda b: result[b]),
                         "software_internet")


class TestAllocateWave(unittest.TestCase):
    def test_first_wave_sums_to_wave_size(self):
        wave = allocate.allocate_wave({}, 25)
        self.assertEqual(sum(wave.values()), 25)

    def test_never_negative(self):
        skewed = {"software_internet": 40}
        wave = allocate.allocate_wave(skewed, 25)
        self.assertTrue(all(count >= 0 for count in wave.values()))
        self.assertEqual(sum(wave.values()), 25)

    def test_corrects_an_over_represented_bucket(self):
        # Software is wildly over-quota, so the next wave should add few or
        # none of it and backfill the starved buckets instead.
        skewed = {"software_internet": 40, "science_research": 0}
        wave = allocate.allocate_wave(skewed, 25)
        self.assertEqual(wave["software_internet"], 0)
        self.assertGreater(wave["science_research"], 0)

    def test_composition_tracks_frame_across_many_waves(self):
        cumulative = {}
        for _ in range(8):
            wave = allocate.allocate_wave(cumulative, 25)
            for bucket, count in wave.items():
                cumulative[bucket] = cumulative.get(bucket, 0) + count
        total = sum(cumulative.values())
        self.assertEqual(total, 200)
        # Every bucket within 1 person of its exact quota after 200.
        for bucket, share in schema.BUCKET_SHARES.items():
            expected = total * share / 100.0
            self.assertLessEqual(abs(cumulative[bucket] - expected), 1.0,
                                 "%s drifted: %d vs %.1f"
                                 % (bucket, cumulative[bucket], expected))


if __name__ == "__main__":
    unittest.main()
