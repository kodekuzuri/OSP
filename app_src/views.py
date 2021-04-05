from app_src import app
import os
from functools import wraps
from flask import json, render_template, jsonify, make_response, send_file, request, redirect, flash, current_app
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from osp import Login, User, Item, Category, ManagerSignUp, CustomerSignUp, Seller, Buyer, SoldItem


app.secret_key = os.environ["OSP_APPKEY"]


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"


@login_manager.user_loader
def load_user(user_id):
    return User.objects(uniqueid=user_id).first()


# decorators to ensure logged in user is authorised to access the asked for functionality
def manager_required(func):
    '''If you decorate a view with this, it will ensure that the current user is a manager'''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (not current_user.is_anonymous) and current_user.GetType() != 0:
            flash("Login as manager to access this page.")
            return redirect("/signin")
        return func(*args, **kwargs)
    return decorated_view


def buyer_required(func):
    '''If you decorate a view with this, it will ensure that the current user is a buyer'''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (not current_user.is_anonymous) and current_user.GetType() != 1:
            flash("Login as buyer to access this page.")
            return redirect("/signin")
        return func(*args, **kwargs)
    return decorated_view


def seller_required(func):
    '''If you decorate a view with this, it will ensure that the current user is a seller'''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (not current_user.is_anonymous) and current_user.GetType() != 2:
            flash("Login as seller to access this page.")
            return redirect("/signin")
        return func(*args, **kwargs)
    return decorated_view
# decorators end


@app.route("/")
def index():
    if current_user.is_anonymous:
        return redirect("/signin")
    elif current_user.GetType() == 0:
        return redirect("/manager")
    elif current_user.GetType() == 1:
        return redirect("/buyer")
    elif current_user.GetType() == 2:
        return redirect("/seller")
    return redirect("/signin")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        userid = request.form["id"]
        password = request.form["password"]

        if user := Login(userid, password, 0):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("/manager")
        elif user := Login(userid, password, 1):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("/buyer")
        elif user := Login(userid, password, 2):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("/seller")
        else:
            flash("Invalid credentials.", "error")
            return render_template("signin.html")

    return render_template("signin.html")


@app.route("/signup", methods=["POST"])
def signup():
    data = request.form
    if data["type"] == "manager": 
        status, msg = ManagerSignUp(data)
    elif data["type"] == "buyer":
        status, msg = CustomerSignUp(data, isBuyer=True)
    else:
        status, msg = CustomerSignUp(data, isBuyer=False)
    
    if(status):
        flash(msg, "info")
    else:
        flash("Signup unsuccessful. Check below for more details.", "error")
        flash(msg, "error")
    return redirect("/signin")


@app.route("/logout")
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.is_authenticated = False
    user.save()
    logout_user()
    flash("Successfully logged out.", "info")
    return redirect("/signin")


# manager views start


@app.route("/manager")
@manager_required
@login_required
def manager_home():
    # user = current_user
    # return render_template("manager/home.html", user=user)
    return redirect("/dashboard")


@app.route("/manager/manage_buyers", methods=["GET", "POST"])
@manager_required
@login_required
def manager_manage_buyers():
    user = current_user
    if request.method == "POST":
        buyerid = request.form["id"]
        status, msg = user.ManageBuyer(buyerid)
        if(status):
            flash(msg, "info")
        else:
            flash(msg, "error")
        return redirect("/manager/manage_buyers")
    return render_template("manager/manage_buyers.html", buyers=Buyer.objects())


@app.route("/manager/manage_sellers", methods=["GET", "POST"])
@manager_required
@login_required
def manager_manage_sellers():
    user = current_user
    if request.method == "POST":
        sellerid = request.form["id"]
        status, msg = user.ManageSeller(sellerid)
        if(status):
            flash(msg, "info")
        else:
            flash(msg, "error")
        return redirect("/manager/manage_sellers")
    return render_template("manager/manage_sellers.html", sellers=Seller.objects())


@app.route("/manager/manage_categories", methods=["GET", "POST"])
@manager_required
@login_required
def manager_manage_categories():
    if request.method == "POST":
        if request.form["type"] == "add":
            status, msg = Category.AddCategory(request.form["name"])
        elif request.form["type"] == "remove":
            status, msg = Category.RemoveCategory(request.form["id"])
        else:
            flash("Invalid request", "error")
            return redirect("/manager/manage_categories")
        if(status):
            flash(msg,"info")
        else:
            flash(msg,"error")
        return redirect("/manager/manage_categories")
    return render_template("manager/manage_categories.html", categories=Category.objects())


@app.route("/manager/remove_item", methods=["POST"])
@manager_required
@login_required
def manager_remove_item():
    item = Item.objects(uniqueid=request.form["id"]).first()
    try:
        if not item:
            raise Exception("Item not found in database hence not removed")
        item.removeFromDB()
        flash("Item successfully removed", "info")
    except Exception as e:
        flash(str(e), "error")
    return redirect("/dashboard")


@app.route("/manager/audit")
@manager_required
@login_required
def manager_audit():
    return render_template("manager/audit.html")


# manager views end


# buyer views start


@app.route("/buyer")
@buyer_required
@login_required
def buyer_home():
    # user = current_user
    # return render_template("buyer/home.html", user=user)
    return redirect("/dashboard")


