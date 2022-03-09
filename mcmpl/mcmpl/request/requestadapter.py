from mcmpl.request.request import Request
from mcmpl.request.requesttype import RequestType


def log(message: str):
    Request(RequestType.LOG, {"message": message}).fire()
