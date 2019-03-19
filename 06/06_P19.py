file = open(input().strip())
fruits = []
for line in file:
    fruit, person = line.strip().split()
    fruit_names = [fruits[i][0] for i in range(len(fruits))]
    if fruit not in fruit_names:
        fruits.append([fruit,[person]])
    else:
        fruits[fruit_names.index(fruit)][1].append(person)
favorite = ''
people_count = -1
for fruit in fruits:
    if len(fruit[1]) > people_count:
        people_count = len(fruit[1])
        favorite = fruit[0]
print(fruits)
print('The most favorite fruit is',favorite)