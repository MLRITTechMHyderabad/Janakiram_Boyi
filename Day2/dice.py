d1 = [1,2,3,4,5,6]
d2 = [1,2,3,4,5,6]
li =[]

for i in d1:
    for j in d2:
        li.append((i,j))
print(li)
di = {}
for i in range (2,13):
    c=0
    for j in li:
        if i == j[0]+j[1]:
            c+=1
    di[str(i)] = c/len(li)
print()
print(di)

import random

p1_d1 = random.randint(1,6)
p1_d2 = random.randint(1,6)
p1_sum = p1_d1 + p1_d2
print("person1 sum", p1_sum)

p2_d1 = random.randint(1,6)
p2_d2 = random.randint(1,6)
p2_sum = p2_d1 + p2_d2
print("person2 sum", p1_sum)

prob1 = di[str(p1_sum)]
prob2 = di[str(p2_sum)]

if prob1 < prob2:
    print(f'person1 has {p1_sum} and  wins  with {prob1}')
elif prob1 > prob2:
    print(f'person2 has {p2_sum} wins with {prob2}')
else :
    print('Its a Draw Match')