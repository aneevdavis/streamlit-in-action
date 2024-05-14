from unit_config import unit_config
from result import Result
from unit import Unit


def list_quantities() -> list[str]:
    return list(unit_config.keys())


def list_units(quantity_name) -> list[str]:
    return list(unit_config[quantity_name].units.keys())


def convert_value(quantity_name: str, from_unit_name: str, to_unit_name: str, value: float) -> Result:
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    value_in_to_unit = _convert_value(from_unit, to_unit, value)
    return Result(from_unit, to_unit, value, value_in_to_unit)


def convert_value_to_all_units(quantity_name: str, from_unit_name: str, value: float) -> dict[str, Result]:
    results = {}

    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]

    for to_unit_name, to_unit in quantity.units.items():
        if to_unit_name != from_unit_name:
            converted_value = _convert_value(from_unit, to_unit, value)
            results[to_unit_name] = Result(from_unit, to_unit, value, converted_value)

    return results


def _convert_value(from_unit: Unit, to_unit: Unit, value: float) -> float:
    value_in_std_units = value * from_unit.value_in_standard_units
    value_in_to_unit = value_in_std_units / to_unit.value_in_standard_units
    return value_in_to_unit
