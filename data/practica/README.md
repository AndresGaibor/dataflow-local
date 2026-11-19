# Datasets sintéticos para Qlik Data Flow

Todos los datos son ficticios y fueron generados para práctica.

## Orden recomendado
1. clientes.csv
2. cuentas.csv
3. transacciones.csv
4. strings_sucios.csv / fechas_sucias.csv / numeros_sucios.csv
5. transacciones_enero.csv + febrero + marzo
6. join_nn_a.csv + join_nn_b.csv
7. transacciones_mensuales.xlsx
8. pivot_con_null.csv / pivot_520_categorias.csv
9. window_transacciones_control.csv
10. clientes_sucios.csv para calidad de datos

## Errores intencionales
- Vacíos y NULL conceptuales.
- Ciudades con espacios y variaciones de mayúsculas/minúsculas.
- Correos y teléfonos inválidos.
- Fechas con formatos mixtos e inválidos.
- Montos con separadores decimales/miles diferentes.
- 10 cuentas huérfanas.
- 20 IDs de transacción duplicados.
- Estados desconocidos.
- Comercios con nombres parecidos para fuzzy matching.
- Caso N:N 3 x 5 = 15.
- Pivot con 520 categorías distintas.
- Pivot con categoría vacía.

00_controles_esperados.csv es solo para validar ejercicios, no como fuente de transformación.
