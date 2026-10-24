# AggPro API — aggregated crypto order book, liquidations, funding and open interest

Python and JavaScript examples for the [AggPro](https://aggpro.xyz) API: one order book summed across
Binance, Bybit, OKX, Hyperliquid, Bitget, Gate, MEXC and 20+ other exchanges, plus liquidations,
an estimated liquidation map, open interest, funding and long/short ratios for every perpetual coin.

- Website and terminal: https://aggpro.xyz
- Full API reference: https://aggpro.xyz/docs/api (machine-readable: https://aggpro.xyz/api/v1/openapi.json)
- Free live screener of 450+ perpetual futures: https://aggpro.xyz/screener
- Coin pages (funding, OI, liquidations across exchanges): https://aggpro.xyz/markets

## No key needed: market snapshot

`GET https://aggpro.xyz/api/coins` returns the most liquid perpetual futures with price, 24h change,
open interest, funding per 8h (weighted by each exchange's open interest, fraction: `0.0001` = 0.01%),
24h liquidations `[longs, shorts]` and order book depth within ±1% `[bids, asks]`, summed across exchanges.

```bash
curl -s https://aggpro.xyz/api/coins | python -m json.tool | head -40
python python/funding_scan.py      # top coins by absolute funding, no key required
```

## With an API key (Pro / Elite)

Create a key in your account: https://aggpro.xyz/profile#api and send it in the `X-API-Key` header.

| Endpoint | What it returns |
|---|---|
| `/api/v1/book?asset=BTC:perp` | Aggregated order book: USD per level and which exchanges stand behind it |
| `/api/v1/chart?asset=ETH:perp&interval=1h` | OHLCV aggregated across exchanges with aggressive buy/sell split |
| `/api/v1/market?asset=BTC&tf=1h` | Open interest, OI change, funding, premium time series |
| `/api/v1/liquidations?asset=BTC` | Liquidations on all exchanges (last 30 days) |
| `/api/v1/liqmap?asset=BTC:perp` | Estimated liquidation levels for longs and shorts |
| `/api/v1/longshort?asset=SOL` | Long/short ratio: top traders and all accounts |
| `/api/v1/screener` | Whole-market overview, refreshed every 30 s |
| `/api/v1/usage` | Your plan and quota (free of charge) |

```bash
export AGGPRO_KEY=your_key
python python/book_walls.py BTC:perp    # largest bid/ask walls across all exchanges
node js/liquidations.mjs BTC            # 24h liquidations by exchange
```

## Files

- `python/aggpro.py` — minimal client (standard library only)
- `python/funding_scan.py` — funding extremes across exchanges (no key)
- `python/book_walls.py` — biggest walls in the aggregated order book (key)
- `js/aggpro.mjs` — minimal client for Node 18+ and browsers
- `js/liquidations.mjs` — liquidations by exchange (key)

Data is provided as is; nothing here is investment advice. MIT licensed.
