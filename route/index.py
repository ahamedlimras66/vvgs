from flask import Blueprint
from model.index import Index

index = Blueprint("index", __name__)

indexObj = Index()

index.add_url_rule("/", view_func=indexObj.indexPage, methods=['GET'])