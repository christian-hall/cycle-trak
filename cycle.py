class Cycle:
    """For keeping track of mileage put on bikes"""
    def __init__(self, bike_id, name, bike_type, year, make, model, date_bought, date_retired, odometer=0):
        self.bike_id = bike_id
        self.name = name
        self.bike_type = bike_type
        self.year = year
        self.make = make
        self.model = model
        self.date_bought = date_bought
        self.date_retired = date_retired
        self.odometer = odometer

    def update_odometer(self):
        """Update the total mileage on a particular bike"""
        pass
