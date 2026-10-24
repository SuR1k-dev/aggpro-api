// 24h liquidations by exchange (needs AGGPRO_KEY). Usage: node liquidations.mjs BTC
import { liquidations } from "./aggpro.mjs";

const asset = process.argv[2] ?? "BTC";
const j = await liquidations(asset, 5000);
const rows = Object.entries(j.by_exchange ?? {}).sort((a, b) => b[1][0] + b[1][1] - (a[1][0] + a[1][1]));
console.log(`${asset} liquidations, last 24h`);
for (const [ex, [longs, shorts]] of rows) {
  console.log(`${ex.padEnd(18)} longs $${Math.round(longs).toLocaleString()}  shorts $${Math.round(shorts).toLocaleString()}`);
}
console.log("\nLiquidation map live: https://aggpro.xyz/terminal");
