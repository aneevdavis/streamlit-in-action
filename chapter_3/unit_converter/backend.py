from unit_config import unit_config
from result import Result


def list_quantities() -> list[str]:
    return list(unit_config.keys())


def list_units(quantity_name) -> list[str]:
    return list(unit_config[quantity_name].units.keys())


def convert_value(
        quantity_name: str,
        from_unit_name: str,
        to_unit_name: str,
        value: float) -> Result:
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    value_in_to_units = (value *
                         from_unit.value_in_std_units /
                         to_unit.value_in_std_units)

    return Result(from_unit, to_unit, value, value_in_to_units)
