from mcmpl.request import Request
from mcmpl.requesttype import RequestType


def log(message: str):
    Request(RequestType.LOG, {"message": message}).fire()
