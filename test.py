import unittest
import pytest
from main import count_vowels


# Тесты для unittest
class TestCountVowelsUnittest(unittest.TestCase):
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)
        self.assertEqual(count_vowels("aaa"), 3)
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("123!@#"), 0)
        self.assertEqual(count_vowels("   "), 0)

    def test_mixed_strings(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)
        self.assertEqual(count_vowels("Python is awesome"), 6)
        self.assertEqual(count_vowels("The quick brown fox"), 5)


# Тесты для pytest
def test_all_vowels_pytest():
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("aaa") == 3
    assert count_vowels("") == 0


def test_no_vowels_pytest():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("123!@#") == 0
    assert count_vowels("   ") == 0


def test_mixed_strings_pytest():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("Python is awesome") == 6
    assert count_vowels("The quick brown fox") == 5


# Запуск unittest (если файл запускается напрямую)
if __name__ == "__main__":
    unittest.main()