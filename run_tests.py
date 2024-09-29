#Replace tests_repetion with tests_functions.
import unittest
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
