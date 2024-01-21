from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models import History

class HistorySchema(SQLAlchemyAutoSchema):

    class Meta:
        model = History
    
