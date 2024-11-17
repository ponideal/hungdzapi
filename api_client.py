import requests

BASE_URL = "https://api.example.com/endpoint"

def make_api_request(key):
    """Делаем запрос к API"""
    params = {'key_value': key}
    try:
        response = requests.get(BASE_URL, params=params)
        print(f"\nDEBUG Response for key {key}:")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Content: {response.text[:200]}...") # показываем первые 200 символов ответа
        return response.text
    except Exception as e:
        error_msg = f"Error for key {key}: {str(e)}"
        print(f"\nDEBUG: {error_msg}")
        return error_msg
