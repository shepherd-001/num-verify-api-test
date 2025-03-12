import requests


#
# class APIError(Exception):
#     """Custom exception for API request errors."""
#     pass
#
#
# class BaseAPI:
#     def __init__(self, session: Optional[requests.Session] = None):
#         self.base_url = base_url
#         self.session = session or requests.Session()
#         self.default_headers = {'Content-Type': "application/json"}
#
#     def _request(
#             self, method: str, endpoint: str,
#             payload: Optional[Dict[str, Any]] = None,
#             params: Optional[Dict[str, Any]] = None,
#             extra_headers: Optional[Dict[str, str]] = None
#     ) -> requests.Response:
#         """
#         Sends an HTTP request with support for JSON payload or query parameters.
#
#         :param method: HTTP method (GET, POST, etc.)
#         :param endpoint: API endpoint (relative to base_url).
#         :param payload: JSON payload for request body.
#         :param params: Query parameters for the request(dict).
#         :param extra_headers: Additional headers to include in the request(dict).
#         :return: Response object.
#         :raises APIError: If a network error occurs or the request fails.
#         """
#         headers = self.default_headers.copy()
#         if extra_headers:
#             headers.update(extra_headers)
#
#         url = f"{self.base_url}{endpoint}"
#
#         try:
#             response = self.session.request(
#                 method, url,
#                 json=payload,
#                 params=params,
#                 headers=headers
#             )
#             self._log_response(response)
#             return response
#         except requests.RequestException as error:
#             self._log_error(error)
#             raise APIError(f"Request failed: {error}") from error
#
#     def _log_error(self, error: Exception) -> None:
#         logger.error(f"Error: {error}")
#
#     def _log_response(self, response: requests.Response) -> None:
#         logger.debug(f"""
#
#         HTTP Status Code: {response.status_code}
#         HTTP Method: {response.request.method}
#         URL: {response.url}
#         Response: {response.text}
#         """)


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