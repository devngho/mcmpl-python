import json
from typing import Dict, List, Callable

from mcmpl.event import Event
from mcmpl.eventtype import EventType
from mcmpl.request import Request
from mcmpl.requesttype import RequestType
from mcmpl.task import Task
from mcmpl.tasktype import TaskType

task_registered: Dict[TaskType, List[Callable[[Task], None]]] = dict()
event_registered: Dict[EventType, List[Callable[[Event], None]]] = dict()


def register_task(task_type: TaskType, task_callable: Callable[[Task], None]):
    if task_type in task_registered:
        task_registered[task_type].append(task_callable)
    else:
        task_registered[task_type] = [task_callable]
        Request(RequestType.REGISTER_TASK, {"type": task_type.value}).fire()


def register_event(event_type: EventType, event_callable: Callable[[Event], None]):
    if TaskType.EVENT not in task_registered:
        register_task(TaskType.EVENT, task_event_callable)
    if event_type in event_registered:
        event_registered[event_type].append(event_callable)
    else:
        event_registered[event_type] = [event_callable]
        Request(RequestType.REGISTER_EVENT, {"type": event_type.value}).fire()


def task_event_callable(task: Task):
    for i in event_registered[EventType[task.data["type"]]]:
        event = Event(task.uuid, EventType(task.data["type"]), task.data["data"])
        i(event)
        modifiers = []
        for k, v in event.modifiers.items():
            modifiers.append({"type": k, "data": v})
        Request(RequestType.MODIFY_EVENT, {"uuid": event.uuid, "modifiers": modifiers})


def listen():
    while True:
        inp = json.loads(input())
        for i in task_registered[TaskType(inp["type"])]:
            i(Task(inp["id"], TaskType(inp["type"]), inp["data"]))
