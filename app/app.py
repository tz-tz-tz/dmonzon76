from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

db = SQLAlchemy(app)
app.config.from_object(config)
db = SQLAlchemy(app)


mysql.init_app(app)


@app.route('/')
def index():
    return render_template('Books/index.html')


@app.route('/books')
def books():
    return render_template('Books/books.html')

    sql="SELECT * FROM titles"

    #connection=mysql.connection
    #cursor=connection.cursor()
    #cursor.execute(sql)
    #titles=cursor.fetchall()
    connection.commit()
    return render_template('Books/books.html', titles=titles)


@app.route('/books/addbooks')
def addbooks():
    return render_template('Books/addbooks.html')


@app.route('/books/addbooks/save')
def addbooks_save():
    title = request.form['title']
    location = request.form['location']
    isbn = request.form['isbn']
    author = request.form['idauthor']
    editorial = request.form['ideditorial']
    
    sql="INSERT INTO titles(title, location, isbn, idauthor, ideditorial) VALUES(%s, %s, %s)" 
    data=(title, location, isbn, idauthor, ideditorial)
    connection = mysql.connection


    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    return redirect('/books')
    
    
    
if __name__=='__main__':
    app.run(debug=True)
    
    