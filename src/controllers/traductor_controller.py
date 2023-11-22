from flask import Blueprint, render_template, request
from models.language_model import LanguageModel, TranslationModel

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


@traductor_controller.post("/")
def translate():
    text_to_translate = request.form['text-to-translate']
    translate_from = request.form['translate-from']
    translate_to = request.form['translate-to']
    translated = TranslationModel.translate(
        text_to_translate,
        translate_to
    )
    data = {
        'languages': LanguageModel.list_dicts(),
        'text_to_translate': text_to_translate,
        'translate_from': translate_from,
        'translate_to': translate_to,
        'translated': translated
    }
    return render_template("index.html", **data)
