def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result:
        return (f"Spell \33[32mrecorded\33[37m: {spell_name} "
                f"({validation_result})")
    return f"Spell \33[31mrejected\33[37m: {spell_name} ({validation_result})"
