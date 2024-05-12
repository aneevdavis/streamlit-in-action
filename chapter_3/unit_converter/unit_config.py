from quantity import Quantity
from unit import Unit

unit_config = {
    "Mass": Quantity(
        standard_unit="Kilograms",
        units={
            "Kilograms": Unit(abbreviation="kg", value_in_standard_units=1),
            "Grams": Unit(abbreviation="g", value_in_standard_units=0.001),
            "Pounds": Unit(abbreviation="lb", value_in_standard_units=0.453592),
            "Ounces": Unit(abbreviation="oz", value_in_standard_units=0.0283495),
        }
    ),
    "Length": Quantity(
        standard_unit="Meters",
        units={
            "Meters": Unit(abbreviation="m", value_in_standard_units=1),
            "Centimeters": Unit(abbreviation="cm", value_in_standard_units=0.01),
            "Inches": Unit(abbreviation="in", value_in_standard_units=0.0254),
            "Feet": Unit(abbreviation="ft", value_in_standard_units=0.3048),
        }
    ),
    "Time": Quantity(
        standard_unit="Seconds",
        units={
            "Seconds": Unit(abbreviation="s", value_in_standard_units=1),
            "Minutes": Unit(abbreviation="min", value_in_standard_units=60),
            "Hours": Unit(abbreviation="hr", value_in_standard_units=3600),
            "Days": Unit(abbreviation="day", value_in_standard_units=86400),
        }
    ),
}