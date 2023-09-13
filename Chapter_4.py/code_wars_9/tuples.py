
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#dimensions = (200,50)
#dimensions[0] = 250

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


cars = ['audi','bmw','subarau','toyota']

for car in cars:
    if car == 'toyota':
        print(car.upper())
    else:
        print(car.title())


car ='subaru'
print("is car =='subaru'? Prolly.")
print(car=='subaru')
print(car =='audi')

car = 'Audi'
print(car.lower() == 'audi')

num = 21
print(num > 20)

animal = 'giraffe'
thought = input()
print(animal == thought)


#dr_age = 21
#print('How old are you ? ')
#user_age = input()
#for age in user_age:
    #if user_age >= dr_age:
        #print('Please tell me what you would like to drink.')
    #else:
        #print("Hey dumbass you're too young to drink here.")

#names = ['jonas','maia','mateo','kim','kerri','loki','willow']
#name = input()
#for name in names:
   # #if name == names:
        #print('Great to see you again')
   # else:
        #print("We've never met!")




