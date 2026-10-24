// Minimal AggPro API client for Node 18+ and browsers. Docs: https://aggpro.xyz/docs/api
const BASE = "https://aggpro.xyz";

export async function get(path, params = {}, key = globalThis.process?.env?.AGGPRO_KEY) {
  const qs = Object.keys(params).length ? `?${new URLSearchParams(params)}` : "";
  const r = await fetch(`${BASE}${path}${qs}`, { headers: key ? { "X-API-Key": key } : {} });
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
  return r.json();
}

/** Most liquid perpetual futures with funding, OI, liquidations and depth (no key). */
export const coins = async () => (await get("/api/coins")).coins;
/** Aggregated order book across all exchanges (key). */
export const book = (asset = "BTC:perp", depth = 100) => get("/api/v1/book", { asset, depth });
/** Liquidations on all exchanges (key). */
export const liquidations = (asset = "BTC", limit = 1000) => get("/api/v1/liquidations", { asset, limit });
