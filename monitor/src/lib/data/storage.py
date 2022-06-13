import os
import pickle
from typing import Optional, Any
from .classes import STATS


class Storage(dict):
    """Initialising database="""
    def __init__(self) -> None:
        self.storage = os.path.join(os.path.dirname(__file__), "storage.pkl")
        super().__init__()
        if os.path.exists(self.storage):
            with open(self.storage, "rb") as file_object:
                self.update(pickle.load(file_object))
        else:
            self.update(
                alive=True,
                stats=STATS(),
            )


data: Optional[Storage] = Storage()


def get_storage() -> Storage:
    """Getting data from storage"""
    global data
    return data


if __name__ == '__main__':
    data = Storage()
    print(data.get('stats'))
