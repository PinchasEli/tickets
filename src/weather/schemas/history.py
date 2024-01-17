from marshmallow import Schema, fields, SQLAlchemySchema

from ..models import History

class HistorySchema(SQLAlchemySchema):
    class Meta:
        model = History
