from server import app, login_manager, system
from flask import Flask, redirect, request, render_template, url_for
from flask_login import LoginManager,login_user, current_user, login_required, logout_user, UserMixin
from system import *


@login_manager.user_loader
def load_user(id):
    return system.get_user(id)



@app.route('/', methods=["POST", "GET"])
def login():
    errors = {}
    if current_user.is_authenticated:
        return redirect(url_for("display_menu"))
    if request.method == "POST":
        user = get_user(request.form['username'])
        if user is None:
            errors["username"] = "Username not found"
        elif user.password != request.form['password']:
            errors['password'] = "Password is wrong"
        else:
            login_user(user)
            return redirect(url_for("display_menu"))
    return render_template("login.html")


@app.route('/display_menu', methods=["POST", "GET"])
@login_required
def display_menu():
    items = system.display_menu()
    return render_template("display_menu.html", items=items)


@app.route('/check_item', methods=["POST", "GET"])
@login_required
def check_item():
    errors = {}
    if request.method == "POST":
        item_name = request.form['item']
        item = system.display_item(item_name)
        if isinstance(item, str):
            errors['item'] = item
        else:
            return render_template("check_item.html", item=item)
    return render_template("check_item.html", errors=errors)


@app.route('/logout', methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# if __name__ == '__main__':
#     app.run(debug=True)
