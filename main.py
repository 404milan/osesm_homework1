"""
Calculation of investment and replacement costs for an energy storage system
"""
import utils

#specific ess power capacity investment cost [EUR/kW]
cp_inv = 500
#specific ess energy capacity investment cost [EUR/kWh]
ce_inv = 500
#specific ess power capacity replacemen cost [EUR/kW]
cp_rep = 100
#specific ess energy capacity replacement cost [EUR/kWh]
ce_rep = 200
#nominal ess power capacity kW
cap_p_nom = 1
#nominal ess energy capacity kWh
cap_e_nom = 1000


#calculating investment costs of an ess
investment_costs = utils.investment_costs(cp_inv, cap_p_nom, ce_inv, cap_e_nom)

#calculating replacement costs of an ess
replacement_costs = utils.replacement_costs(cp_rep, cap_p_nom, ce_rep, cap_e_nom)

print("\nInvestment costs are " + str(investment_costs) + " EUR")
print("\nReplacement costs are " + str(replacement_costs) + " EUR")


# print("Investment costs are" + investment_costs + "EUR")
# print("Replacement costs are" + replacement_costs + "EUR")