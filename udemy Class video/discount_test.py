import unittest
import discount


class Additon_Of_Float(unittest.TestCase):

    def test_i_Could_get_the_discount(self):
        my_object = discount.MyClass(100, 10)
        discountValues = my_object.disCount_Price()
        self.assertEqual(10, discountValues)

    def test_Negative_value_Cant_be_Passed(self):
            my_object = discount.MyClass(-100, 10)
            self.assertRaises(TypeError, my_object.disCount_Price)

    def test_AlphabetCantBeEnter(self):
            my_object = discount.MyClass("a", 10)
            self.assertRaises(TypeError, my_object.disCount_Price)

    def test_Negative_discount_cant_be_enter(self):
        my_object = discount.MyClass(100, -10)
        self.assertRaises(TypeError, my_object.disCount_Price)

    def test_Alphabet_discount_cant_be_enter(self):
        my_object = discount.MyClass(100, "a")
        self.assertRaises(TypeError, my_object.disCount_Price)



