import psycopg2


conn = psycopg2.connect(
database="dukaclass", user='postgres', password='kenkivuti254', host='127.0.0.1', port= '5432')
def table_name(p):
   cursor = conn.cursor()
   t = "select * from"+" " + p
   cursor.execute(t)
   data = cursor.fetchall()
   return data

products=table_name("products")

# print(products)



sales = table_name("sales")
# print(sales)


# def input_data(pro):
#    conn = psycopg2.connect(
#    database="dukaclass", user='postgres', password='kenkivuti254', host='127.0.0.1', port= '5432')
#    cursor = conn.cursor()
#    t = "insert into  "+" " + pro + " (name,buying_price,selling_price,stock_quantity)values()"
#    cursor.execute(t)
#    data = cursor.fetchall()
#    return data




def insert_data():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database="dukaclass", user="postgres", password="kenkivuti254", host="127.0.0.1", port="5432")
        cur = conn.cursor()

        # Execute the INSERT statement
        cur.execute("INSERT INTO products (name, buying_price,selling_price,stock_quantity) VALUES (%s, %s, %s, %s)", ("yoghurt", "20","50","10"))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        print("Data inserted successfully!")  
    except (Exception, psycopg2.Error) as error:
            print("Error while inserting data:", error)

total=insert_data()
print(total)