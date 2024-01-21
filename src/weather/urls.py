from flask import request

from ..app import app

from ..decorators import token_required

from .controllers import WeatherController, HistoryController


@app.route("/weather", methods=['GET', 'POST'])
@token_required
def weather_search(current_account):
    match request.method:
        case 'GET':
            return WeatherController().get_weather_info(current_account)
        case _:
            return 'Method is Not Allowed'


@app.route("/history", methods=['GET'])
@token_required
def history(current_account):
    history_controller = HistoryController()
    match request.method:
        case 'GET':
            return history_controller.get_list(current_account)
        case _:
            return 'Method is Not Allowed'
