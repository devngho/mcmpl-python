from mcmpl.requesttype import RequestType
import json


class Request:
    def __init__(self, requestType: RequestType, requestData: dict):
        self.requestType = requestType
        self.requestData = requestData

    def fire(self):
        out = {"type": self.requestType.value, "data": self.requestData}
        print(json.dumps(out))
