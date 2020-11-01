class Config:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    #SQLALCHEMY_DATABASE_URI = "postgres://postgres:159753852@localhost:5432/my_first_database"
    # It has to be called SQLALCHEMY_DATABASE_URI
    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = "chocolate"