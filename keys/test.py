

# import requests
# url = 'http://127.0.0.1:8000/api/keys/upload-activation-keys/'  # Replace with your API URL
# file_path = 'C:/Users/krana/Desktop/osp/backend/keys/aas.csv' # Replace with your API URL

# with open(file_path, 'rb') as file:
#     files = {'file': file}
#     response = requests.post(url, files=files)

#     if response.status_code // 100 == 2:  # Check if the response status code is in 2xx range (success)
#         try:
#             data = response.json()
#             print(data)
#         except requests.exceptions.JSONDecodeError:
#             print("Successful request, but the response is not in JSON format.")
#     else:
#         print(f"Request failed with status code: {response.status_code}, response text: {response.text}")

import requests

url = 'http://127.0.0.1:8000/api/keys/upload-csv/'  # Replace with your API URL
file_path = 'C:/Users/krana/Desktop/osp/backend/keys/oos.csv' # Replace with your API URL
# category = 'L'  # Replace with the desired category
# category="A"
# category="B"
# category="I"
# category="J"
# category="E"
# category="F"
category="K"

category=category.upper()
with open(file_path, 'rb') as file:
    files = {'file': file, 'category': (None, category)}
    response = requests.post(url, files=files)

    if response.status_code // 100 == 2:  # Check if the response status code is in 2xx range (success)
        try:
            data = response.json()
            print(data)
        except requests.exceptions.JSONDecodeError:
            print("Successful request, but the response is not in JSON format.")
    else:
        print(f"Request failed with status code: {response.status_code}, response text: {response.text}")
