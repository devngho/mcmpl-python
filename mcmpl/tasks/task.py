from mcmpl1.task.tasktype import TaskType


class Task:
    def __init__(self, uuid: str, taskType: TaskType, data):
        self.uuid = uuid
        self.type = taskType
        self.data = data
