import unittest
from  src.arabToRom import int_to_roman

# Unit test suite
class TestIntToRoman(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(5), "V")
        self.assertEqual(int_to_roman(9), "IX")

    def test_tens(self):
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(50), "L")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(99), "XCIX")

    def test_hundreds(self):
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(900), "CM")
        self.assertEqual(int_to_roman(999), "CMXCIX")

    def test_thousands(self):
        self.assertEqual(int_to_roman(1000), "M")
        self.assertEqual(int_to_roman(2000), "MM")
        self.assertEqual(int_to_roman(3000), "MMM")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_out_of_range(self):
        self.assertEqual(int_to_roman(0), "Input must be between 1 and 3999")
        self.assertEqual(int_to_roman(4000), "Input must be between 1 and 3999")
        self.assertEqual(int_to_roman(-1), "Input must be between 1 and 3999")

    def test_random_cases(self):
        self.assertEqual(int_to_roman(58), "LVIII")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")
        self.assertEqual(int_to_roman(2023), "MMXXIII")

# Run the tests
if __name__ == "__main__":
    unittest.main()