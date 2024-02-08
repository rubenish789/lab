def gramsToOunces(grams):
    return (28.3495231 * grams)

grams = int(input("Write amount of grams: "))

print("You have to put", gramsToOunces(grams), "ounces")