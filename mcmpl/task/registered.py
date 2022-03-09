import json
from typing import Dict, List, Callable

from mcmpl1.request.request import Request
from mcmpl1.request.requesttype import RequestType
from mcmpl1.task.task import Task
from mcmpl1.task.tasktype import TaskType

task_registered: Dict[TaskType, List[Callable[[Task], None]]] = dict()


def register_task(task_type: TaskType, task_callable: Callable[[Task], None]):
    if task_type in task_registered:
        task_registered[task_type].append(task_callable)
    else:
        task_registered[task_type] = [task_callable]
        Request(RequestType.REGISTER_TASK, {"type": task_type.value}).fire()


def listen():
    while True:
        inp = json.loads(input())
        for i in task_registered[TaskType(inp["type"])]:
            i(Task(inp["id"], TaskType(inp["type"]), inp["data"]))
