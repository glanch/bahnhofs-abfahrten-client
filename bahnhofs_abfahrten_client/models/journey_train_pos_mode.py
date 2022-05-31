from enum import Enum


class JourneyTrainPosMode(str, Enum):
    CALC = "CALC"
    CALC_FOR_REPORT = "CALC_FOR_REPORT"
    CALC_ONLY = "CALC_ONLY"
    CALC_REPORT = "CALC_REPORT"
    REPORT_ONLY = "REPORT_ONLY"
    REPORT_ONLY_WITH_STOPS = "REPORT_ONLY_WITH_STOPS"

    def __str__(self) -> str:
        return str(self.value)
