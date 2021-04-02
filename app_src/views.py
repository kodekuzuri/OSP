from app_src import app
from functools import wraps
from flask import render_template, jsonify, make_response, send_file, request, redirect, flash, current_app
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from osp import Login, User, Item

# make this environment variable finally
app.secret_key = "testing_for_now_change_in_the_future"


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


@app.route("/manager")
@manager_required
@login_required
def manager_home():
    user = current_user
    return render_template("manager/base.html", name=user.name)


@app.route("/buyer")
@buyer_required
@login_required
def buyer_home():
    user = current_user
    return render_template("buyer/base.html", name=user.name)


@app.route("/seller")
@seller_required
@login_required
def seller_home():
    user = current_user
    return render_template("seller/base.html", name=user.name)

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


## this returns the file as a download :(
@app.route('/testitem') 
def index1():
    item = Item.objects().first()
    return send_file(item.photo, as_attachment=True, attachment_filename='myfile.jpeg')
