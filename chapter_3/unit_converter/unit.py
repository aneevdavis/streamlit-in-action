from dataclasses import dataclass


@dataclass
class Unit:
    name: str
    abbreviation: str
    value_in_standard_units: float
