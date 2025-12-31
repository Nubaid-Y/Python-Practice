class City:
    def __init__(self, name, country, population, landmarks, year_created, rating):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.year_created = year_created
        self.rating = rating

NY = City("NY","US",20000000,"Time Square",1624,3.4)
London = City("London","UK",9000000,"Big Ben",43,4.2)

print(vars(NY))
print(vars(London))
