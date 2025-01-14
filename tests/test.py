import requests
import os

CONTAINER_IP=os.getenv('CONTAINER_IP', '127.0.0.1')
print(f'CONTAINER_IP={CONTAINER_IP}')

def test_config():
    # Define the URL 
    url = f'http://{CONTAINER_IP}:80/config'

    # Perform the GET request
    response = requests.get(url,)

    # Print the response status code
    print("Response Status Code:", response.status_code)

    # Print the response headers
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Print the response payload (body)
    print("Response Payload:")
    print(response.text)

    assert response.status_code == 200


def test_object_detection():
    # Define the URL and the image file path
    url = f'http://{CONTAINER_IP}:80/'
    image_file_path = './tests/image1.jpg'

    # Create a dictionary with the file data
    files = {'image_file': open(image_file_path, 'rb')}

    #  Perform the POST request
    response = requests.post(url, files=files)

    # Print the response status code
    print("Response Status Code:", response.status_code)

    # Print the response headers
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Print the response payload (body)
    print("Response Payload:")
    print(response.text)

    assert response.status_code == 200

