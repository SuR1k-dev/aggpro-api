"""Funding extremes across exchanges — no API key needed. Live pages: https://aggpro.xyz/markets"""

from aggpro import coins

rows = [c for c in coins() if c.get("funding") is not None]
rows.sort(key=lambda c: abs(c["funding"]), reverse=True)
print(f"{'coin':<8}{'funding/8h':>12}{'OI, USD':>16}{'liq 24h':>14}  exchanges")
for c in rows[:15]:
    liq = sum(c.get("liq24h") or [0, 0])
    print(
        f"{c['base']:<8}{c['funding'] * 100:>11.4f}%{c['oi'] or 0:>16,.0f}{liq:>14,.0f}  {c['venues']}"
    )
if rows:
    print("\nLive: https://aggpro.xyz/markets/" + rows[0]["base"].lower())
