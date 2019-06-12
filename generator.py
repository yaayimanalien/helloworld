# Generates random integer between 0&9

import random
print(random.randint(0,9))

# 10 number ID generator




def generator():
    No1=(random.randint(0,9))
    No2=(random.randint(0,9))
    No3=(random.randint(0,9))
    No4=(random.randint(0,9))
    No5=(random.randint(0,9))
    No6=(random.randint(0,9))
    No7=(random.randint(0,9))
    No8=(random.randint(0,9))
    No9=(random.randint(0,9))
    numbers=(int(str(No1) + str(No2) + str(No3) + str(No4) + str(No5) + str(No6) + str(No7) + str(No8) + str(No9)))
    print(numbers)

generator()
