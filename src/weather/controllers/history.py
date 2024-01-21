import pydash as _ 

from flask import request, jsonify

from ... import db

from ..models import History
from ..schemas import HistorySchema


class HistoryController:

    def get_list(self, current_account):
        try:
            history_list = History.query.filter_by(account_id=current_account.id)
            history_schema = HistorySchema(many=True)
            data_response = history_schema.dump(history_list)

            return jsonify(data_response)
        except Exception as e:
            return jsonify({'error': f'History List wrong: {e}'}), 400
