import math
import re


def parse_storage_quota(quota_str):
    """
    Parse a storage quota into GB.

    Accepted format: a non-negative integer followed by MB, GB, or TB.
    Returns a formatted string for valid input and None for invalid input.
    """
    if not isinstance(quota_str, str):
        return None

    match = re.fullmatch(r"\s*(\d+)\s*(MB|GB|TB)\s*", quota_str, re.IGNORECASE)
    if not match:
        return None

    value = int(match.group(1))
    unit = match.group(2).upper()
    multipliers = {"MB": 0.001, "GB": 1.0, "TB": 1000.0}
    gb_total = value * multipliers[unit]
    return f"Quota: {gb_total:.2f} GB"


def compute_compression_ratio(size_metric_str):
    """
    Compute raw_bytes / compressed_bytes.

    Accepted format: 'raw_bytes:compressed_bytes'. Both values must be
    finite and non-negative, and compressed_bytes must be greater than zero.
    Returns the rounded ratio for valid input and None for invalid input.
    """
    if not isinstance(size_metric_str, str):
        return None

    parts = size_metric_str.split(":")
    if len(parts) != 2:
        return None

    try:
        raw_bytes = float(parts[0].strip())
        comp_bytes = float(parts[1].strip())
    except (TypeError, ValueError, OverflowError):
        return None

    if not math.isfinite(raw_bytes) or not math.isfinite(comp_bytes):
        return None
    if raw_bytes < 0 or comp_bytes <= 0:
        return None

    ratio = raw_bytes / comp_bytes
    if not math.isfinite(ratio):
        return None
    return round(ratio, 2)


def lookup_bandwidth_tier_rate(tier_descriptor):
    """
    Look up the egress rate for HOT, COL, or ARC tier descriptors.
    Matching is case-insensitive and ignores surrounding whitespace.
    Returns the rate for valid input and None for invalid/unknown input.
    """
    if not isinstance(tier_descriptor, str):
        return None

    cleaned = tier_descriptor.strip().upper()
    if not cleaned:
        return None

    tier_rates = {"HOT": 0.08, "COL": 0.05, "ARC": 0.02}
    prefix = cleaned[:3]
    return tier_rates.get(prefix)


def main():
    print("==== Running parse_storage_quota ====")
    q_input = input("Enter quota (e.g. 500MB, 10GB, 2TB): ")
    result = parse_storage_quota(q_input)
    print(result if result is not None else "Invalid storage quota.")

    print("\n==== Running compute_compression_ratio ====")
    c_input = input("Enter raw:compressed bytes (e.g. 1024:256): ")
    result = compute_compression_ratio(c_input)
    print("Compression Ratio:", result if result is not None else "Invalid size metrics.")

    print("\n==== Running lookup_bandwidth_tier_rate ====")
    t_input = input("Enter tier descriptor (e.g. HOT_TIER, COLD, ARCHIVE): ")
    result = lookup_bandwidth_tier_rate(t_input)
    print("Rate per GB: $", result if result is not None else "Unknown bandwidth tier.")


if __name__ == "__main__":
    main()
