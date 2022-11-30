import unittest
import numpy as np
from src.notscared.statistics.welford import Welford

# import python_file_name.py


class TestNotScared(unittest.TestCase):
    def test_example(self):
        self.assertTrue(2 == 2)


class TestWelford(unittest.TestCase):
    def test_all_0(self):
        # all values when n=0
        welford = Welford()
        # math.isclose since we'll be dealing with floating point arithmetic
        self.assertAlmostEqual(0, welford.mean)
        self.assertAlmostEqual(0, welford.std_dev)
        self.assertAlmostEqual(0, welford.variance)
        self.assertAlmostEqual(0, welford.n)

    def test_mean_10(self):
        # mean when n=10
        welford = Welford()
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for x in list:
            welford.push(x)
        self.assertAlmostEqual(np.mean(list), welford.mean)

    def test_variance_10(self):
        # variance when n=10
        welford = Welford()
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for x in list:
            welford.push(x)
        self.assertAlmostEqual(np.var(list), welford.variance)

    def test_stddev_10(self):
        # standard deviation when n=10
        welford = Welford()
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for x in list:
            welford.push(x)
        self.assertAlmostEqual(np.std(list), welford.std_dev)

    # Review Tests
    def test_mean_random_10(self):
        # Mean when n=10 and random integers are chosen
        welford = Welford()
        random_list = np.random.randint(32, 192, 10, dtype=np.uint8)
        for x in random_list:
            welford.push(x)
        self.assertAlmostEqual(np.mean(random_list), welford.mean)

    def test_variance_random_10(self):
        # Variance when n=10 and random integers are chosen
        welford = Welford()
        random_list = np.random.randint(32, 192, 10, dtype=np.uint8)
        for x in random_list:
            welford.push(x)
        self.assertAlmostEqual(np.var(random_list), welford.variance)

    def test_stddev_random_10(self):
        # Mean when n=10 and random integers are chosen
        welford = Welford()
        random_list = np.random.randint(32, 192, 10, dtype=np.uint8)
        for x in random_list:
            welford.push(x)
        self.assertAlmostEqual(np.std(random_list), welford.std_dev)

if __name__ == "__main__":
    unittest.main()
