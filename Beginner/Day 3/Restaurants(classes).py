class Restaurant:
  name = ""
  category = ""
  rating = 0.0
  commercial = False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.commercial = False 

McDonalds = Restaurant()

McDonalds.name = 'McDonalds'
McDonalds.category = 'Fast Food'
McDonalds.rating = 3.5
McDonalds.commercial = True

KFC = Restaurant()

KFC.name = 'KFC'
KFC.category = 'Fast Food'
KFC.rating = 3.2
KFC.commercial = True

print(vars(bobs_burgers))

print(vars(McDonalds))

print(vars(KFC))