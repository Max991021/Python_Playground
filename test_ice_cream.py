import unittest
import ice_cream as adv

class TestAdvancedExercises(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(adv.reverse_string("hello"), "olleh")
        self.assertEqual(adv.reverse_string(""), "")
        self.assertEqual(adv.reverse_string("a"), "a")

    def test_factorial(self):
        self.assertEqual(adv.factorial(0), 1)
        self.assertEqual(adv.factorial(5), 120)
        self.assertIsNone(adv.factorial(-3))

    def test_fibonacci(self):
        self.assertEqual(adv.fibonacci(0), 0)
        self.assertEqual(adv.fibonacci(1), 1)
        self.assertEqual(adv.fibonacci(7), 13)
        self.assertIsNone(adv.fibonacci(-2))

    def test_is_prime(self):
        self.assertTrue(adv.is_prime(2))
        self.assertTrue(adv.is_prime(17))
        self.assertFalse(adv.is_prime(1))
        self.assertFalse(adv.is_prime(0))
        self.assertFalse(adv.is_prime(18))

    def test_sum_digits(self):
        self.assertEqual(adv.sum_digits(123), 6)
        self.assertEqual(adv.sum_digits(0), 0)
        self.assertEqual(adv.sum_digits(9999), 36)
        self.assertEqual(adv.sum_digits(-123), 6)

    def test_count_words(self):
        self.assertEqual(adv.count_words("Hello world"), 2)
        self.assertEqual(adv.count_words("One"), 1)
        self.assertEqual(adv.count_words(""), 0)
        self.assertEqual(adv.count_words("  Lots   of  spaces "), 3)

    def test_merge_lists_unique(self):
        self.assertCountEqual(adv.merge_lists_unique([1,2,3],[3,4,5]), [1,2,3,4,5])
        self.assertEqual(adv.merge_lists_unique([], []), [])

    def test_most_frequent(self):
        lst = [1,1,2,3,1,2,2]
        self.assertIn(adv.most_frequent(lst), [1,2])
        self.assertIsNone(adv.most_frequent([]))

    def test_is_anagram(self):
        self.assertTrue(adv.is_anagram("listen", "silent"))
        self.assertTrue(adv.is_anagram("Triangle", "integral"))
        self.assertFalse(adv.is_anagram("hello", "world"))

    def test_count_even_odd(self):
        self.assertEqual(adv.count_even_odd([1,2,3,4]), (2,2))
        self.assertEqual(adv.count_even_odd([2,4,6]), (3,0))
        self.assertEqual(adv.count_even_odd([1,3,5]), (0,3))
        self.assertEqual(adv.count_even_odd([]), (0,0))

    def test_reverse_list(self):
        self.assertEqual(adv.reverse_list([1,2,3]), [3,2,1])
        self.assertEqual(adv.reverse_list([]), [])
        self.assertEqual(adv.reverse_list(["a"]), ["a"])

    def test_square_numbers(self):
        self.assertEqual(adv.square_numbers([1,2,3]), [1,4,9])
        self.assertEqual(adv.square_numbers([]), [])
        self.assertEqual(adv.square_numbers([-2,0,5]), [4,0,25])

    def test_fibonacci_sequence(self):
        self.assertEqual(adv.fibonacci_sequence(0), [])
        self.assertEqual(adv.fibonacci_sequence(1), [0])
        self.assertEqual(adv.fibonacci_sequence(2), [0,1])
        self.assertEqual(adv.fibonacci_sequence(5), [0,1,1,2,3])
        self.assertEqual(adv.fibonacci_sequence(-3), [])

# Allow running the tests directly
if __name__ == "__main__":
    unittest.main()


    def test_reverse_list(self):
        self.assertEqual(adv.reverse_list([1,2,3]), [3,2,1])
        self.assertEqual(adv.reverse_list([]), [])
        self.assertEqual(adv.reverse_list(["a"]), ["a"])

    def test_square_numbers(self):
        self.assertEqual(adv.square_numbers([1,2,3]), [1,4,9])
        self.assertEqual(adv.square_numbers([]), [])
        self.assertEqual(adv.square_numbers([-2,0,5]), [4,0,25])

    def test_fibonacci_sequence(self):
        self.assertEqual(adv.fibonacci_sequence(0), [])
        self.assertEqual(adv.fibonacci_sequence(1), [0])
        self.assertEqual(adv.fibonacci_sequence(2), [0,1])
        self.assertEqual(adv.fibonacci_sequence(5), [0,1,1,2,3])
        self.assertEqual(adv.fibonacci_sequence(-3), [])

# Allow running the tests directly
if __name__ == "__main__":
    unittest.main()
