def forecast(*weather_data):
    locations = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for location, weather in weather_data:
        locations[weather].append(location)
    sorted_locations = {}
    for k, v in locations.items():
        if v:
            sorted_locations[k] = sorted(v)
    result = ''
    for key, value in sorted_locations.items():
        for x in value:
            result += f'{x} - {key}\n'
    return result


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
