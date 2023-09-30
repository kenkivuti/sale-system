from dbservices import get_data ,insert_data
from flask import Flask,render_template
 
app=Flask(__name__)
@app.route("/")
def sales_system():
     return render_template("index.html")

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

app.run()

