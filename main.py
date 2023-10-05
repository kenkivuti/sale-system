from dbservices import get_data,insert_product,insert_sales,calc_profit
from flask import Flask,render_template,request,redirect



 
app=Flask(__name__)
@app.route("/")
def sales_system():
     return render_template("index.html")


@app.route("/add-product" , methods=["POST"])
def add_product():
    pn = request.form['name']
    bp = request.form['buying_price']
    sp = request.form['selling_price']
    sq = request.form['stock_quantity']

    stored_var=(pn,bp,sp,sq)
    insert_product(stored_var)

    return redirect("/products")

@app.route("/products")
def product():
    prod = get_data("products")
    return render_template("product.html",myproducts=prod)

@app.route("/add-sale" , methods=["POST"])
def add_sales():
     productid=request.form["productid"]
     quantity = request.form['quantity']  
     store_sale=(productid,quantity)
     insert_sales(store_sale)

     return redirect("/sales")

@app.route("/sales")
def sales():
     sale=get_data("sales")
     prd=get_data("products")
     return render_template("sales.html",mysales=sale , myprd=prd)

@app.route("/dashboard")
def dashboard():
     dates = []
     profits = []
     for i  in calc_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))

     return render_template("dashboard.html" ,dates=dates,profits=profits)



app.run(debug=True)

