from quantity import Quantity
from unit import Unit

unit_config: dict[str, Quantity] = {
    "Mass": Quantity(
        std_unit="Kilograms",
        units={
            "Kilograms": Unit(abbrev="kg", value_in_std_units=1),
            "Grams": Unit(abbrev="g", value_in_std_units=0.001),
            "Pounds": Unit(abbrev="lb", value_in_std_units=0.453592),
            "Ounces": Unit(abbrev="oz", value_in_std_units=0.0283495),
        }
    ),
    "Length": Quantity(
        std_unit="Meters",
        units={
            "Meters": Unit(abbrev="m", value_in_std_units=1),
            "Centimeters": Unit(abbrev="cm", value_in_std_units=0.01),
            "Inches": Unit(abbrev="in", value_in_std_units=0.0254),
            "Feet": Unit(abbrev="ft", value_in_std_units=0.3048),
        }
    ),
    "Time": Quantity(
        std_unit="Seconds",
        units={
            "Seconds": Unit(abbrev="s", value_in_std_units=1),
            "Minutes": Unit(abbrev="min", value_in_std_units=60),
            "Hours": Unit(abbrev="hr", value_in_std_units=3600),
            "Days": Unit(abbrev="d", value_in_std_units=86400),
        }
    ),
}