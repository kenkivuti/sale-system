from dbservices import get_data,insert_product,insert_sales
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
     return render_template("dashboard.html")

app.run(debug=True)

