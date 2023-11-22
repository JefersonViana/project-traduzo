from flask import Blueprint, render_template
from models.language_model import LanguageModel

traductor_controller = Blueprint("traductor_controller", __name__)


@traductor_controller.get("/")
def index():
    data = {
        'languages': LanguageModel.list_dicts(),
        'text_to_translate': "O que deseja traduzir?",
        'translate_from': "pt",
        'translate_to': "en",
        'translated': "What do you want to translate?"
    }
    return render_template("index.html", **data)
