from flask import Flask, render_template, g
import sqlite3
import database

app = Flask(__name__)

app.config['DATABASE'] = "static/bd/coffee.db"
app.secret_key = "abc748596"

nav_menu = [
    {"link": "/index", "name": "Главная"},   
    {"link": "/info", "name": "О нас"},
    {"link": "/blog", "name": "Блог"},
    {"link": "/shop", "name": "Магазин"},
    {"link": "/contacts", "name": "Контакты"}
]

def connect_db():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect

def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", menu=nav_menu)

@app.route("/info")
def info():
    return render_template("info.html", menu=nav_menu)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", menu=nav_menu)

@app.route("/blog")
def blog():
    return render_template("blog.html", menu=nav_menu)

@app.route("/shop")
def shop():
    connect = get_connect()
    base = database.ProductDB(connect)
    return render_template("shop.html", menu=nav_menu, cards=base.get_all_products())


@app.route("/shop/<int:value>")
def prod(value):
    connect = get_connect()
    base = database.ProductDB(connect)
    product = base.get_product(value)
    return render_template("product.html", img=product["img"], price=product["price"], 
                           desc=product["description"], name=product["name"],  menu=nav_menu)


@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run()
