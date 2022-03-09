from mcmpl1.request.request import Request
from mcmpl1.request.requesttype import RequestType


def log(message: str):
    Request(RequestType.LOG, {"message": message}).fire()
