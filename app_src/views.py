from app_src import app
import os
from functools import wraps
from flask import json, render_template, jsonify, make_response, send_file, request, redirect, flash, current_app
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from osp import Login, User, Item, Category, ManagerSignUp, CustomerSignUp, Seller


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
            return redirect("signin")
        return func(*args, **kwargs)
    return decorated_view


def buyer_required(func):
    '''If you decorate a view with this, it will ensure that the current user is a buyer'''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (not current_user.is_anonymous) and current_user.GetType() != 1:
            flash("Login as buyer to access this page.")
            return redirect("signin")
        return func(*args, **kwargs)
    return decorated_view


def seller_required(func):
    '''If you decorate a view with this, it will ensure that the current user is a seller'''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if (not current_user.is_anonymous) and current_user.GetType() != 2:
            flash("Login as seller to access this page.")
            return redirect("signin")
        return func(*args, **kwargs)
    return decorated_view
# decorators end


@app.route("/")
def index():
    if current_user.is_anonymous:
        return redirect("signin")
    elif current_user.GetType() == 0:
        return redirect("manager")
    elif current_user.GetType() == 1:
        return redirect("buyer")
    elif current_user.GetType() == 2:
        return redirect("seller")
    return redirect("signin")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        userid = request.form["id"]
        password = request.form["password"]

        if user := Login(userid, password, 0):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("manager")
        elif user := Login(userid, password, 1):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("buyer")
        elif user := Login(userid, password, 2):
            user.is_authenticated = True
            user.save()
            login_user(user)
            return redirect("seller")
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
    return redirect("signin")


@app.route("/manager")
@manager_required
@login_required
def manager_home():
    user = current_user
    return render_template("manager/home.html", name=user.name)


@app.route("/buyer")
@buyer_required
@login_required
def buyer_home():
    user = current_user
    return render_template("buyer/home.html", name=user.name)


@app.route("/seller")
@seller_required
@login_required
def seller_home():
    user = current_user
    return render_template("seller/home.html", name=user.name)


@app.route("/logout")
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.is_authenticated = False
    user.save()
    logout_user()
    flash("Successfully logged out.", "info")
    return redirect("signin")


@app.route('/seller/upload_item')
@seller_required
@login_required
def upload_items():
    user = current_user
    return render_template("seller/uploadItem.html", name=user.name)

# this returns the file as a download :(


@app.route('/image_item/<uid>')
def index1(uid):
    item = Item.objects(uniqueid=uid).first()
    return send_file(item.photo, as_attachment=False, attachment_filename='item.jpeg')


@app.route('/api/category_list', methods=['POST'])
def ret_catlist():
    if request.method == 'POST':
        cat_list = [x.name for x in Category.objects()]
        return make_response(
            jsonify({
                "message": "ok",
                "list_cat": cat_list
            }), 200)

@app.route('/api/upload_item', methods=['POST'])
def up_item():
    if request.method == 'POST':
        data=request.get_json()
        i1=Item()
        data['seller']=current_user.name
        data['photo']=data['photo'].split(',')[1]
        print("hihihihi")
        i1.createItem(**data)
        print("hihihihi")
        print(i1.__dict__)
        i1.uploadToDB()
        print("hihihihi")
        return make_response(
            jsonify({
                "message": "ok"
            }), 200)