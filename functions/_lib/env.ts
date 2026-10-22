export interface Env {
  DB: D1Database;
  WOMPI_PUBLIC_KEY: string;
  WOMPI_PRIVATE_KEY: string;
  WOMPI_INTEGRITY_SECRET: string;
  WOMPI_EVENTS_SECRET: string;
  WOMPI_API: string;        // https://sandbox.wompi.co/v1  |  https://production.wompi.co/v1
  PRICE_CENTS?: string;     // por defecto 2990000 (COP 29.900)
  SITE_URL: string;
}
export const PRICE_CENTS_DEFAULT = 2990000;
export const json = (o: unknown, status = 200) => new Response(JSON.stringify(o), { status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
