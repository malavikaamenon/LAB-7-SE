from hypothesis import given, strategies as st

from processor import (
    parse_storage_quota,
    compute_compression_ratio,
    lookup_bandwidth_tier_rate,
)


@given(st.text() | st.none())
def test_parse_storage_quota_no_crash(s):
    try:
        parse_storage_quota(s)
    except Exception as e:
        assert False, f"parse_storage_quota crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_compute_compression_ratio_safe(s):
    try:
        compute_compression_ratio(s)
    except Exception as e:
        assert False, f"compute_compression_ratio crashed with input {s!r}: {e}"


@given(st.text() | st.none())
def test_lookup_bandwidth_tier_rate_safe(s):
    try:
        lookup_bandwidth_tier_rate(s)
    except Exception as e:
        assert False, f"lookup_bandwidth_tier_rate crashed with input {s!r}: {e}"


# Valid-input checks ensure that defensive handling does not break normal use.
def test_parse_storage_quota_valid_values():
    assert parse_storage_quota("500MB") == "Quota: 0.50 GB"
    assert parse_storage_quota("20GB") == "Quota: 20.00 GB"
    assert parse_storage_quota("2TB") == "Quota: 2000.00 GB"


def test_compute_compression_ratio_valid_value():
    assert compute_compression_ratio("1024:256") == 4.0


def test_lookup_bandwidth_tier_rate_valid_values():
    assert lookup_bandwidth_tier_rate("HOT_TIER") == 0.08
    assert lookup_bandwidth_tier_rate("cold") == 0.05
    assert lookup_bandwidth_tier_rate("ARCHIVE") == 0.02


# Invalid-input checks document the expected safe response.
def test_invalid_inputs_return_none():
    assert parse_storage_quota(None) is None
    assert parse_storage_quota("20XX") is None
    assert compute_compression_ratio("10:0") is None
    assert compute_compression_ratio("abc:20") is None
    assert lookup_bandwidth_tier_rate(None) is None
    assert lookup_bandwidth_tier_rate("UNKNOWN") is None
