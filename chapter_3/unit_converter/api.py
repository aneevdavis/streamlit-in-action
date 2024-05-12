from .unit_config import unit_config


def convert_value(quantity_name, from_unit_name, to_unit_name, value):
    try:
        quantity = unit_config[quantity_name]
        from_unit = quantity.units[from_unit_name]
        to_unit = quantity.units[to_unit_name]

        value_in_to_unit = _convert_value(from_unit, to_unit, value)
        return {
            "code": 0,
            "result": value_in_to_unit
        }

    except KeyError:
        if quantity_name not in unit_config:
            return {"code": 1, "error": f"Unknown quantity: {quantity_name}"}
        if from_unit_name not in quantity.units:
            return {"code": 2, "error": f"Unknown unit: {from_unit_name}"}
        if to_unit_name not in quantity.units:
            return {"code": 3, "error": f"Unknown unit: {to_unit_name}"}


def convert_value_to_all_units(quantity_name, from_unit_name, value):
    try:
        results = {}

        quantity = unit_config[quantity_name]
        from_unit = quantity.units[from_unit_name]

        for to_unit_name, to_unit in quantity.units.items():
            if to_unit_name != from_unit_name:
                results[to_unit_name] = _convert_value(from_unit, to_unit, value)

        return {
            "code": 0,
            "result": results
        }

    except KeyError:
        if quantity_name not in unit_config:
            return {"code": 1, "error": f"Unknown quantity: {quantity_name}"}
        if from_unit_name not in quantity.units:
            return {"code": 2, "error": f"Unknown unit: {from_unit_name}"}


def _convert_value(from_unit, to_unit, value):
    value_in_std_units = value * from_unit.value_in_standard_units
    value_in_to_unit = value_in_std_units / to_unit.value_in_standard_units
    return value_in_to_unit
