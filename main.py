from flask import Flask
from modules import page_index

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return page_index.view()


@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    return f'Post {id}'
