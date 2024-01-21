from flask import request, jsonify
import uuid

from ... import db
from ..models import Account


class AccountController:

    def list_all_accounts_controller(self):
        try:
            accounts = Account.query.all()
            response = []
            for account in accounts:
                response.append(account.toDict())

            return jsonify(response)
        except Exception as e:
                return jsonify({'error': f'List all accounts wrong: {e}'}), 400

    def create_account_controller(self):
        try:
            request_form = request.form.to_dict()

            id = str(uuid.uuid4())
            new_account = Account(
                                id             = id,
                                email          = request_form['email'],
                                username       = request_form['username'],
                                dob            = request_form['dob'],
                                country        = request_form['country'],
                                phone_number   = request_form['phone_number'],
                                )
            db.session.add(new_account)
            db.session.commit()

            response = Account.query.get(id).toDict()
            return jsonify(response)
        except Exception as e:
            return jsonify({'error': f'Create account wrong: {e}'}), 400

    def retrieve_account_controller(self, account_id):
        try:
            response = Account.query.get(account_id).toDict()
            return jsonify(response)
        except Exception as e:
            return jsonify({'error': 'Account id wrong'}), 400

    def update_account_controller(self, account_id):
        try:
            data_update = request.json  # get the data body from req
            count = Account.query.filter_by(id=account_id).update(data_update)
            db.session.commit()

            response = Account.query.get(account_id).toDict()
            return jsonify(response)
        except Exception as e:
            return jsonify({'error': f'Update account wrong: {e}'}), 400

    def delete_account_controller(self, account_id):
        try:
            Account.query.filter_by(id=account_id).delete()
            db.session.commit()

            return ('Account with Id "{}" deleted successfully!').format(account_id)
        except Exception as e:
            return jsonify({'error': f'Delete account wrong: {e}'}), 400
