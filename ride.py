from datetime import datetime


class Ride:
    def __init__(self, ride_id, ride_name, bike, location, datetime, duration, distance):
        self.ride_id = ride_id
        self.ride_name = ride_name
        self.bike = bike
        self.location = location
        self.datetime = datetime
        self.duration = duration
        self.distance = distance
