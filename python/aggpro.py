"""Minimal AggPro API client — standard library only. Docs: https://aggpro.xyz/docs/api"""

import json
import os
import urllib.parse
import urllib.request

BASE = "https://aggpro.xyz"


def get(path, key=None, **params):
    """GET an AggPro endpoint. `key` defaults to the AGGPRO_KEY environment variable."""
    key = key or os.environ.get("AGGPRO_KEY")
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"User-Agent": "aggpro-api-examples/1.0"})
    if key:
        req.add_header("X-API-Key", key)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def coins():
    """Most liquid perpetual futures with funding, OI, liquidations and depth (no key)."""
    return get("/api/coins")["coins"]


def book(asset="BTC:perp", depth=100, multiplier=10):
    """Aggregated order book across all exchanges (key)."""
    return get("/api/v1/book", asset=asset, depth=depth, multiplier=multiplier)


def liquidations(asset="BTC", limit=1000):
    """Liquidations on all exchanges (key)."""
    return get("/api/v1/liquidations", asset=asset, limit=limit)
