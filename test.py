import unittest

from poe_ninja_api import get_currency_history, get_currency_overview, get_item_history


class TestPoeNinjaApi(unittest.TestCase):
    def test_get_currency_history(self):
        league = 'Necropolis'
        type_ = 'Currency'
        currency_id = '21'

        result = get_currency_history(league, type_, currency_id)

        self.assertIsNotNone(result)

    def test_get_currency_overview(self):
        league = 'Necropolis'
        type_ = 'Currency'

        result = get_currency_overview(league, type_)

        self.assertIsNotNone(result)

    def test_get_item_history(self):
        league = 'Necropolis'
        type_ = 'BaseType'
        item_id = '109670'

        result = get_item_history(league, type_, item_id)

        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()

