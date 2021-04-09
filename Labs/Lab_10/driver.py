from city_processor import ISSDataRequest, CityDatabase
from producer_consumer import CityOverheadTimeQueue, ProducerThread, ConsumerThread


def main():
    request_one = ISSDataRequest()
    cities_test = CityDatabase("city_locations_test.xlsx")
    citites = CityDatabase("city_locations.xlsx")

    collections = []
    queue = CityOverheadTimeQueue()
    for city in cities_test.city_db:
        queue.put(request_one.get_overhead_pass(city))
        collections.append(request_one.get_overhead_pass(city))

    thread1 = ProducerThread(cities_test.city_db, queue)
    thread1.run()
    thread2 = ConsumerThread(queue)
    thread2.run()

#
#
# 09:41:57: Producer 2 is adding to the queue
# ISSDataRequest for Grand Prairie with params: {'lat': 55.1666, 'lon': -118.8}
# element added to queue! Queue has 10 elements
# 09:41:57: Producer 1 is adding to the queue
# ISSDataRequest for Trout River with params: {'lat': 49.4837, 'lon': -58.1166}
# element added to queue! Queue has 11 elements
# 09:41:57: Producer 3 is adding to the queueelement added to queue! Queue has 12 elements
#
# ISSDataRequest for Eastmain with params: {'lat': 52.2333, 'lon': -78.5167}
# 09:41:57: Producer 2 is adding to the queue
# ISSDataRequest for La Sarre with params: {'lat': 48.8, 'lon': -79.2}
# element added to queue! Queue has 13 elements
# 09:41:58: Producer 3 is adding to the queue
# element added to queue! Queue has 14 elements09:41:58: Producer 3 is sleeping after producing 5 items
#
# 09:41:58: Producer 2 is adding to the queueelement added to queue! Queue has 15 elements
#
# 09:41:58: Producer 2 is sleeping after producing 5 items
# 09:41:58: Producer 1 is adding to the queue
# 09:41:58: Producer 1 is sleeping after producing 5 items
# element removed from queue! Queue has 14 elements left
# 09:41:58: Consumer 1 is consuming from the queue
# ---------
# The ISS will pass over Whitehorse 5 times. The times are:
# 2021-04-07 13:04:44 for 184 seconds
# 2021-04-07 14:37:24 for 514 seconds
# 2021-04-07 16:12:40 for 585 seconds
# 2021-04-07 17:48:43 for 576 seconds
# 2021-04-07 19:25:20 for 474 seconds
# ---------
# element removed from queue! Queue has 49 elements left
# 09:42:03: Consumer 1 is consuming from the queue
# ---------
#
# *** LATER IN THE OUTPUT ***
#
# element removed from queue! Queue has 0 elements left
# 09:43:13: Consumer 1 is consuming from the queue
# ---------
# The ISS will pass over Ottawa 5 times. The times are:
# 2021-04-07 09:53:51 for 647 seconds
# 2021-04-07 11:30:44 for 647 seconds
# 2021-04-07 13:08:14 for 630 seconds
# 2021-04-07 14:45:21 for 653 seconds
# 2021-04-07 16:22:16 for 623 seconds
# ---------
# Total duration 76.42235207557678 seconds


if __name__ == '__main__':
    main()