import requests


class Weatherstack:
        
    __WEATHERSTACK_API_KEY = 'c19e42a869fd2a9b205c4e291cc80b5b'
    __WEATHERSTACK_API_BASE_URL = 'http://api.weatherstack.com/current'

    def get_weather(self, city):
        params = {
            'access_key': self.__WEATHERSTACK_API_KEY,
            'query': city
        }

        response = requests.get(self.__WEATHERSTACK_API_BASE_URL, params=params)
        data = response.json()

        return data
