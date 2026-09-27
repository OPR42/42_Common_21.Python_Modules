def validate_ingredients(ingredients: str) -> str:
    if ("fire" in ingredients
            or "water" in ingredients
            or "earth" in ingredients
            or "air" in ingredients):
        return f"{ingredients} - \33[32mVALID\33[37m"
    return f"{ingredients} - \33[31mINVALID\33[37m"
