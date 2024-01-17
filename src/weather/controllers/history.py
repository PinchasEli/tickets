import pydash as _ 

from flask import request, jsonify

from ... import db

from ..models import History


class HistoryController:

    def get_list(self):
        try:
            history_list = History.query.all()
   
            # Serialize the query result using marshmallow schema
            user_schema = UserSchema(many=True)
            data_response = user_schema.dump(history_list)
            # response = []
            # for account in history_list:
            #     response.append(account.toDict())

            return jsonify(history_list)
        except Exception as e:
            return jsonify({'error': f'History List wrong: {e}'}), 400
