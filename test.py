import unittest

from suma import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test suma de lista de enteros
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()