"""Wave composition.

Growing the sample by whichever names are easiest to research next causes
composition drift toward well-documented US software figures as N rises,
which would make a 'stabilising' median partly an artifact of the sample
changing shape. Each wave is therefore apportioned so that cumulative
composition tracks the frozen frame at every N.
"""

import sys

from src import schema


def apportion(total, shares):
    """Largest-remainder apportionment of `total` across percentage `shares`."""
    exact = {b: total * shares[b] / 100.0 for b in shares}
    base = {b: int(exact[b]) for b in shares}
    remainder = total - sum(base.values())
    # Biggest fractional part wins; ties broken by bucket name for determinism.
    order = sorted(shares, key=lambda b: (-(exact[b] - base[b]), b))
    for bucket in order[:remainder]:
        base[bucket] += 1
    return base


def allocate_wave(cumulative, wave_size, shares=None):
    """Return {bucket: count} for the next wave of `wave_size` people."""
    if shares is None:
        shares = schema.BUCKET_SHARES

    total_after = sum(cumulative.get(b, 0) for b in shares) + wave_size
    ideal = apportion(total_after, shares)
    wave = {b: max(0, ideal[b] - cumulative.get(b, 0)) for b in shares}

    def deviation(bucket):
        """How far this bucket sits above its exact quota, if we ship as-is."""
        got = cumulative.get(bucket, 0) + wave[bucket]
        return got - total_after * shares[bucket] / 100.0

    # Clamping at zero can leave the wave over- or under-sized. Trim from the
    # most over-quota bucket, add to the most under-quota one, until exact.
    diff = sum(wave.values()) - wave_size
    while diff > 0:
        bucket = max((b for b in wave if wave[b] > 0), key=deviation)
        wave[bucket] -= 1
        diff -= 1
    while diff < 0:
        bucket = min(wave, key=deviation)
        wave[bucket] += 1
        diff += 1

    return wave


def main(argv):
    """Print the next wave's bucket allocation given cumulative counts."""
    if len(argv) < 2:
        print("usage: python3 -m src.allocate <wave_size> "
              "[bucket=count ...]")
        return 2
    wave_size = int(argv[1])
    cumulative = {}
    for pair in argv[2:]:
        bucket, count = pair.split("=")
        cumulative[bucket] = int(count)
    for bucket, count in sorted(allocate_wave(cumulative, wave_size).items()):
        print("%-30s %d" % (bucket, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
