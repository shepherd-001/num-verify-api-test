import requests


# import requests
# from config.projectConfiguration import logger, base_url
#
#
# class APIError(Exception):
#     """Custom exception for API request errors."""
#     pass
#
#
# class BaseAPI:
#     def __init__(self, session=None):
#         self.base_url = base_url
#         self.session = session or requests.Session()
#         self.default_headers = {'Content-Type': "application/json"}
#
#     def _request(self, method, endpoint, payload=None, params=None, extra_headers=None):
#         """
#         Sends an HTTP request with support for JSON payload, or query parameters.
#
#         :param method: HTTP method (GET, POST, etc.)
#         :param endpoint: API endpoint (relative to base_url)
#         :param payload: JSON payload for request body
#         :param params: Query parameters (dict)
#         :param extra_headers: Additional headers (dict)
#         :return: Response object
#         :raises APIError: If request fails
#         """
#         headers = self.default_headers.copy()
#         if extra_headers:
#             headers.update(extra_headers)
#
#         url = f"{self.base_url}{endpoint}"
#
#         response = None
#         try:
#             response = self.session.request(
#                 method, url,
#                 json=payload if payload else None,
#                 params=params if params else None,
#                 headers=headers
#             )
#             response.raise_for_status()
#             return response
#         except requests.HTTPError as http_err:
#             _log_error(response, http_err)
#             raise APIError(f"HTTP error {response.status_code}: {response.text}") from http_err
#         except requests.RequestException as error:
#             logger.error(f"Request failed: {error}")
#             raise APIError("Network error occurred") from error
#
#
# class AuthenticatedAPI(BaseAPI):
#     def __init__(self, token, session=None):
#         super().__init__(session)
#         self.default_headers["Authorization"] = f"Bearer {token}"
#
#
# def _log_error(response, http_err):
#     if response is not None:
#         logger.error(f"""
#         HTTP error: {http_err}
#         Status: {response.status_code}
#         Response: {response.text}
#         """)
#     else:
#         logger.error(f"HTTP error: {http_err}")



# class AuthAPI(BaseAPI):
#     def login(self, payload):
#         return self._request('POST', '/auth', payload)


# class SecuredAPI(AuthenticatedAPI):
#     def secured(self, payload, access_token):
#         return self._request('POST', '/auth', payload, )


class NumVerifyAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def validate_phone_number(self, phone_number, callback=None, format=None):
        params = {
            'access_key': self.api_key,
            'number': phone_number,
        }

        if callback:
            params['callback'] = callback
        if format:
            params['format'] = format

        response = requests.get(f'{self.base_url}/validate', params=params)
        response.raise_for_status()
        return response


    def list_countries(self,):
        params = {
            'access_key': self.api_key,
        }
        response = requests.get(f'{self.base_url}/countries', params=params)
        response.raise_for_status()
        return response