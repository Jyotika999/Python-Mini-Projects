import random

upper_char = ['A','B','C','D','E']
lower_char = ['a', 'b' ,'c' ,'d','e']
num= ['1','2','3','4','5']
special_char = ['@','#','$','*','&']

pas = random.choice(upper_char)+random.choice(lower_char)+random.choice(special_char)+random.choice(num)


print(pas)