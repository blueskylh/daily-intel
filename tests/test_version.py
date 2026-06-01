from daily_intel_900.version import __version__


def test_version_format():
    parts = __version__.split(".")
    assert len(parts) == 3
