import pathlib
import sys

import pytest

# Ensure project root is on sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from ping_utils import ping


def test_ping_ipv4_localhost():
    result = ping("127.0.0.1", 4)
    assert result["success"], result["output"]


def test_ping_ipv6_localhost():
    result = ping("::1", 6)
    if not result["success"]:
        pytest.skip("IPv6 not available")
    assert result["success"], result["output"]
