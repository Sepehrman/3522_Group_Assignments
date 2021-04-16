import logging
import time
import city_processor
import threading


class CityOverHeadTimeQueue:

    def __init__(self):
        """
        CityOverHeadTimeQueue initializer.
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Add an object of type CityOverheadTimes to the queue.

        :param overhead_time: an object of type CityOverheadTimes
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        Gets the first element of the queue and deletes it.

        :return: an object of type CityOverheadTimes
        """
        with self.access_queue_lock:
            city_overhead_time = self.data_queue[0]
            del self.data_queue[0]
            return city_overhead_time

    def __len__(self) -> int:
        """
        Return the length of the data_queue.

        :return: length of the que
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    """
    Class representation of the Producer Thread which inherits from the Threading class.
    """

    def __init__(self, cities: list, queue: CityOverHeadTimeQueue):
        """
        Producer Thread initializer.

        :param cities: list
        :param queue: an object of CityOverHeadTimeQueue
        """
        super().__init__()
        self.list_of_cities = cities
        self.city_overhead_queue = queue

    def run(self) -> None:
        """
        Runs the Producer Thread.
        """
        city_counter = 0
        for city in self.list_of_cities:
            city_overhead_times = city_processor.ISSDataRequest.get_overhead_pass(city)
            self.city_overhead_queue.put(city_overhead_times)
            print(f"ISSDataRequest for {city.city_name}(lat: {city.lat}, lng: {city.lng})"
                  f" added to queue! \nQueue: {len(self.city_overhead_queue)} request(s).")
            city_counter += 1
            if city_counter % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    Consumer Thread (inherited from the Threading class).
    """

    def __init__(self, queue: CityOverHeadTimeQueue):
        """
        Consumer Thread class initializer.

        :param queue: an object of City Over Heat Time Queue.
        """
        super().__init__()
        self.city_overhead_queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """
        Method runs the Consumer Thread.
        """
        while self.data_incoming or len(self.city_overhead_queue) > 0:
            city_overhead_times = self.city_overhead_queue.get()
            print("\n", city_overhead_times)
            time.sleep(0.5)
            if not self.city_overhead_queue:
                time.sleep(0.75)


def main():
    """
    Drives the program.

    :return: none
    """
    formatter = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatter, level=logging.INFO,
                        datefmt="%H:%M:%S")

    city_database = city_processor.CityDatabase("city_locations_test.xlsx")
    city_overhead_time_queue = CityOverHeadTimeQueue()
    consumer_thread = ConsumerThread(city_overhead_time_queue)
    producer_thread = ProducerThread(city_database.city_db, city_overhead_time_queue)
    producer_thread.run()
    consumer_thread.data_incoming = False
    consumer_thread.run()


if __name__ == '__main__':
    main()
