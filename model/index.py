from flask import render_template

class Index:
    def indexPage(self):
        return render_template("index.html")