import random
result='my_number:'
for i in range(3): 
    num=random.randint(1,6)
    result=f"{i}:{num}"
    print(result)
