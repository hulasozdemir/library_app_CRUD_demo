from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_sqlite_db():
    conn = sqlite3.connect('database/library.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/')
def index():
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=data)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        conn = sqlite3.connect('database/library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM books WHERE id=?", (id,))
    data = cursor.fetchone()
    conn.close()
    return render_template('update_book.html', book=data)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
