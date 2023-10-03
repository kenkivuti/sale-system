from dbservices import get_data,insert_product
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
@app.route("/sales")
def sales():
     sale=get_data("sales")
     return render_template("sales.html",mysales=sale)

@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html")

app.run(debug=True)

