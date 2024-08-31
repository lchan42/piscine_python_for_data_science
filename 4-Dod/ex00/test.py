# import numpy as np
# import math

# # from ft_statistics import ft_statistics, mean, median, quartile, \
# #             standard, variance

# from ft_statistics import bubble_sort, mean, median, quartile
# import statistics
# import unittest

# # run test with: python3 -m unittest -v test.py


# class Test_ft_statistics(unittest.TestCase):
#     def setUp(self):
#         self.lists = [
#             np.random.rand(5) * 100,
#             np.random.rand(6),
#             np.random.rand(7),
#             np.random.rand(8),
#             np.random.rand(9),
#             np.random.rand(10),
#             np.random.rand(11),
#             np.random.randint(0, 1000, size=5),
#             np.random.randint(0, 1000, size=6),
#             [1, 42, 360, 11, 64]
#         ]

#     def test_sort(self):
#         for lst in self.lists:
#             mine_result = bubble_sort(*lst)
#             real_result = sorted(lst)
#             self.assertEqual(mine_result, real_result,
#                              f"{mine_result} vs {real_result}")

#     def test_mean(self):
#         for lst in self.lists:
#             mine_result = mean(lst)
#             real_result = float(statistics.mean(lst))
#             self.assertAlmostEqual(
#                 mine_result,
#                 real_result,
#                 msg=f"\nlst: {lst} \n{mine_result} vs {real_result}",
#                 delta=0.001
#                 )

#     def test_median(self):
#         for lst in self.lists:
#             mine_result = median(bubble_sort(*lst))
#             real_result = statistics.median(lst)
#             self.assertAlmostEqual(
#                 mine_result,
#                 real_result,
#                 msg=f"\nlst : {lst}\n {mine_result}\nvs\n{real_result}",
#                 delta=0.001
#                 )
#         pass

#     def test_standard(self):
#         # Écrire des tests pour la fonction standard()
#         pass

#     def test_variance(self):
#         # Écrire des tests pour la fonction variance()
#         pass

#     def test_ft_statistics(self):
#         # Écrire des tests pour la fonction ft_statistics()
#         pass


# if __name__ == '__main__':
#     unittest.main()


#     # def test_mean(self):
#     # 	self.assertEqual
# # ft_statistics(toto="mean", tutu="median", tata="quartile")
# # print("expecting: ERROR")


# # print("----")
# # data = [1, 2]
# # ft_statistics(*data, toto="mean", tutu="median", tata="quartile")


# # print("----")
# # print("expecting: ERROR")
# # ft_statistics(1, 2, "lol", toto="mean", tutu="median", tata="quartile")


# # print("----")
# # ft_statistics(1.1234, 2, 3.14, toto="mean", tutu="median", tata="quartile")

from statistics import ft_statistics

print("---- subject test ----")
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
