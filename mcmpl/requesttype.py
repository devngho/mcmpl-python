from enum import Enum


class RequestType(Enum):
    LOG = "Log"
    REGISTER_TASK = "RegisterTask"
    REGISTER_EVENT = "RegisterEvent"
    MODIFY_EVENT = "ModifyEvent"
