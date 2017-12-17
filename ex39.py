# create a mapping of state to abbreviation
states = {
	'Schleswig-Holstein': 'SH',
	'Lower Saxony': 'LS',
	'Saxony': 'SX',
	'Hamburg': 'HH',
	'Bavaria': 'FB'
}

# create a basic set of states and some cities in them
cities = {
	'LS': 'Lueneburg',
	'SX': 'Leipzig',
	'SH': 'Luebeck'
}

# add some more cities
cities['FB'] = 'Muenchen'
cities['HH'] = 'Hamburg City'

#print out some cities
print '-' * 10
print "Lower Saxony has: ", cities['LS']
print "Saxony has: ", cities['SX']

# print some states
print '-' * 10
print "Schleswig-Holstein's abbreviation is: ", states['Schleswig-Holstein']
print "Sachsen's abbreviation is: ", states['Saxony']

# do it by using the state then citites dict
print '-' * 10
print "Bavaria has: ", cities[states['Bavaria']]
print "Schleswig-Holstein has: ", cities[states['Schleswig-Holstein']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Saarland')

if not state:
	print "Sorry, no Saarland."

# get a city with a default value
city = cities.get('SL', 'Does Not Exist')
print "The city for the state 'SL' is: %s" % city