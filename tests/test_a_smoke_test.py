from config.app_config import base_url, access_key
from src.apis.num_verify_api import NumVerifyAPI
from utils.custom_assertions import assert_status_code
from utils.test_utils import TestUtils
from jsonschema import validate

num_verify_api = NumVerifyAPI(base_url, access_key)

callback = 'CALLBACK_FUNCTION'

def test_validate_phone_number():
    number = TestUtils.generate_phone_number()
    response = num_verify_api.validate_phone_number(number)

    assert_status_code(response, 200)
    assert response.json()['valid'] == True
    assert response.json()['number'] is not None
    assert response.json()['international_format'] is not None
    assert response.json()['local_format'] is not None
    assert response.json()['country_prefix'] is not None
    assert response.json()['country_code'] is not None
    assert response.json()['country_name'] is not None
    assert response.json()['location'] is not None
    assert response.json()['carrier'] is not None
    assert response.json()['line_type'] is not None


def test_missing_access_key():
    number = TestUtils.generate_phone_number()

    num_verify_api = NumVerifyAPI(base_url, '')
    response = num_verify_api.validate_phone_number(number)

    assert_status_code(response, 200)
    assert response.json()['success'] == False
    assert response.json()['error']['code'] == 101
    assert response.json()['error']['type'] == 'missing_access_key'
    assert response.json()['error']['info'] == 'You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]'


def test_invalid_phone_number():
    phone_number = TestUtils.generate_phone_number()
    number = f'{phone_number}123'
    response = num_verify_api.validate_phone_number(number)

    assert_status_code(response, 200)
    assert response.json()['valid'] == False
    assert response.json()['number'] is not None
    assert response.json()['local_format'] == ''
    assert response.json()['international_format'] == ''
    assert response.json()['country_prefix'] == ''
    assert response.json()['country_code'] == ''
    assert response.json()['country_name'] == ''
    assert response.json()['location'] == ''
    assert response.json()['carrier'] == ''
    assert response.json()['line_type'] is None


def test_validate_phone_number_json_callback():
    number = TestUtils.generate_phone_number()
    response = num_verify_api.validate_phone_number(number, callback)

    assert_status_code(response, 200)
    response_data = TestUtils.load_callback_response(response)

    print(response_data)
    assert response_data['valid'] == True
    assert response_data['number'] == number
    assert response_data['international_format'] is not None
    assert response_data['local_format'] is not None
    assert response_data['country_prefix'] is not None
    assert response_data['country_code'] is not None
    assert response_data['country_name'] is not None
    assert response_data['location'] is not None
    assert response_data['carrier'] is not None
    assert response_data['line_type'] is not None


def test_validate_phone_number_json_formatting():
    phone_number = TestUtils.generate_phone_number_with_code()
    country_code = phone_number['country_code']
    number = phone_number['phone']
    response = num_verify_api.validate_phone_number(number, callback, country_code)

    assert_status_code(response, 200)
    response_data = TestUtils.load_callback_response(response)
    assert response_data['valid'] == True
    assert response_data['number'] == number
    assert response_data['international_format'] is not None
    assert response_data['local_format'] is not None
    assert response_data['country_prefix'] is not None
    assert response_data['country_code'] is not None
    assert response_data['country_name'] is not None
    assert response_data['location'] is not None
    assert response_data['carrier'] is not None
    assert response_data['line_type'] is not None


def test_list_countries():
    schema = {
        "type": "object",
        "patternProperties": {
            "^[A-Z]{2}$": {
                "type": "object",
                "properties": {
                    "country_name": {"type": "string"},
                    "dialling_code": {"type": "string"}
                },
                "required": ["country_name", "dialling_code"]
            }
        }
    }
    response = num_verify_api.list_countries()
    assert_status_code(response, 200)

    actual_response = response.json()
    validate(instance=actual_response, schema=schema)