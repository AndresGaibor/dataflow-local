# Cobertura de Qlik script

Generado por `python scripts/script_inventory.py --write`; no se edita a mano.

- Scripts del corpus: 8
- Constructs distintos: 13
- Sin cubrir por el traductor: 5
- Scripts que traducen sueltos: 0 de 8 (un nodo de script es un fragmento con RESIDENT del resto del flujo; no mide cobertura)

## Constructs sin cubrir

- `DATE` (funcion, 12 scripts)
- `MATCHREGEXI` (funcion, 6 scripts)
- `NULL` (funcion, 8 scripts)
- `PICK` (funcion, 10 scripts)
- `TIMESTAMP` (funcion, 8 scripts)

| construct | tipo | scripts | estado |
| --- | --- | --- | --- |
| `DATE` | funcion | 12 | no cubierto |
| `PICK` | funcion | 10 | no cubierto |
| `TRIM` | funcion | 10 | cubierto |
| `ISNULL` | funcion | 8 | cubierto |
| `LEN` | funcion | 8 | cubierto |
| `LOAD` | sentencia | 8 | cubierto |
| `NULL` | funcion | 8 | no cubierto |
| `TIMESTAMP` | funcion | 8 | no cubierto |
| `UPPER` | funcion | 8 | cubierto |
| `DROP` | sentencia | 6 | cubierto |
| `MATCHREGEXI` | funcion | 6 | no cubierto |
| `COUNT` | funcion | 2 | cubierto |
| `SUM` | funcion | 2 | cubierto |
