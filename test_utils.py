"""
In this module the functions of utils.py are tested
"""

import utils


def test_investment_costs():
    """Test the function investment_cost"""
    assert utils.investment_costs(1, 1, 1, 1) == 2


def test_replacement_costs():
    """Test the function replacement_costs"""
    assert utils.replacement_costs(1, 1, 1, 1) == 2
