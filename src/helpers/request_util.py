
# src/helpers/request_util.py
import logging
import requests

from config.config import Config

class RequestUtil:
    
    @staticmethod
    def get(endpoint, headers=None):
        url = f"{Config.BASE_URL}{endpoint}"
        headers = headers or Config.get_headers()
        logging.info(f"GET Request to URL: {url} with headers: {headers}")
        response = requests.get(url, headers=headers)
        logging.info(f"Response Status Code: {response.status_code}, Response Body: {response.json()}")
        return response

    @staticmethod
    def post(endpoint, data, headers=None):
        url = f"{Config.BASE_URL}{endpoint}"
        headers = headers or Config.get_headers()
        logging.info(f"POST Request to URL: {url} with data: {data} and headers: {headers}")
        response = requests.post(url, json=data, headers=headers)
        logging.info(f"Response Status Code: {response.status_code}, Response Body: {response.text}")
        return response

    # put, delete, etc.
    