class User:
    def __init__(self, user_id, user_name, password, birthdate, sex, weight, height, total_mileage=0):
        """presently there is only one user but with the potential for multiple"""
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.birthdate = birthdate
        self.sex = sex
        self.weight = weight
        self.height = height
        self.total_mileage = total_mileage

    def update_total_mileage(self):
        pass
