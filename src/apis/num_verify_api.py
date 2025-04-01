import requests


#
# from typing import Optional, Dict, Any
# from urllib.parse import urljoin
#
#
# import requests
# from config.projectConfiguration import logger, base_url
#
#
#
# class APIError(Exception):
#     """Custom exception for API request errors."""
#     pass
#
#
# class APIClient:
#     def __init__(self, base_client_url: Optional[str] = None, auth_token: Optional[str] = None):
#
#         self.base_url = base_url.rstrip("/") or base_client_url.rstrip("/")
#         self.auth_token = auth_token
#         self.session = requests.Session()
#         self.default_headers = {
#             'Content-Type': "application/json",
#             **({'Authorization': f"Bearer {auth_token}"} if auth_token else {})
#         }
#
#     def set_auth_token(self, auth_token: str) -> None:
#         """Dynamically updates the authentication token."""
#         self.auth_token = auth_token
#         self.default_headers["Authorization"] = f"Bearer {auth_token}"
#         if self.auth_token:
#             self.default_headers["Authorization"] = f"Bearer {self.auth_token}"
#
#     def _send_request(
#             self, method: str, endpoint: str,
#             payload: Optional[Dict[str, Any]] = None,
#             params: Optional[Dict[str, Any]] = None,
#             auth_token: Optional[str] = None,
#             extra_headers: Optional[Dict[str, str]] = None,
#     ) -> requests.Response:
#         """
#         Sends an HTTP request with support for JSON payload or query parameters.
#
#         :param method: HTTP method (GET, POST, etc.)
#         :param endpoint: API endpoint (relative to base_url).
#         :param payload: JSON payload for request body.
#         :param params: Query parameters for the request(dict).
#         :param extra_headers: Additional headers to include in the request(dict).
#         :param auth_token: Authentication token passed at runtime.
#         :return: Response object.
#         :raises APIError: If a network error occurs or the request fails.
#         """
#         headers = self.default_headers.copy()
#         if extra_headers:
#             headers.update(extra_headers)
#
#         token = auth_token or self.auth_token
#         if token:
#             headers["Authorization"] = f"Bearer {token}"
#
#         url = f"{self.base_url}/{endpoint.lstrip('/')}"
#
#         try:
#             response = self.session.request(method, url, json=payload, params=params, headers=headers)
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
#         logger.info(f"""
#         Request URL: {response.url}
#         Status Code: {response.status_code} | HTTP Method: {response.request.method}
#         Response: {response.text}
#          """)
#
#     def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
#         return self._send_request('GET', endpoint, params=params, **kwargs)
#
#     def post(self, endpoint: str, payload: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
#         return self._send_request('POST', endpoint, payload=payload, **kwargs)
#
#     def put(self, endpoint: str, payload: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
#         return self._send_request('PUT', endpoint, payload=payload, **kwargs)
#
#     def patch(self, endpoint: str, payload: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
#         return self._send_request('PATCH', endpoint, payload=payload, **kwargs)
#
#     def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
#         return self._send_request('DELETE', endpoint, params=params, **kwargs)


# static class data factory
# class OrganizationDataFactory:
# @staticmethod
# def generate_organization_data(overrides: Dict[str, Any] = None) -> Dict[str, Any]:
#     organization_data = {
#         "name": fake.company(),
#         "organizationLogo": "",
#         "website": TestUtils.generate_website(),
#         "industry": fake.company(),
#         "siteName": TestUtils.generate_site_name()
#     }
#     if overrides:
#         organization_data.update(overrides)
#     return organization_data

# usages
# payload = OrganizationDataFactory.generate_organization_data()
# payload = OrganizationDataFactory.generate_organization_data({"website": invalid_website}) #overrides the website field


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