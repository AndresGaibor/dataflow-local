CREATE TABLE public.transacciones (
  transaccion_id text, cuenta_id text, cliente_id text, fecha_ts text, fecha_raw text, tipo text,
  monto numeric, monto_texto text, canal text, ciudad text, comercio text, estado text);
COPY public.transacciones FROM '/data/transacciones.csv' CSV HEADER;
