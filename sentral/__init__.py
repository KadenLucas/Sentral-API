import json
from urllib.parse import urlencode

from requests import Response, Session

from .meta import SentralObject
from .params import Params
from .payloads import Payload

__all__ = ["Engine", "SentralObject"]

class Engine:
    __slots__ = ["api_key", "api_url", "session", "tenant_key"]

    def __init__(
        self, sentral_rest_url: str, sentral_api_key: str, sentral_tenant_key: str
    ):
        self.api_url = sentral_rest_url
        self.api_key = sentral_api_key
        self.tenant_key = sentral_tenant_key
        self.session = Session()
        self.session.headers.update(
            {"X-API-KEY": self.api_key, "X-API-TENANT": self.tenant_key}
        )

    def query(
        self,
        endpoint: str,
        method: str,
        params: Params | dict | None = None,
        payload: Payload | dict | None = None,
    ) -> Response:
        if params:
            if isinstance(params, Params):
                params = params.__dict__
        else:
            params = None

        if payload:
            if isinstance(payload, Payload):
                payload = payload.__dict__
        else:
            payload = None

        return self.session.request(
            method=method.upper(),
            url=self.api_url + endpoint,
            data=urlencode(payload) if payload else None,
            params=params,
        )

    def query_json(
        self,
        endpoint: str,
        method: str,
        params: Params | dict | None = None,
        payload: Payload | dict | None = None,
    ) -> dict:
        response = self.query(
            endpoint=endpoint, method=method, params=params, payload=payload
        )

        if not response.ok:
            raise RuntimeError(response.text)

        return json.loads(response.text)

    def query_raw(
        self,
        endpoint: str,
        method: str,
        params: Params | dict | None = None,
        payload: Payload | dict | None = None,
    ) -> Response:
        return self.query(
            endpoint=endpoint, method=method, params=params, payload=payload
        )
