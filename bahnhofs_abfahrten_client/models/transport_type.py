from enum import Enum


class TransportType(str, Enum):
    HIGH_SPEED_TRAIN = "HIGH_SPEED_TRAIN"
    INTERCITY_TRAIN = "INTERCITY_TRAIN"
    INTER_REGIONAL_TRAIN = "INTER_REGIONAL_TRAIN"
    REGIONAL_TRAIN = "REGIONAL_TRAIN"
    CITY_TRAIN = "CITY_TRAIN"
    SUBWAY = "SUBWAY"
    TRAM = "TRAM"
    BUS = "BUS"
    FERRY = "FERRY"
    FLIGHT = "FLIGHT"
    CAR = "CAR"
    TAXI = "TAXI"
    SHUTTLE = "SHUTTLE"
    BIKE = "BIKE"
    SCOOTER = "SCOOTER"
    WALK = "WALK"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
