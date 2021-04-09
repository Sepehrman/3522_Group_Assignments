import copy
import logging
import threading
from time import sleep

from city_processor import CityOverheadTimes
from threading import Thread


class CityOverheadTimeQueue:

    def __init__(self):
        self._data_queue = []
        self.access_queue_lock = threading.Lock()
        self._deleted_obj = None

    def put(self, overhead_time: CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self._data_queue.append(overhead_time)

    def get(self):
        with self.access_queue_lock:
            if len(self._data_queue) > 0:
                obj = copy.deepcopy(self._data_queue[0])
                # self._deleted_obj =
                del self._data_queue[0]
                return obj

    def __len__(self):
        return len(self._data_queue)


class ProducerThread(Thread):
    FIVE_SECONDS = 5

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._city_objects = cities
        self._queue = queue

    def run(self):
        for city in self._city_objects:
            print(f"ProducerThread for {city}")
            if len(self._queue) % self.FIVE_SECONDS == 0:
                sleep(5)
            self._queue.put(city)


class ConsumerThread(Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self.data_incoming = True

    def run(self) -> None:
        while self.data_incoming or len(self._queue) > 0:
            print(f"ConsumerThread - {self._queue.get()}")
            sleep(0.5)
        sleep(0.75)
