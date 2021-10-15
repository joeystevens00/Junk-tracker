import enum

from pydantic import BaseModel

class EngineStatus(enum.Enum):
    works = "works"
    fixable = "fixable"
    junk = "junk"


class Vehicle(BaseModel):
    nickname: str
    mileage: int
    wheels: int = 4
    engine_status: EngineStatus = "works"

    def mileage_rating(self):
        if self.mileage < 10_000:
            return "low"
        if self.mileage >= 10_000 and self.mileage <= 100_000:
            return "medium"
        if self.mileage > 100_000:
            return "high"

    def to_dict(self):
        d = dict(self)
        d['engine_status'] = d['engine_status'].value
        return d


class Car(Vehicle):
    doors: int = 4


class Sedan(Car):
    pass


class Coupe(Car):
    doors: int = 2


class MiniVan(Car):
    pass


class Motorcycle(Vehicle):
    wheels: int = 2
    seat_status: EngineStatus



VEHCILE_TYPE_MAP = {
    'Sedan': Sedan,
    'Coupe': Coupe,
    'Mini-Van': MiniVan,
    'Motorcycle': Motorcycle
}
