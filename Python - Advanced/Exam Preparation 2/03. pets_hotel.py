def accommodate_new_pets(capacity, weight, *pets):
    result = []
    pets_map = {}
    for pet_type, pet_weight in pets:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets_map!")
            break
        if pet_weight > weight:
            continue
        if pet_type not in pets_map:
            pets_map[pet_type] = 0
        pets_map[pet_type] += 1
        capacity -= 1
    else:
        result.append(f"All pets_map are accommodated! Available capacity: {capacity}")

    result.append("Accommodated pets_map:")
    [result.append(f"{k}: {v}") for k, v in sorted(pets_map.items())]
    return '\n'.join(result)


print(accommodate_new_pets(10, 15.0, ("cat", 5.8), ("dog", 10.0), ))
