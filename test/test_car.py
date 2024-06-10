import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class BaseTestCar(unittest.TestCase):
    car_class = None
    battery_service_years = 0
    engine_service_mileage = 0
    has_warning_light = False

    def create_car_with_battery_service(self, years):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - years)
        if self.has_warning_light:
            return self.car_class(last_service_date, False)
        return self.car_class(last_service_date, 0, 0)

    def create_car_with_mileage(self, mileage, warning_light=False):
        last_service_date = datetime.today().date()
        if self.has_warning_light:
            return self.car_class(last_service_date, warning_light)
        return self.car_class(last_service_date, mileage, 0)

    def battery_should_be_serviced(self):
        car = self.create_car_with_battery_service(self.battery_service_years)
        self.assertTrue(car.needs_service())

    def battery_should_not_be_serviced(self):
        car = self.create_car_with_battery_service(self.battery_service_years - 2)
        self.assertFalse(car.needs_service())

    def engine_should_be_serviced(self):
        car = self.create_car_with_mileage(self.engine_service_mileage + 1, True)
        self.assertTrue(car.needs_service())

    def engine_should_not_be_serviced(self):
        car = self.create_car_with_mileage(self.engine_service_mileage, False)
        self.assertFalse(car.needs_service())

class TestCalliope(BaseTestCar):
    car_class = Calliope
    battery_service_years = 3
    engine_service_mileage = 30000

class TestGlissade(BaseTestCar):
    car_class = Glissade
    battery_service_years = 3
    engine_service_mileage = 60000

class TestPalindrome(BaseTestCar):
    car_class = Palindrome
    battery_service_years = 5
    engine_service_mileage = 0
    has_warning_light = True

class TestRorschach(BaseTestCar):
    car_class = Rorschach
    battery_service_years = 5
    engine_service_mileage = 60000

class TestThovex(BaseTestCar):
    car_class = Thovex
    battery_service_years = 5
    engine_service_mileage = 30000

if __name__ == '__main__':
    unittest.main()