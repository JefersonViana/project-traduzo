from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict[str, str]):
        super().__init__(data)

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }

    @classmethod
    def list_dicts(cls) -> list[dict[str, str]]:
        return [
            language.to_dict()
            for language in LanguageModel.find()
        ]
