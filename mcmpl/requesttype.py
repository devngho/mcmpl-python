from enum import Enum


class RequestType(Enum):
    LOG = "Log"
    REGISTER_TASK = "RegisterTask"
    MODIFY_EVENT = "ModifyEvent"
