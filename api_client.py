import requests
import json
import csv
import logging
import os
import time

BASE_URL = "http://sv5.api999.com/google/api.php"


def make_api_request(key):
    """Делаем запрос к API"""
    params = {"key_value": key}
    try:
        response = requests.get(BASE_URL, params=params)
        print(f"\nDEBUG Response for key {key}:")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Content: {response.text}")  # Show full response content
        return response.text
    except Exception as e:
        error_msg = f"Error for key {key}: {str(e)}"
        print(f"\nDEBUG: {error_msg}")
        return error_msg


def read_keys_from_file(filename):
    """Читаем ключи из файла"""
    try:
        with open(filename, "r") as f:
            keys = []
            for line in f:
                line = line.strip()
                if line and "Key:" in line:
                    key = line.split("Key:")[1].strip()
                    keys.append(key)
        logging.info(f"Read {len(keys)} keys from {filename}")
        return keys
    except Exception as e:
        logging.error(f"Error reading keys from file: {str(e)}")
        return []


def main():
    # Читаем ключи из файла
    keys = read_keys_from_file("input.txt")
    if not keys:
        return

    # Делаем запросы и собираем результаты
    results = {}
    for key in keys:
        logging.info(f"Making API request for key: {key}")
        result = make_api_request(key)
        results[key] = result

        # Добавляем небольшую задержку между запросами
        time.sleep(0.1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )
    main()
