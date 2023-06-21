import random
result = []
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0
# while n <= 100:
#     n += 1
#     result = random.choice(list)
    
    
    
    
for i in range(100):
    result.append(random.choice(list))

for number in list:
    count = result.count(number)
    print(f"{number} {count}")
 
    
    
    # if random.choice(list) == "heads":
        # heads += 1
    # else:
        # tails += 1
        
# print(tails,heads)
