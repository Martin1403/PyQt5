import asyncio
import psutil
import time
import re
from subprocess import check_output

from .storage import get_storage

data: dict = get_storage()
error = True


def exception(function):
    g, loc = {}, {}
    try:
        exec(f'x = {function}', g, loc)
        return loc.get('x')
    except:
        return None


async def worker(label):
    global data, error
    if label == "CPU" and data.get('alive'):
        temp = psutil.sensors_temperatures().get('coretemp')
        data.get('stats').get('cpu').update(
            percent=exception(int(psutil.cpu_percent(interval=1, percpu=False))),
            cores=exception(psutil.cpu_count(logical=True)),
            temp=exception(temp.pop(0).current if temp else None),
        )
    elif label == "MEMO" and data.get('alive'):
        memo = psutil.virtual_memory()
        temp = psutil.sensors_temperatures().get('acpitz')
        data.get('stats').get('memo').update(
            total=exception(round(memo.total / 1000000000, 1)),
            free=exception(round(memo.available / 1000000000, 1)),
            percent=exception(int(memo.percent)),
            temp=exception(temp.pop().current if temp else None)
        )
        time.sleep(1)
    elif label == "GPU" and error and data.get('alive'):
        try:
            stdout = re.sub(r'\s', '', check_output('nvidia-smi', shell=True, encoding='UTF-8'))
            pattern1 = r'(\d+)MiB/(\d+)MiB'
            used, total = [int(i) for i in re.findall(re.compile(pattern1), stdout).pop()]
            data.get('stats').get('gpu').update(
                percent=int(100 / total * used),
                free=round((total - used) / 1000, 1),
                total=round(total / 1000, 1),
            )
        except:
            error = False
        time.sleep(1)


async def do_something():
    # Run three calls to worker concurrently and collect results
    for async_func in asyncio.as_completed((
            worker('CPU'), worker('MEMO'), worker('GPU')
    )):
        await async_func
        if not data.get('alive'):
            break


def start_monitor():
    global data
    if data.get('alive'):
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(do_something())
        except:
            loop.stop()
            loop.close()
