import psycopg2

conn = psycopg2.connect(database="dukaclass", user='postgres', password='kenkivuti254', host='127.0.0.1', port= '5432')
# select function

def get_data(p):
   cur = conn.cursor()
   t = "select * from " + p
   cur.execute(t)
   data = cur.fetchall()
   return data

# insert function
def insert_data(table_product,table_sales):
        # Connect to the PostgreSQL database
        cur = conn.cursor()

        # Execute the INSERT statement
        column_product="(name,buying_price,selling_price,stock_quantity)"
        values_product="('manjibisc',40,80,10)"
        column_sales="(productid,quantity,created_at)"
        values_sales="(23,10,now())"
        store_products= f"INSERT INTO {table_product}{column_product}VALUES{values_product}"
        store_sales=f"INSERT INTO {table_sales}{column_sales}VALUES{values_sales}"
        cur.execute(store_products)
        cur.execute(store_sales)
        # Commit the transaction
        conn.commit()

        return True



