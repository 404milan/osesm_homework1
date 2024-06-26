"""
This module defines the functions required for calculating investment
and replacement costs for energy storage systems.
The parameters are defined in main.py.
"""


def investment_costs(cp_inv, cap_p_nom, ce_inv, cap_e_nom):
    """Calculation of investment costs for energy storage system"""
    return cp_inv * cap_p_nom + ce_inv * cap_e_nom


def replacement_costs(cp_rep, cap_p_nom, ce_rep, cap_e_nom):
    """Calculation of replacement costs for energy storage system"""
    return cp_rep * cap_p_nom + ce_rep * cap_e_nom
