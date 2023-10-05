import psycopg2
from datetime import date
conn = psycopg2.connect(database="dukaclass", user='postgres', password='kenkivuti254', host='127.0.0.1', port= '5432')

cur = conn.cursor()
# select function
def get_data(p):
   cur = conn.cursor()
   t = "select * from " + p
   cur.execute(t)
   data = cur.fetchall()
   return data

# insert function
def insert_product(values):
        # Connect to the PostgreSQL database
        cur = conn.cursor()

        # Execute the INSERT statement
        column_product="(name,buying_price,selling_price,stock_quantity)"
       
        store_products= f"INSERT INTO products{column_product}VALUES{values}"
    
        cur.execute(store_products,values)
        # Commit the transaction
        conn.commit()

        return True

def insert_sales(values):
      column_sales="(productid,quantity,created_at)"
      store_sales=f"INSERT INTO sales{column_sales} VALUES(%s,%s,'now()')"

      cur.execute(store_sales,values)



def calc_profit():
      calc_query="select DATE(created_at) AS Date, sum((selling_price -buying_price)*quantity) as profit from sales join products on products.id=sales.productid group by Date order by date"
      cur.execute(calc_query)
      fetch=cur.fetchall()
      return fetch
# test = calc_profit()
# print(test)




