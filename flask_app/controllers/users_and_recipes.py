from flask import Flask, render_template, redirect, request, session
# from werkzeug import datastructures
from flask_bcrypt import Bcrypt

from ..models.user import User
from ..models.recipe import Recipe
# user.User
# recipe.Recipe

from flask_app import app


bcrypt = Bcrypt(app)



@app.route('/')
def index():
    if "uuid" in session:
        return redirect("/dashboard")

    return render_template("index.html")


@app.route('/login', methods = ["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect('/')
    
    user = User.get_by_email({"email": request.form['email']})

    session['uuid'] = user.id

    return redirect('/dashboard')


@app.route('/register', methods = ["POST"])
def register():
    if not User.register_validator(request.form):
        return redirect('/')

    bruh = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bruh
    }

    user_id = User.create_user(data)

    session['uuid'] = user_id

    return redirect('/dashboard')


@app.route('/dashboard')
def recipe_dashboard():
    if "uuid" not in session:
        return redirect("/")

    return render_template("users_recipes.html"
    , user = User.get_by_id
    ({'id' : session['uuid']}))


@app.route('/new_recipes')
def user_recipe():
    
    return render_template("new_recipe.html")

@app.route('/create_recipe', methods=['POST'])
def new_recipe():
    if not Recipe.validate(request.form):
        return redirect("/new_recipes")
    data = {
        "recipe_name": request.form['recipe_name'],
        "recipe_instructions": request.form['recipe_instructions'],
        "user_id" : session['uuid']
    }
    Recipe.create_recipe(data)

    return redirect("/dashboard")

@app.route('/recipes/<int:id>/delete')
def delete_recipe():
    Recipe.delete({ 'id': id })

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

