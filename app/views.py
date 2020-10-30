
import flask

#import app as app # The directory where the file is currently (here is app/)
from app import app
from app import forms
from app import db
from app.models import User
from app.models import books
import flask_login


@app.route("/")
@app.route("/index.html")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="My awesome app", title2="Awesome app")



@app.route('/ListView')
def show():
    from app.models import books
    rows = books.query.all()
    return flask.render_template('overview.html',
                            title='Overview',
                            rows=rows)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            user = User()
            user.name = form.username.data
            user.password = form.password.data
            user.save()
            print(user)
            return flask.redirect('/')
    else:
        print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        user = User.login_user(form.username.data, form.password.data)
        print(user)
        if user:
            return flask.redirect('/')
    return flask.render_template("signin.html", form=form)


@app.route("/sign-out")
def signout():
    flask_login.logout_user()
    return flask.redirect('/')


@app.route("/search-query", methods=["GET", "POST"])
def querys():
    form = forms.searchquery()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            value = str(dict(form.searchby.choices).get(form.searchby.data))
            if value=="name":
                form_test=list(books.query.filter_by(name=str(form.value.data)).all())

            elif value=="category":
                form_test=list(books.query.filter_by(category=str(form.value.data)).all())

            elif value=="id":
                form_test = list(books.query.filter_by(id=int(form.value.data)).all())

            elif value=="author":
                form_test = list(books.query.filter_by(author_name=str(form.value.data)).all())

            elif value=="year":
                form_test = list(books.query.filter_by(year=int(form.value.data)).all())
            return flask.render_template("overview.html", rows=form_test)

        else:
            print("Form errors:", form.errors)

    return flask.render_template("search_by.html", form=form)


@app.route("/manager-page")
@flask_login.login_required
def secret():
    #return "You reached the secret page !"
    form = forms.Add_books()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            book = books()
            book.name= form.name.data
            book.price = form.price.data
            book.stock_quantity = form.stock_quantity.data
            book.category = form.category.data
            book.author_name = form.author_name.data
            book.year = form.year.data
            book.save()
            print(book)
            #return flask.redirect('/')
            return flask.render_template('indexo.html')
    else:
        print("Form errors:", form.errors)

    return flask.render_template("manager_page.html", form=form)