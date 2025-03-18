#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimising Government Expenditure using Linear Programming
Author: Jordan Sydney-Darling
Date: May 2024

Description:
This script uses a linear programming approach to allocate government funding efficiently.
It minimizes expenditure while prioritizing critical sectors using a trade-off parameter (α).
"""

import numpy as np
from cvxopt import matrix, solvers
import csv
import time
from tqdm import tqdm  # Progress bar

# Ensure reproducibility
np.random.seed(42)


# Define the trade-off function
def alpha_fun(alpha):
    """
    Compute the trade-off function f(alpha), which dynamically scales priorities.
    """
    k = 45
    x0 = 0.15
    y0 = 7.2249e-8
    return 0.5 / (1 + np.exp(-k * (alpha - x0))) + y0


def solve_optimization_problem(output_filename=None):
    """
    Solves the government budget optimization problem and saves results to a CSV file.
    """

    # Define constraints (Must be explained properly)
    h = matrix([
        1025, -214.187294, -82.314, -45.254, -20.418, -42.364884, -19.692443,
        -19.795027, -19.140675, -32.518044, -13.7, -10.140895, -5.8589, -9.8,
        -8, -5.14354, -7, -3.85546, -3.1, -2.7, -6.193532, -0.971201, -0.8, -1.99
    ])
    G = matrix(0.0, (24, 23))
    G[0, :] = 1
    for i in range(1, 24):
        G[i, i - 1] = -1

    # Allow user to specify output filename
    if output_filename is None:
        output_filename = f"optimization_results_{int(time.time())}.csv"

    # Open CSV file to store results
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        header = ['Alpha', 'Pi1', 'Pi4', 'Objective Value'] + [f'X{i + 1}' for i in range(23)]
        writer.writerow(header)

        # Loop over alpha and pi values with progress tracking
        for alpha in tqdm(np.linspace(0.4, 0.476, 20), desc="Processing Alpha Values"):
            f_alpha = alpha_fun(alpha)

            for pi1 in np.linspace(1, 2, 23):
                for pi4 in np.linspace(1, 2, 23):

                    # Normalize priorities
                    pi = [1] * 23
                    pi[0] = pi1
                    pi[3] = pi4
                    pt = sum(pi)
                    pi = [p / pt + 1 for p in pi]  # Normalization

                    # Define objective function
                    c = matrix([1 - f_alpha * pi[i] for i in range(23)])

                    # Solve LP problem with error handling
                    try:
                        sol = solvers.lp(c, G, h)
                        if sol['status'] == 'optimal':
                            x_values = [x for x in sol['x']]
                            row = [alpha, pi1, pi4, sol['primal objective']] + x_values
                            writer.writerow(row)
                        else:
                            print(f"Solution not found for alpha={alpha}, pi1={pi1}, pi4={pi4}")
                    except Exception as e:
                        print(f"Solver error for alpha={alpha}, pi1={pi1}, pi4={pi4}: {e}")

    print(f"Optimization complete. Results saved to {output_filename}")


# Run the solver
if __name__ == "__main__":
    solve_optimization_problem()
