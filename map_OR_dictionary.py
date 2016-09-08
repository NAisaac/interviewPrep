"""
Time to play with dictionaries!

{Continent: {Country: [City or Cities]}}

Information to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Print a list of all cities in the USA in alphabetic order
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
	print city

# Print all cities in Asia, in alphabetic
asia_cities = []
for country, city in locations['Asia'].items():
	city_country = city[0] + " - " + country
	asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
	print city