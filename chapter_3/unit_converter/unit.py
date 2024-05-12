from dataclasses import dataclass


@dataclass
class Unit:
    abbreviation: str
    value_in_standard_units: float
