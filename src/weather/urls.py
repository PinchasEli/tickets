from flask import request

from ..app import app
from .controllers import WeatherController


@app.route("/weather", methods=['GET', 'POST'])
def weather_search():
    match request.method:
        case 'GET':
            return WeatherController().get_weather_info()
        # case 'POST': 
        #     return AccountController().create_account_controller()
        case _: 
            return 'Method is Not Allowed'
