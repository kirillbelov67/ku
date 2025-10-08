from flask import Flask 
from flask import render_template,request
import sqlite3

app = Flask(__name__)

app = Flask(__name__, template_folder='templates')
 
#создаум подключение к базе данных ( файл называется "my_database.db")
connection = sqlite3.connect('my_database.db',check_same_thread=False)
cursor = connection.cursor()

# Функция для получения товаров определённой категории 
def product_menclothingDB(category): 
    cursor.execute("SELECT * FROM product WHERE category=?", (category,)) 
    return cursor.fetchall() 
 
# Функция для главной (главная + новинки/тишки/худи по имени) 
def productDB_main(): 
    cursor.execute(""" 
        SELECT * FROM product 
        WHERE category='главная' 
           OR name LIKE '%кроссовки%' 
           OR name LIKE '%футболка%' 
    """) 
    return cursor.fetchall() 

def product_oneDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id+'"')
    return listDB.fetchall()

def product_oneDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

@app.route('/')
def index():
    shop = productDB_main()
    return render_template("index.html", shop=shop)


@app.route('/cat/<id>')
def menclothing(id):
    shop = product_menclothingDB(id)
    product_menclothingDB
    return render_template("menclothing.html",shop=shop)
    
@app.route('/proba')
def proba():
     return render_template("proba.html")

@app.route('/womenclothing') #женская одежда
def womenclothing(id):
    shop = product_womenclothingDB(id)
    product_womenclothingDB
    return render_template("womenclothing.html",shop=shop)

@app.route('/basket/<id>') #корзина
def basket(id):
    shop = product_oneDB(id)
    print(shop)
    return render_template("basket.html", shop=shop)


@app.route('/childrenclothing') #детская одежда
def childrenclothing(id):
    shop = product_childrenclothingDB(id)
    product_childrenclothingDB
    return render_template("childrenclothing.html", shop=shop)


@app.route('/user/<username>')
def user_profile(username):
    return render_template("user_profil.html")


if __name__ == '__main__':  #точка входа нашей программы
    print("сервер запущен") #проверка точки входа
    app.run(debug=True)