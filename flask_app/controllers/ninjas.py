from flask_app.models.ninja import Ninja
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    results= Ninja.get_all()
    return render_template('dojo1.html', results=results)

@app.route("/ninjas/all")
def allninja():
    return render_template('ninjas.html', all_dojos = Dojo.get_all())

#--- create dojos page----
@app.route("/create_ninja", methods=["POST"])
def new_ninja():

    Ninja.save(request.form)
    return redirect("/dojos")


