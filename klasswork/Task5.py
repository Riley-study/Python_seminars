import random
from random import randint
randint(0, 20)
new_list = [random.randint(0, 20) for _ in range(0, 20)]
print(new_list)

set_list = set(new_list)
print(set_list)

print(len(set_list))
