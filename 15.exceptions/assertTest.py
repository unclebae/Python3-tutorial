def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0)
    return ((Temperature-273)*1.8) + 32

print (KelvinToFahrenheit(273))
print (KelvinToFahrenheit(505.78))
print (KelvinToFahrenheit(-5))
