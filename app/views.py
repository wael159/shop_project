
import flask

#import app as app # The directory where the file is currently (here is app/)
from app import app
from app.models import products
from app import forms
from app import db
from app.models import all_products
from app.models import User
import flask_login


#filter function
def filter_id(value):
    value_list=[]
    [value_list.append(item['id'])for item in products]
    if (value in value_list):
        return True
    else:
        return False


@app.route("/")
@app.route("/index.html")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="My awesome app", title2="Awesome app")


@app.route("/product/<int:productId>")
def filtered_products(productId):
    filtered_productId = filter(filter_id, [productId])
    id_list=[]
    product_list=[]
    for item in filtered_productId:
        id_list.append(item)
    for product in products:
        if product['id'] in id_list:
            product_list.append(product)
    return flask.render_template("product_list.html", products=product_list)


@app.route("/search/by-category/<value>")
def search_by(value):
        category_product=[]
        for item in products:
            if item['category'] == value:
                category_product.append(item)
        if len(category_product)==0:
            return("there is no item with these category")
        else:
            return flask.render_template("product_list.html", products=category_product)


@app.route("/product_list")
def product_list():
    return flask.render_template("product_list.html", products=products)



@app.route('/ListView')
def show():
    from app.models import all_products
    rows = all_products.query.all()
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
                form_test=list(all_products.query.filter_by(name=str(form.value.data)).all())

            elif value=="category":
                form_test=list(all_products.query.filter_by(category=str(form.value.data)).all())

            elif value=="id":
                form_test = list(all_products.query.filter_by(id=int(form.value.data)).all())

            return flask.render_template("overview.html", rows=form_test)


        else:
            print("Form errors:", form.errors)

    return flask.render_template("search_by.html", form=form)


@app.route("/secret-page")
@flask_login.login_required
def secret():
    return "You reached the secret page !"

