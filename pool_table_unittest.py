import unittest
from pool_table import main, calculate_total_time_played, calculate_amount, display_tables, save_log, print_out_log


class PoolTableTests(unittest.TestCase):
    def test_amt_calculation(self):
        self.assertEqual(30, calculate_amount(60))


unittest.main()
