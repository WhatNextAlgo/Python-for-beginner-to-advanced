a_couple_of_letters = ["a", "b", "c", "d", "e", "f"]
print(list(zip(a_couple_of_letters,[ord(x) for x in a_couple_of_letters])))

location = ["Helgoland", "Kiel", 
            "Berlin-Tegel", "Konstanz", 
            "Hohenpeißenberg"]
air_pressure = [1021.2, 1019.9, 1023.7, 1023.1, 1027.7]
temperatures = [6.0, 4.3, 2.7, -1.4, -4.4]
altitude = [4, 27, 37, 443, 977]
print(list(zip(location, air_pressure, temperatures, altitude)))


food = ["ham", "spam", "cheese"]
for item in zip(range(1000, 1003), food):
    print(item)

#Calling zip with no Argument
for i in zip():
    print("This will not be printed")


s = "Python"
for t in zip(s):
    print(t)

#Parameters with Different Lengths

colors = ["green", "red", "blue"]
cars = ["BMW", "Alfa Romeo"]
for car, color in zip(cars, colors):
    print(car, color)

#Advanced Usages of zip

cities_and_population = [("Zurich", 415367),
                         ("Geneva", 201818),
                         ("Basel", 177654),
                         ("Lausanne", 139111),
                         ("Bern", 133883),
                         ("Winterthur", 111851)]

cities, population = list(zip(*cities_and_population))
print(cities,population)

#Converting two Iterables into a Dictionary
abc = "abcdef"
morse_chars = [".-", "-...", "-.-.", "-..", ".", "..-."]
text2morse = dict(zip(abc, morse_chars))
print(text2morse)




