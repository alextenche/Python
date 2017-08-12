import cProfile

from binary_search import *
from linear_search import *


big_list = list(range(10000000))
print(len(big_list))

print(binary_search(big_list, 10000000))
print(linear_search(big_list, 10000000))

cProfile.run('binary_search(big_list, 10000000)')
cProfile.run('linear_search(big_list, 10000000)')
