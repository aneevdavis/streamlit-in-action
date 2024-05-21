from dataclasses import dataclass
from typing import Dict

from unit import Unit


@dataclass
class Quantity:
    std_unit: str
    units: Dict[str, Unit]
