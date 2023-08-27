# Write a program that will tell the number of dogs and chicken are
# there when the user will provide the value of total heads and legs.
def num_dog_chicken(heads,legs):
    for num_dogs in range(heads +1):
        num_chikens = heads - num_dogs
        if (4*num_dogs + 2*num_chikens) == legs:
            return num_dogs,num_chikens
    return None

tlegs = 56
theads = 20

result = num_dog_chicken(theads,tlegs)
if result is not None :
    num_dogs,num_chikens = result
    print("num_dogs",num_dogs )
    print("num_chickens",num_chikens )
else:
    print("no")
