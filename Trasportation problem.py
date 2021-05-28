
from pulp import *

# Sources and Destinations: List
Branch = ['A', 'B', 'C', 'D']
Warehouse = [1, 2, 3, 4]

# Supply from each Branch
supply = {'A': 35, 'B': 50, 'C': 80, 'D': 65}

# Demand of each Wareshouse
demand = {1: 70, 2: 30, 3: 75, 4: 55}

# Cost for all Braches and Wareshouse
cost = {'A': {1: 10, 2: 7, 3: 6, 4: 4},
        'B': {1: 8, 2: 8, 3: 5, 4: 7},
        'C': {1: 4, 2: 3, 3: 6, 4: 9},
        'D': {1: 7, 2: 5, 3: 4, 4: 3},
        }

# Setting Problem
prob = LpProblem("Транспортиране", LpMinimize)

routes = [(i, j) for i in Branch for j in Warehouse]

# Defining Decision Variables
amount_vars = LpVariable.dicts("Суми", (Branch, Warehouse), 0)

# Defining Objective Function
prob += lpSum(amount_vars[i][j] * cost[i][j] for (i, j) in routes)

# Constraints
for j in Warehouse:
    prob += lpSum(amount_vars[i][j] for i in Branch) == demand[j]

for i in Branch:
    prob += lpSum(amount_vars[i][j] for j in Warehouse) <= supply[i]

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

print("Общо мили = ", value(prob.objective))
