# from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
from src.database.db import db
import json


def test_history_delete(app_test):
    db.get_collection("history").drop()
    app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    app_test.post(
        "/",
        data={
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    history = app_test.get("/history/")
    data = json.loads(history.get_data(as_text=True))

    assert history.status_code == 200
    assert len(data) == 2
    id_to_delete = data[0]["_id"]

    UserModel(
        {"name": "Peter", "token": "token_secreto123", "level": "admin"}
    ).save()

    response = app_test.delete(f"/admin/history/{id_to_delete}", headers={
        "Authorization": "token_secreto123",
        "User": "Peter"
    })

    assert response.status_code == 204
    data_finish = json.loads(app_test.get("/history/").get_data(as_text=True))
    assert len(data_finish) == 1
