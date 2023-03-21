#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app import process_input


class TestApp(unittest.TestCase):
	def setUp(self):
		self.a = 10
		self.b = 5

	def test_add(self):
		result = process_input(self.a, self.b, "add")
		self.assertEqual(result, 15)

	def test_divide(self):
		result = process_input(self.a, self.b, "divide")
		self.assertEqual(result, 2)

	def test_multiple(self):
		result = process_input(self.a, self.b, "multiple")
		self.assertEqual(result, 50)

	def test_subtract(self):
		result = process_input(self.a, self.b, "subtract")
		self.assertEqual(result, 5)


def suite():
	s = unittest.TestSuite()
	s.addTests(
		unittest.TestLoader().loadTestsFromTestCase(TestApp)
	)
	return s


if __name__ == '__main__':
	unittest.TextTestRunner(verbosity=2).run(suite())
