import unittest
from knapsack import Knapsack
import time

class KnapsackBottomUpV1Test(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    # def test1(self):
    #     values = [92,57,49,68,60,43,67,84,87,72]
    #     weights = [23,31,29,44,53,38,63,85,89,82]
    #     capacity = 165
    #     solution = [1,1,1,1,0,1,0,0,0,0]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    # def test2(self):
    #     values = [24,13,23,15,16]
    #     weights = [12,7,11,8,9]
    #     capacity  = 26
    #     solution = [0,1,1,1,0]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    # def test3(self):
    #     values = [50,50,64,46,50,5]
    #     weights = [56,59,80,64,75,17]
    #     capacity = 190
    #     solution = [1,1,0,0,1,0]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    # def test4(self):
    #     values = [70,20,39,37,7,5,10]
    #     weights = [31,10,20,19,4,3,6]
    #     capacity = 50
    #     solution = [1,0,0,1,0,0,0]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    # def test5(self):
    #     values = [350,400,450,20,70,8,5,5]
    #     weights = [25,35,45,5,25,3,2,2]
    #     capacity = 104
    #     solution = [1,0,1,1,1,0,1,1]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    # def test6(self):
    #     values = [442,525,511,593,546,564,617]
    #     weights = [41,50,49,59,55,57,60]
    #     capacity = 170
    #     solution = [0,1,0,1,0,0,1]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)

    
    # def test7(self):
    #     values = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]
    #     weights = [70,73,77,80,82,87,90,94,98,106,110,113,115,118,120]
    #     capacity = 750
    #     solution = [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1]

    #     expected = 0
    #     for i in range(len(solution)):
    #         if solution[i] == 1:
    #             expected += values[i]
    #     knapsack_solver = Knapsack(values, weights, capacity)
    #     actual = knapsack_solver.knapsack_bottom_up_v1()
    #     self.assertEqual(actual, expected)


    def test8(self):
        values = [825594,1677009,1676628,1523970,943972,97426,69666,1296457,1679693,\
                  1902996,1844992,1049289,1252836,1319836,953277,2067538,675367,853655,\
                  1826027,65731,901489,577243,466257,369261]
        weights = [382745,799601,909247,729069,467902,44328,34610,698150,823460,903959,\
                   853665,551830,610856,670702,488960,951111,323046,446298,931161,31385,\
                   496951,264724,224916,169684]
        capacity = 6404180
        solution = [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1]

        expected = 0
        for i in range(len(solution)):
            if solution[i] == 1:
                expected += values[i]
        knapsack_solver = Knapsack(values, weights, capacity)
        actual = knapsack_solver.knapsack_bottom_up_v1()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KnapsackBottomUpV1Test)
    unittest.TextTestRunner(verbosity=0).run(suite)