from flask import Flask, url_for

from route.index import index
from route.about import about
from route.contact import contact


app = Flask(__name__)

app.register_blueprint(index, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True)