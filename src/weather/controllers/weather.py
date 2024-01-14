import uuid
import requests

import pydash as _ 

from flask import request, jsonify

from ... import db

from ...services import Weatherstack
from ..models import History


class WeatherController:

    def get_weather_info(self):
        try:
            city = request.args.get('city')
            if not city:
                raise('City parameter is required')
                # return jsonify({'error': 'City parameter is required'}), 400

            weather_data = Weatherstack().get_weather(city)
            if not weather_data:
                raise('Error search by city')
            if not _.get(weather_data, 'success', True):
                raise(_.get(weather_data, 'error.info', 'Not found'))

            new_history = History(
                title=city,
                details=weather_data,
            )
            db.session.add(new_history)
            db.session.commit()
            return jsonify(weather_data)
        except Exception as e:
            return jsonify({'error': f'Update account wrong: {e}'}), 400
