"""Largest walls in the aggregated order book (needs AGGPRO_KEY). Usage: python book_walls.py BTC:perp"""

import sys

from aggpro import book

asset = sys.argv[1] if len(sys.argv) > 1 else "BTC:perp"
b = book(asset, depth=300)
mid = b["mid"]
for side in ("bids", "asks"):
    top = sorted(b[side], key=lambda l: l["usd"], reverse=True)[:5]
    print(f"\n{side.upper()} — {asset}, mid {mid}")
    for l in top:
        venues = ", ".join(f"{e} ${u:,.0f}" for e, u in l["ex"][:3])
        print(
            f"  {l['p']:>12} ({(l['p'] / mid - 1) * 100:+.2f}%)  ${l['usd']:>14,.0f}  {venues}"
        )
print("\nSee it live: https://aggpro.xyz/terminal")
