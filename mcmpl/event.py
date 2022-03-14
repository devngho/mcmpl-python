from mcmpl.requesttype import RequestType

from mcmpl.request import Request

from mcmpl.eventtype import EventType


class Event:
    def __init__(self, uuid: str, taskType: EventType, data):
        self.uuid = uuid
        self.type = taskType
        self.data = data
        self.modifiers = {}

    def modify(self, modify_type: str, data):
        self.modifiers[modify_type] = data
