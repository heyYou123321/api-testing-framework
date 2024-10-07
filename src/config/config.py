
# src/config/config.py

class Config:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    API_KEY = "your_api_key_here"

    @staticmethod
    def get_headers():
        return {
            "Authorization": f"Bearer {Config.API_KEY}",
            "Content-Type": "application/json",
        }

