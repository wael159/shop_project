import flask

#import app as app # The directory where the file is currently (here is app/)
from app import app
from app import forms
from app import db
from app.models import User
from app.models import books,Orders
import flask_login
from flask import flash
from flask import request
from app import db, admin
from app.models import  MyModelView

admin.add_view(MyModelView(books, db.session))
admin.add_view(MyModelView(User, db.session))
#admin.add_view(MyModelView(Orders, db.session))


@app.route("/")
@app.route("/index.html")
@app.route("/home")
def index():
    rows = books.query.all()
    return flask.render_template("index.html", rows=rows)


@app.route("/booksLi.html")
@app.route("/list")
def show():
    from app.models import books
    rows = books.query.all()
    return flask.render_template('booksLi.html',
                            title='Overview',
                            rows=rows)

@app.route("/contact")
def contact():
    return flask.render_template('contact.html',
                            title='',
                            rows= '')

@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            user = User()
            user.name = form.username.data
            user.password = form.password.data
            user.email=form.email.data
            user.save()
            print(user)
            return flask.redirect('/')
    else:
        print("Form errors:", form.errors)

    #return flask.render_template("signup.html", form=form)
    return flask.render_template("signup.html", form=form)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        user = User.login_user(form.username.data, form.password.data)
        print(user)
        if user:
            return flask.redirect('/')
    return flask.render_template("signin.html", form=form)


@app.route("/signout")
def signout():
    flask_login.logout_user()
    return flask.redirect('/')

#searching books by name/category/id/author/year
@app.route("/search", methods=["GET", "POST"])
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
                form_test = list(books.query.filter_by(id=form.value.data).all())

            elif value=="author_name":
                form_test = list(books.query.filter_by(author_name=str(form.value.data)).all())

            elif value=="publish_year":
                form_test = list(books.query.filter_by(publish_year=str(form.value.data)).all())
            return flask.render_template("results.html", rows=form_test)

        else:
            print("Form errors:", form.errors)

    return flask.render_template("search.html", form=form)


#def add_toCard():
@app.route('/all_books')
def all_books():
    from app.models import books
    rows = books.query.all()
    return flask.render_template('all_books.html',
                            title='Overview',
                            rows=rows)

@app.route('/add_order/<int:id>',methods=["GET", "POST"])
@flask_login.login_required
def add_order(id):
    book=books.query.get(id)
    user = User.query.get(flask_login.current_user.id)
    user.new_books.append(book)
    user.save()
    #flash('the book were added successfully')
    return flask.redirect(request.referrer) #TODO we must redirect to the same page

@app.route('/delete_order/<int:id>',methods=["GET", "POST"])
@flask_login.login_required
def edit_order(id):
    #order=db.session.query(Orders).query.filter_by(order_id=id)
    #order.delete()
   # try:
    num_rows_deleted = db.session.query(Orders).filter(Orders.c.id==id).first()
    db.session.delete(num_rows_deleted)
    db.session.commit()
    print(num_rows_deleted)
    #except:
       # db.session.rollback()
    #flash('the book were deleted successfully')
    return flask.redirect(request.referrer) #TODO we must redirect to the same page



# taking the id of the current_user
@app.route('/card_items/<int:id>',methods=["GET", "POST"])
@flask_login.login_required
def UserCard_items(id):
    user = User.query.get(id)
    user_book = user.new_books
    orders = db.session.query(Orders).filter_by(user_id = id).all()
    #order_list=user_book.join(Orders,Orders.user_id==id).add_columns(user_book.id,user_book.name)
    return flask.render_template("card_items.html",rows=zip(user_book,orders) )#TODO we must redirect to the same page



