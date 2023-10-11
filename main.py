from dbservices import get_data,insert_product,insert_sales,calc_profit,create_users,email_pass,email_and_pas
from flask import Flask,render_template,request,redirect,session,url_for



 
app=Flask(__name__)
app.secret_key='kenkivuti'

# def login_check():
#     if session['email'] != None:
#         return redirect(url_for('dashbord'))
#     return redirect(url_for('user_login'))




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
     # login_check()
     dates = []
     profits = []
     for i  in calc_profit():
        dates.append(str(i[0]))
        profits.append(float(i[1]))

     return render_template("dashboard.html" ,dates=dates,profits=profits)



@app.route("/register", methods=['GET','POST'])
def user_register():
   if request.method=="POST":
     fn=request.form['full_name']
     em=request.form['email']
     ps=request.form['password']
     stored_value=(fn,em,ps)
     create_users(stored_value)

     return redirect(url_for("user_login"))

   return render_template("register.html")



@app.route("/login" , methods=['POST','GET'])
def user_login():
   if request.method == 'POST': 
       m_email=request.form.get('email')
       m_pass=request.form.get('password')
       user_access=email_and_pas(m_email,m_pass)

       if user_access:
           session['userid'] = user_access
          #  session['full_name'] = user_access[1]
           return redirect("/dashbord")
       else:
         return redirect(url_for("user_login"))



app.run(debug=True)

