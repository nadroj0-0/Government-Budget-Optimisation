# Optimising Government Expenditure: A Deterministic Approach to Alleviate the Cost of Living Crisis

## Overview
This project presents a **mathematical optimisation model** for UK government budget allocation. The goal is to **minimise overall government expenditure while prioritising funding for sectors most affected by the cost of living crisis**. The model introduces a trade-off parameter (α) and sector priority coefficients (pᵢ) to balance cost efficiency and sector funding needs.

## Mathematical Model
The problem is formulated as a **linear optimisation model** with:
- **Objective Function:** Minimise total expenditure while ensuring high-priority sectors receive more funding.
- **Constraints:**
  - Total allocated budget ≤ Government revenue.
  - Each sector receives at least its minimum required funding.

The model leverages **a sigmoid trade-off function** to optimise budget allocation dynamically across different government sectors.

## Implementation Details
- **Programming Language:** Python
- **Libraries Used:** NumPy, SciPy, CVXOPT
- **Solver:** The model is solved using a **linear programming approach**.

## Results & Findings
- The model **effectively prioritises sectors like healthcare, housing, and energy**, ensuring an increase in funding where needed.
- Using **α ≈ 0.47**, critical sectors received budget increases of **~£700 million**.
- **Trade-off parameter adjustments** significantly impacted funding allocation dynamics.

## Future Improvements
- Extending the model with **stochastic optimisation** to account for uncertainty in revenue generation.
- Incorporating **machine learning forecasting** for better budget predictions.
- Adding an interactive **visualisation dashboard** for better data interpretation.
