from flask import request, jsonify
import uuid

from ... import db
from ..models import Account


# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522

class AccountController:

    def list_all_accounts_controller(self):
        accounts = Account.query.all()
        response = []
        for account in accounts:
            response.append(account.toDict())

        return jsonify(response)

    def create_account_controller(self):
        request_form = request.form.to_dict()

        id = str(uuid.uuid4())
        print(request_form)
        print(id)
        new_account = Account(
                            id             = id,
                            email          = request_form['email'],
                            username       = request_form['username'],
                            dob            = request_form['dob'],
                            country        = request_form['country'],
                            phone_number   = request_form['phone_number'],
                            )
        print(new_account.email)
        db.session.add(new_account)
        db.session.commit()
        print('created')

        response = Account.query.get(id).toDict()
        return jsonify(response)

    def retrieve_account_controller(self, account_id):
        response = Account.query.get(account_id).toDict()
        return jsonify(response)

    def update_account_controller(self, account_id):
        data_update = request.json  # get the data body from req
        count = Account.query.filter_by(id=account_id).update(data_update)
        print(count)
        db.session.commit()

        response = Account.query.get(account_id).toDict()
        return jsonify(response)

    def delete_account_controller(self, account_id):
        Account.query.filter_by(id=account_id).delete()
        db.session.commit()

        return ('Account with Id "{}" deleted successfully!').format(account_id)
