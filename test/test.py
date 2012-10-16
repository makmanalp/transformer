from transformer import Document, Schema, Column, transforms
from unittest import TestCase
from decimal import Decimal, DecimalException

class TestTransforms(TestCase):

    def test_date_format_to_format(self):
        trans = transforms.date.format_to_format("%Y%m%d", "%m-%d-%Y")
        self.assertEqual("04-02-2012", trans.run("20120402"))
        self.assertRaises(ValueError, trans.run, ("040201"))

    def test_string_to_decimal(self):
        trans = transforms.number.string_to_decimal()
        self.assertEqual(Decimal("10.4"), trans.run("10.4"))
        self.assertRaises(DecimalException, trans.run, ("a"))
        self.assertRaises(DecimalException, trans.run, ("&^*"))
