# Cobertura de Qlik script

Generado por `python scripts/script_inventory.py --write`; no se edita a mano.

- Scripts del corpus: 8
- Constructs distintos: 13
- Sin cubrir por el traductor: 0
- Cubiertos sin medir en el tenant: 5 (DATE, MATCHREGEXI, NULL, PICK, TIMESTAMP)
- Scripts que traducen sueltos: 0 de 8 (un nodo de script es un fragmento con RESIDENT del resto del flujo; no mide cobertura)

| construct | tipo | scripts | estado |
| --- | --- | --- | --- |
| `DATE` | funcion | 12 | cubierto (sin medir en el tenant) |
| `PICK` | funcion | 10 | cubierto (sin medir en el tenant) |
| `TRIM` | funcion | 10 | cubierto |
| `ISNULL` | funcion | 8 | cubierto |
| `LEN` | funcion | 8 | cubierto |
| `LOAD` | sentencia | 8 | cubierto |
| `NULL` | funcion | 8 | cubierto (sin medir en el tenant) |
| `TIMESTAMP` | funcion | 8 | cubierto (sin medir en el tenant) |
| `UPPER` | funcion | 8 | cubierto |
| `DROP` | sentencia | 6 | cubierto |
| `MATCHREGEXI` | funcion | 6 | cubierto (sin medir en el tenant) |
| `COUNT` | funcion | 2 | cubierto |
| `SUM` | funcion | 2 | cubierto |
