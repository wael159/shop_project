
import flask

#import app as app # The directory where the file is currently (here is app/)
from app import app
from app.models import products

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