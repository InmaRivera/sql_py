import sqlite3
import pandas as pd


# def square(n): return n*n
# square = lambda n : n*n
def square(n): return n*n


# con with la conexion se cierra automáticamente
with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square", 1, square)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT *,square(Price) as Precio_al_cuadrado FROM Products WHERE Price > 0')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

print(results_df)
