# MCMPL-Python
MCMPL-Python은 [MC-MPL](https://github.com/devngho/mcmpl) 의 플러그인을 Python으로 만들 수 있게 하는 모듈입니다.
## Hello, World!
파이썬이 설치되어 있는 상태를 기준으로 합니다.
```commandline
pip install git+https://github.com/devngho/mcmpl-python.git
```
example.py
```python
from mcmpl.task import registered
from mcmpl.task.task import Task
from mcmpl.tasktype import TaskType
from mcmpl.request import requestadapter


def on_enable(task: Task):
    requestadapter.log("Hello, World!")


registered.register_task(TaskType.ON_ENABLE, on_enable)
registered.listen()
```
example.cmd(Windows) or example.sh(Linux)
```commandline
python example.py
```
또는 pyinstaller 등을 이용해 exe 파일로 빌드하세요.
결과물은 MCMPL 플러그인이 설치된 서버의 /plugins/mcmpl/ 폴더에 넣으세요.
