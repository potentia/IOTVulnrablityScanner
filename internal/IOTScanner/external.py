
from asyncio.windows_events import NULL
from logging import NullHandler


def testing():
    vulrnableDevices = [["Device Name", "Finger Print"] ,["Device Name","Finger Print"]]
    nullList =  [["Device Name", "Finger Print"] ,["Device Name","Finger Print"]]
    if len(nullList)==0:
        print("empty")
    else:
        print("Not empty")
    return vulrnableDevices

testing()