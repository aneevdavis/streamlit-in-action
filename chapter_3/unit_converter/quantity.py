from dataclasses import dataclass
from typing import Dict

from .unit import Unit


@dataclass
class Quantity:
    standard_unit: str
    units: Dict[str, Unit]
