from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import locale


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """Show index.html"""

    return render_template("index.html")


@app.route("/application-form")
def fill_application_form():
    """Allows the user to fill out the application form."""

    job_positions = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html",
                            job_positions=job_positions)


@app.route("/application-success", methods=["POST"])
def submit_appl_form():
    """Handles submission of application-form.html"""

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    salary = locale.format("%.2f", float(request.form.get("salary")), grouping=True)
    job_title = request.form.get("job-position")

    return render_template("application-response.html",
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job_title=job_title)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
