from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app import app


# @app.route("/")
@app.route("/dojos")
def dojo():
   
    results = Dojo.get_all()
    return render_template('dojos.html', results=results)

# @app.route("/dojos/all")
# def alldojo():
#     return render_template('dojos.html', dojos = Dojo.get_all())


#--- create dojos page----
@app.route("/dojo_create", methods=["POST"])
def old_ninja():


  Dojo.save(request.form)
  return redirect("/dojos")


#--- display dojo1 page----

@app.route('/ninjas/<int:id>')
def display_ninjas(id):
    data = {
      "id":id
    }
    ninjas = Dojo.onedojo(data)
    return render_template("dojo1.html", ninjas=ninjas)
