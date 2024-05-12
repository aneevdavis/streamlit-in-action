from unit_config import unit_config


def list_quantities():
    return list(unit_config.keys())


def list_units(quantity_name):
    return list(unit_config[quantity_name])


def convert_value(quantity_name, from_unit_name, to_unit_name, value):
    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]

    value_in_to_unit = _convert_value(from_unit, to_unit, value)
    return {
        "code": 0,
        "result": value_in_to_unit
    }


def convert_value_to_all_units(quantity_name, from_unit_name, value):
    results = {}

    quantity = unit_config[quantity_name]
    from_unit = quantity.units[from_unit_name]

    for to_unit_name, to_unit in quantity.units.items():
        if to_unit_name != from_unit_name:
            results[to_unit_name] = _convert_value(from_unit, to_unit, value)

    return results


def _convert_value(from_unit, to_unit, value):
    value_in_std_units = value * from_unit.value_in_standard_units
    value_in_to_unit = value_in_std_units / to_unit.value_in_standard_units
    return value_in_to_unit