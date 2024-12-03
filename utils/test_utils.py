import json
import random
import re


class TestUtils:
    @staticmethod
    def load_callback_response(response):
        match = re.search(r"^\w+\((.*)\);?$", response.text)

        if match:
            json_data = match.group(1)
            return json.loads(json_data)
        else:
            raise ValueError('Unable to parse the callback response data. Check whether the callback parameter is included')


    @staticmethod
    def generate_phone_number():
        phone_no_prefix = ['4420', '4479', '5411', '9111', '9198', '9221', '2010', '9665']
        prefix = random.choice(phone_no_prefix)
        eight_digit_number = random.randint(10_000_000, 99_999_999)
        return f'{prefix}{eight_digit_number}'


    @staticmethod
    def generate_invalid_phone_number_format():
        phone_no_prefix = ['4420', '4479', '5411', '9111', '9198', '9221', '2010', '9665']
        prefix = random.choice(phone_no_prefix)
        eight_digit_number = random.randint(10_000_0, 99_999_9)
        return f'{prefix}{eight_digit_number}Ab'


    @staticmethod
    def generate_number_containing_special_char():
        phone_no_prefix = ['4420', '4479', '5411', '9111', '9198', '9221', '2010', '9665']
        prefix = random.choice(phone_no_prefix)
        eight_digit_number = random.randint(10_000_0, 99_999_9)
        special_char = TestUtils.generate_random_special_character()
        return f'{prefix}{eight_digit_number}{special_char}'


    @staticmethod
    def generate_phone_number_with_code():
        phone_number = TestUtils.generate_phone_number()
        country_code = TestUtils.get_first_two_char(phone_number)
        return {
            'country_code': country_code,
            'phone': phone_number
        }


    @staticmethod
    def get_first_two_char(input_string):
        if len(input_string) < 2:
            return input_string
        return input_string[:2]


    @staticmethod
    def generate_random_special_character():
        return random.choice(['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '[', ']', '{', '}',
                              '\\', '|', ':', ';', '"', '<', '>', '?', '/', ',', '.', '~', '`'])
