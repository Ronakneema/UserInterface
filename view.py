from flask import Blueprint, flash, request, render_template
views = Blueprint(__name__,"views")

@views.route("/" , methods =["GET","POST"])
def home():
    print()
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("InscClaimAmtReimbursed")
       # getting input with name = lname in HTML form
       print(request.form)
       if first_name is not None:
         print('from 11')
         # flash('Looks like you have changed your name!')
         return render_template("index.html", scroll='result', name=first_name)
       print('from here')
       return render_template("index.html")

    return render_template("index.html")
    #  add all the outputs here
