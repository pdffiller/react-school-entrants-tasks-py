import unittest
from task_2 import have_same_items
from test.task_2.fixtures import fixtures


class HaveSameItemsTest(unittest.TestCase):
    pass

def test_generator(first, second, result):
    def test(self):
        self.assertEqual(
          have_same_items(first[:], second[:]),
          result)
    return test

def frozen_test_generator(first, second, result):
    def test(self):
        first_prev = first[:]
        second_prev = second[:]
        self.assertEqual(
          have_same_items(first, second),
          result)
        self.assertEqual(first, first_prev)
        self.assertEqual(second, second_prev)
    return test

for key, t in fixtures.items():
    test_name = 'test_%s' % key
    test = test_generator(t[0], t[1], t[2])
    setattr(HaveSameItemsTest, test_name, test)

for key, t in list(fixtures.items())[-2:]:
    test_name = 'test_%s_frozen' % key
    test = frozen_test_generator(t[0], t[1], t[2])
    setattr(HaveSameItemsTest, test_name, test)
        
if __name__ == '__main__':
    unittest.main()
