squares = [value**2 for value in range(1,8)]
print(squares)

num = [value+1 for value in range(0,20)]
print(num)

big_num = list(range(1,1000001))
print(big_num[-1])
print(min(big_num))
print(max(big_num))
print(sum(big_num))

odd_num = [value for value in range(1,20,2)]
print(odd_num)

thr_mult = [value for value in range(0,20,3)]
print(thr_mult)

cube = [value**3 for value in range(0,20)]
print(cube)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)


names = ['john','jake','abby','carlos','unice']
print(names[3:])

foods = ['apple','banana','mango','strawberry','grapes']
print(foods)

bad_food = foods[:]
print(bad_food[1:3])

#[start:end:step] This is what i was attempting to think of when doing these


age = 98
print(f'my age is {age} today and i love feeling this young')


grocery_list = ['dip','chips','fruit','juice']
for item in grocery_list:
    if item[0:5] == 'j':
        print(item)
    else:
        print('Does not start with the proper letter')
        break
