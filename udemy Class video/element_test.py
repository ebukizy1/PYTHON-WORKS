import unittest
import element


class Additon_Of_Float(unittest.TestCase):

    def test_lst_value_can_change(self):
        actual = [1, 2, 3, 4, 5, 6]
        expected = [0, 2, 3, 4, 5, 0]
        myObject = element.MyClass(actual)
        myValue = myObject.change_element_in_lst()
        self.assertEqual(expected, actual)


