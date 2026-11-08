import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')


# # --------------- JOIN all records from orderDetails and products ---------------
# query1 = """
# SELECT * 
#     FROM orderDetails
#         JOIN products
#         ON orderdetails.productCode = products.productCode
#         LIMIT 10
# """
# print(pd.read_sql(query, conn))

# # --------------- SELECT all records from orderDetails and display first 10 ---------------
# query2 = """
# SELECT * 
#     FROM orderDetails
#     LIMIT 10
# """
# print(pd.read_sql(query2, conn))


# # --------------- SELECT all records from products and display first 10 ---------------
# query3 = """
# SELECT * 
#     FROM products
#     LIMIT 10
# """
# print(pd.read_sql(query3, conn))


# # --------------- JOIN all records from orderDetails and products and join them on productCode with USING() ---------------
# query4 = """
# SELECT * 
#     FROM orderDetails
#         JOIN products
#         USING(productCode)
#         LIMIT 10
# """
# print(pd.read_sql(query4, conn))


# # --------------- Aliasing table names to shorten overall query ---------------
# query5 = """
# SELECT * 
#     FROM orderDetails AS od
#         JOIN products as p
#         ON od.productCode = p.productCode
#         LIMIT 10
# """
# print(pd.read_sql(query5, conn))


# # --------------- LEFT JOIN all records from products and join all records in orderDetails on productcode ---------------
# query6 = """
# SELECT * 
#     FROM products
#         LEFT JOIN orderdetails
#         USING(productcode)
# """
# df = pd.read_sql(query6, conn)

# print("Number of records returned: ", len(df))
# print("Number of records where order details are null: ", len(df[df.orderNumber.isnull()]))
# print(df[df.orderNumber.isnull()])


# --------------- Aliasing table names to shorten overall query ---------------
query7 = """
SELECT * 
    FROM customers AS c
        JOIN employees AS e
        ON c.salesRepEmployeeNumber = e.employeeNumber
        ORDER BY employeeNumber
"""
print(pd.read_sql(query7, conn))


conn.close()