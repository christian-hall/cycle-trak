from datetime import datetime


class Ride:
    def __init__(self, ride_id, ride_name, bike, location, date, time, duration, distance):
        self.ride_id = ride_id
        self.ride_name = ride_name
        self.bike = bike
        self.location = location
        self.date = date
        self.time = time
        self.duration = duration
        self.distance = distance
