from mcmpl.requests.request import Request
from mcmpl.requests.requesttype import RequestType


def log(message: str):
    Request(RequestType.LOG, {"message": message}).fire()
