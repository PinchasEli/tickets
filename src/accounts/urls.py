from flask import request

from ..app import app
from .controllers import AccountController


@app.route("/accounts", methods=['GET', 'POST'])
def list_create_accounts():
    match request.method:
        case 'GET':
            return AccountController().list_all_accounts_controller()
        case 'POST': 
            return AccountController().create_account_controller()
        case _: 
            return 'Method is Not Allowed'


@app.route("/accounts/<account_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(account_id):
    match request.method:
        case 'GET':
            return AccountController().retrieve_account_controller(account_id)
        case 'PUT': 
            return AccountController().update_account_controller(account_id)
        case 'DELETE': 
            return AccountController().delete_account_controller(account_id)
        case _: 
            return 'Method is Not Allowed'
