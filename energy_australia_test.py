# This is a Python script.
import requests
from jsonschema import validate

# API URL
BASE_URL = 'https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals'

# Declare json schema
SCHEMA = {
    "name": "string",
    "bands": [
        {
            "name": "string",
            "recordLabel": "string"
        }
    ]
}


def test_status_code(p_response):
    assert p_response.status_code == 200


def test_check_content_type(p_response):
    assert p_response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_request_url():
    """ Function to test url and process response output"""
    response = requests.get(BASE_URL)

    # Test response status code
    test_status_code(response)

    # Test response Content Type
    test_check_content_type(response)

    print("Printing Response Header information")
    for header_type, header_value in response.headers.items():
        print(f'Header: {header_type}')
        print(f'Value: {header_value}')
    print('###########################')

    # Get API response
    response_data = response.json()

    # Validate will raise an exception if response json is not what is described in schema above.
    validate(instance=response_data, schema=SCHEMA)

    # Iterate over response data and display values
    for fest in response_data:
        print(f"Festival Name: {fest.get('name', 'No Festival')}")
        for band in fest.get('bands'):
            print(f"Band Name: {band.get('name')}")
            print(f"Record Label Name: {band.get('recordLabel')}")
        print('###########################')


def main():
    """' Start execution"""

    # Request URL
    test_request_url()


if __name__ == '__main__':
    main()
