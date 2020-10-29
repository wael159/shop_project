class Config:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:159753852@localhost:5432/my_first_database"
    # It has to be called SQLALCHEMY_DATABASE_URI
    SECRET_KEY = "chocolate"