from dataclasses import dataclass

from unit import Unit


@dataclass
class Result:
    from_unit: Unit
    to_unit: Unit
    from_value: float
    to_value: float
