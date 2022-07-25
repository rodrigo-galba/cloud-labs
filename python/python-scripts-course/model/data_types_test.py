import unittest


class DataTypesTest(unittest.TestCase):

    def test_map(self):
        my_dict = {'key': 'value'}
        self.assertEqual('value', my_dict['key'])
        self.assertEqual(1, len(my_dict))

    def test_list(self):
        my_list = [1, 2, 'test']
        self.assertEqual(1, my_list[0])

    def test_tuple(self):
        my_tuple = (1, 2, 'xupa java')
        self.assertEqual(1, my_tuple[0])

    def test_reverse_iterable(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(my_list, my_list[::])
        self.assertEqual([4, 3, 2, 1], my_list[::-1])

    def test_map_function(self):
        fibbo = lambda num: num**2
        print(list(map(fibbo, [1, 2, 3, 4])))

    def test_floor_division(self):
        self.assertEqual(1, 3//2)
        self.assertEqual(2, 5//2)
        self.assertEqual(3, 7//2)

    def test_shallow_copy(self):
        my_list = [1, 2]
        another_list = my_list
        self.assertEqual(1, my_list[0])
        self.assertEqual(1, another_list[0])

        another_list[0] = 10
        self.assertEqual(10, my_list[0])
        self.assertEqual(10, another_list[0])

    def test_deep_copy(self):
        my_list = [1, 2]
        another_list = my_list
        another_list = another_list.copy()
        self.assertEqual(1, my_list[0])
        self.assertEqual(1, another_list[0])

        another_list[0] = 10
        self.assertEqual(1, my_list[0])
        self.assertEqual(10, another_list[0])

    def test_self_keyword(this):
        this.assertTrue(True, "The instance of the class accept any word, like 'this'. To use 'self' is a convention")

if __name__ == '__main__':
    unittest.main()
