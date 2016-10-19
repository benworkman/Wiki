from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from flask import Flask, render_template, redirect, request
import pg
import os

db = pg.DB(
    dbname=os.environ.get('PG_DBNAME'),
    host=os.environ.get('PG_HOST'),
    user=os.environ.get('PG_USERNAME'),
    passwd=os.environ.get('PG_PASSWORD')
)

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask('Wiki', template_folder=tmp_dir)



@app.route('/<page_name>')
def view_page(page_name):
    return render_template(
        'placeholder template',
        page_name=page_name
    )

@app.route('/<page_name>/edit')
def edit_page(page_name):
    return render_template(
        'edit.html',
        page_name=page_name
    )

@app.route('/<page_name>/save', methods=["POST"])
def save_page(page_name):
    content = request.form.get('content')
    db.insert('page', title=page_name, content=content)
if __name__ == ('__main__'):
    app.run(debug=True)
