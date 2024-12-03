from locust import HttpUser, task, between
from apis.num_verify_api import NumVerifyAPI
from config.app_config import base_url, access_key
from utils.custom_assertions import assert_status_code
from utils.test_utils import TestUtils


class PerformanceTest(HttpUser):
    wait_time = between(1, 2)
    host = base_url
    def on_start(self):
        self.api = NumVerifyAPI(base_url, access_key)
        self.phoneNumber = TestUtils.generate_phone_number()

    @task
    def test_validate_phone_number_endpoint(self):
        phone_number = self.phoneNumber
        response = self.api.validate_phone_number(phone_number)
        assert_status_code(response, 200)
        assert response.elapsed.total_seconds() < 1.0, "Response time exceeded threshold of 1.0s"
        # print(f'\nElapsed time of performance test: {response.elapsed.total_seconds()}\n')
