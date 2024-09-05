from requests import get, post, put, delete
from typing import Union, List, Dict
from utils import config
from .diff import colorDiff, diff
from json import dumps

def resolveResponse(response, responseCode, expectedReturn):
    if responseCode is not None and response.status_code != responseCode:
        raise Exception(f"Wrong return code.\nExpected: {responseCode}\nGot: {response.status_code}\nResponse: {response.content.decode('unicode_escape')}")
    if isinstance(expectedReturn, (str, list, dict)):
        if isinstance(expectedReturn, str):
            text = response.content.decode('unicode_escape')
            differ = colorDiff(expectedReturn, text, False)
            if differ != "":
                raise Exception(f"Wrong returned text.\ndiff:\n{differ}")
            return text
        elif isinstance(expectedReturn, (list, dict)):
            res = response.json()
            differ = diff(expectedReturn, res)
            if differ != {} and differ != []:
                raise Exception(f"Wrong returned json.\ndiff:\n{dumps(differ, ensure_ascii=False, indent=4)}")
            return res
    return response.content.decode('unicode_escape')


class RequestExpect:
    def get(self, url: str, responseCode: Union[int, None] = None, headers: Union[Dict] = [],
            expectedReturn: Union[str, List, Dict, None] = None):
        response = get(f"http://{config.server.host}:{config.server.port}{url}", headers=headers)
        return resolveResponse(response, responseCode, expectedReturn)

    def put(self, url: str, jsonPayload: dict, responseCode: Union[int, None] = None, headers: Union[Dict] = [],
            expectedReturn: Union[str, List, Dict, None] = None):
        response = put(f"http://{config.server.host}:{config.server.port}{url}", headers=headers, json=jsonPayload)
        return resolveResponse(response, responseCode, expectedReturn)

    def post(self, url: str, jsonPayload: dict, responseCode: Union[int, None] = None, headers: Union[Dict] = [],
            expectedReturn: Union[str, List, Dict, None] = None):
        response = post(f"http://{config.server.host}:{config.server.port}{url}", headers=headers, json=jsonPayload)
        return resolveResponse(response, responseCode, expectedReturn)
    def delete(self, url: str, responseCode: Union[int, None] = None, headers: Union[Dict] = [],
            expectedReturn: Union[str, List, Dict, None] = None):
        response = delete(f"http://{config.server.host}:{config.server.port}{url}", headers=headers)
        return resolveResponse(response, responseCode, expectedReturn)

requestExpect = RequestExpect()
