# Leer una medida en pies
# Mostrar distancia equivalente en pulgadas, yardas y millas

user_ft = float(input('Introduce your ft here to convert: '))

ft = 1

# a/b = x/c ; x = (a * c) / b

hypothesis_one = user_ft / ft

print('-------------------------------')

# user_ft = x yards
# 1 ft = 0.333333 yards
# a/b = x/c ; x = (a * c) / b

ft_yard = 0.333333

print(f'1 ft is equivalent to {ft_yard} yards')

ft_to_yards = (ft_yard * user_ft) / ft

hypothesis_two = ft_to_yards / ft_yard

print(hypothesis_one)

print(hypothesis_two)

if hypothesis_one == hypothesis_two:
    print(f'Your hypothesis is right. Your ft is equivalent to {ft_to_yards} yards')
else:
    print('Your hypothesis is wrong')
    
    
print('-------------------------------')

# user_ft = x inch
# 1 ft = 12 inch


ft_inch = 12

print(f'1 ft is equivalent to {ft_inch} inch')

ft_to_inch = (ft_inch * user_ft) / ft

# x = (a * c) / b

hypothesis_three = ft_to_inch / ft_inch

print(hypothesis_one)

print(hypothesis_three)

if hypothesis_one == hypothesis_three:
    print(f'Your hypothesis is right. Your ft is equivalent to {ft_to_inch} inch')
else:
    print('Your hypothesis is wrong')
    

print('-------------------------------')

# user_ft = x miles
# 1 ft =  0.000189394 miles

ft_miles = 0.000189394

print(f'1 ft is equivalent to {ft_miles} miles')

ft_to_miles = (ft_miles * user_ft) / ft

# x = (a * c) / b

hypothesis_four = ft_to_miles / ft_miles

print(hypothesis_one)

print(hypothesis_four)

if hypothesis_one == hypothesis_four:
    print(f'Your hypothesis is right. Your ft is equivalent to {ft_to_miles} miles')
else:
    print('Your hypothesis is wrong')
    

print('-------------------------------')