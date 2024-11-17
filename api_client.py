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
    keys = read_keys_from_file("input.txt")
    if not keys:
        return

    with open('results.txt', 'w', encoding='utf-8') as f:
        for key in keys:
            logging.info(f"Making API request for key: {key}")
            response = make_api_request(key)
            
            try:
                # Убираем парсинг JSON, так как ответ - это просто текст
                if '|' in response:
                    email, password = response.strip().split('|')
                    f.write(f"{email}:{password}\n")
            except Exception as e:
                print(f"Error processing response: {e}")
                continue

            time.sleep(0.1)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )
    main()
