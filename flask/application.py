from flask import Flask, render_template, session, request, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "msschermerhornc"

@app.route("/")
def index_page():
    """Show an index page."""
    #redirect user to application-form
    return redirect("/application-form")


@app.route("/application-form")
def application_form():
    """Show application form page"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
    """Render /application page using user input from form"""

    first_name = request.form["firstname"].title()
    last_name = request.form["lastname"].title()

    #If user enters a decimal, strip everything to right
    salary = int(request.form["salary"].split('.')[0])
    job_type = request.form["jobtype"]


    return render_template("application-response.html", first_name=first_name, 
                           last_name=last_name, salary=salary, job_type=job_type)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # This stops debugger from pausing when there is a redirect.
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

