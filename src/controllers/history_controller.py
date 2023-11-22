from flask import Blueprint, jsonify
from models.history_model import HistoryModel
import json

history_controller = Blueprint("history_controller", __name__)


@history_controller.get("/")
def index():
    data = json.loads(HistoryModel.list_as_json())
    return jsonify(data), 200
