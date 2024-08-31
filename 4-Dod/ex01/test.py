from in_out import outer
from in_out import square
from in_out import pow
# import unittest

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())


# class Test_ft_statistics(unittest.TestCase):
# 	def school_test():
# 		my_counter = outer(3, square)
# 		print(my_counter())
# 		print(my_counter())
# 		print(my_counter())
# 		print("---")
# 		another_counter = outer(1.5, pow)
# 		print(another_counter())
# 		print(another_counter())
# 		print(another_counter())

