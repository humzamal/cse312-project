from flask import Flask
from pymongo import MongoClient

# Database
my_client = MongoClient("mongodb://localhost:27017/")
my_database = my_client["WebAppDatabase"]
# this collection contains user accounts, and profile pictures names.
user_accounts = my_database["UserAccounts"]

app = Flask(__name__)


@app.route('/')
def homepage():
    with open('index.html', 'r') as index:
        index_html = index.read()
        index.close()
    return index_html


if __name__ == '__main__':
    app.run(debug=True)