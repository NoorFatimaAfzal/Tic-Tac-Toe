import random
choice="ghedvhewvjw763et763$%^&((@12))"
passward=""
for i in range(10):
    passward+="".join(random.choice(choice))
print(passward)