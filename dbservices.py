import psycopg2

def table_name(p):
   conn = psycopg2.connect(
   database="mytest1", user='postgres', password='kenkivuti254', host='127.0.0.1', port= '5432')
   cursor = conn.cursor()
   t = "select * from"+" " + p
   cursor.execute(t)
   data = cursor.fetchall()
   return data

products=table_name("products")

# print(products)



sales = table_name("sales")
print(sales)