@app.route("/buyer/buy_requests", methods=["GET", "POST"])
@buyer_required
@login_required
def buyer_buy_requests():
    user = current_user
    if request.method == "POST":
        if request.form["type"] == "change":
            status, msg = user.ChangeOfferPrice(request.form["id"], request.form["offer"])
        else:
            status, msg = user.Negotiate(request.form["id"])
        if status:
            flash(msg, "info")
        else:
            flash(msg, "error")
        return redirect("/buyer/buy_requests")
        
    return render_template("buyer/buy_requests.html", user=user, buyrequests=user.GetBuyRequests())


@app.route("/buyer/past_purchases")
@buyer_required
@login_required
def buyer_past_purchases():
    user = current_user
    return render_template("buyer/past_purchases.html", user=user, items=SoldItem.objects(buyer=user.uniqueid))


@app.route("/buyer/create_buy_request", methods=["POST"])
@buyer_required
@login_required
def buyer_create_buy_request():
    user = current_user
    status, msg = user.GenerateBuyRequest(request.form["id"], request.form["offer"])
    if status:
        flash(msg, "info")
    else:
        flash(msg, "error")
    return redirect("/dashboard")

# buyer views end


# seller views start


@app.route("/seller")
@seller_required
@login_required
def seller_home():
    # user = current_user
    # return render_template("seller/home.html", user=user)
    return redirect("/dashboard")


@app.route('/seller/upload_item')
@seller_required
@login_required
def upload_items():
    user = current_user
    return render_template("seller/uploadItem.html", name=user.name)


@app.route('/seller/buy_requests', methods=["GET", "POST"])
@seller_required
@login_required
def seller_buy_requests():
    user = current_user
    if request.method == "POST":
        if request.form["type"] == "accept":
            status, msg = user.ApproveRequest(request.form["id"])
        elif request.form["type"] == "reject":
            status, msg = user.RejectRequest(request.form["id"])
        else:
            status, msg = user.ApprovePayment(request.form["id"])
        if status:
            flash(msg, "info")
        else:
            flash(msg, "error")
        return redirect("/seller/buy_requests")
    return render_template("seller/buy_requests.html", user=user, buyrequests=user.GetBuyRequests())


@app.route('/seller/uploads', methods=["GET", "POST"])
@seller_required
@login_required
def seller_uploads():
    user = current_user
    if request.method == "POST":
        item = Item.objects(uniqueid=request.form["id"]).first()
        try:
            if not item:
                raise Exception("Item not found in database hence not removed")
            item.removeFromDB()
            flash("Item successfully removed", "info")
        except Exception as e:
            flash(str(e), "error")
        return redirect("/seller/uploads")
    return render_template("seller/uploads.html", user=user, list_items=user.GetItems())


@app.route('/seller/past_sales')
@seller_required
@login_required
def seller_past_sales():
    user = current_user
    return render_template("seller/past_sales.html", user=user, items=SoldItem.objects(seller=user.uniqueid))


@app.route('/api/upload_item', methods=['POST'])
@seller_required
@login_required
def up_item():
    if request.method == 'POST':
        data=request.get_json()
        i1=Item()
        data['seller']=current_user.name
        data['photo']=data['photo'].split(',')[1]
        i1.createItem(**data)
        print(i1.__dict__)
        i1.uploadToDB()
        return make_response(
            jsonify({
                "message": "ok"
            }), 200)


# seller views end


# dashboard


@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    user = current_user
    if request.method == "POST":
        if request.form["type"] == "search_name":
            res = Item.searchItems_Name(name_=request.form["name"])
            if(res.count()):
                flash("Search results for name \'" + request.form["name"] + "\'", "info")
            else:
                flash("No items found matching name \'" + request.form["name"] + "\'", "error")
            return render_template("/show_items.html", user=user, title="Search Results", list_items=res, categories=Category.objects())
        else:
            res = Item.searchItems_Category(cat_=request.form["name"])
            if(res.count()):
                flash("Search results for category \'" + request.form["name"] + "\'", "info")
            else:
                flash("No items found in category \'" + request.form["name"] + "\'", "error")
            return render_template("/show_items.html", user=user, title="Search Results", list_items=res, categories=Category.objects())
    return render_template("/show_items.html", user=user, title="Dashboard", list_items=Item.objects(), categories=Category.objects())



# other views


@app.route('/image_item/<uid>')
@login_required
def ret_item_image(uid):
    item = Item.objects(uniqueid=uid).first()
    return send_file(item.photo, as_attachment=False, attachment_filename='item.jpeg')


@app.route('/api/category_list', methods=['POST'])
@login_required
def ret_catlist():
    if request.method == 'POST':
        cat_list = [x.name for x in Category.objects()]
        return make_response(
            jsonify({
                "message": "ok",
                "list_cat": cat_list
            }), 200)


# @app.route('/image_solditem/<uid>')
# def ret_solditem_image(uid):
#     item = SoldItem.objects(uniqueid=uid).first()
#     return send_file(item.photo, as_attachment=False, attachment_filename='item.jpeg')


# @app.route('/user/search_items')
# def search_base():
#     return render_template('/search_base.html')

# @app.route('/search_name/<name>')
# def search_item_name(name):
#     return render_template('/show_items.html',list_items=Item.searchItems_Name(name_=name))

# @app.route('/search_cat/<cat>')
# def search_item_cat(cat):
#     x=Item.searchItems_Category(cat_=cat)
#     return render_template('/show_items.html',list_items=x, user=current_user)
