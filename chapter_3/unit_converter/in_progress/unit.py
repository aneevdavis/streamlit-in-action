from dataclasses import dataclass


@dataclass
class Unit:
    abbrev: str
    value_in_std_units: float
