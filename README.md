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

## Data Sources
The dataset used in this project consists of **real-world government spending data**, which was cleaned and structured for analysis.

### **Sector Spending Data.csv**
- Contains raw budget data sourced from **official government reports and the ONS (Office for National Statistics)**.
- Includes columns for **sector-wise expenditure, net income, net expenditure, minimum required funding, and actual government budget allocations**.

### **Optimised Results Data.csv**
- Stores the **model-generated optimal budget allocations** based on applied constraints.
- Includes a **comparison column** showing the difference between:
  - **Model minimum budget allocation constraints vs. Model predictions.**
- Useful for understanding how **effectively the model prioritises different sectors**.

## How It Works
1. **Data Processing**: The budget dataset is preprocessed for analysis.
2. **Model Formulation**: A **mathematical optimisation model** is developed to allocate funds efficiently.
3. **Solving the Problem**: The model is executed using Python to compute optimal allocations.
4. **Comparison**: The model’s results are compared with **model-defined constraints**.

## Installation & Usage

### Prerequisites
- You need **Python 3.7 or later** installed.
- Download and install Python from [python.org](https://www.python.org/downloads/) if you don’t have it.

### Installing Required Packages
- Open any Python environment.
- Run this in a new script or interactive window:

  ```python
  pip install -r requirements.txt
  ```
### Running the Model
1. Open **Budget Optimisation Model Solver.py** in your Python environment.
2. Click **Run** .
3. The script will produce an output CSV file containing optimised budget allocations for various parameter values.

### Output File
- The results are saved as **"optimization_results_<timestamp>.csv"**, my results are uploaded inside the **results** folder.
- If needed, you can modify the filename directly inside the script.

## Future Improvements
- Extending the model with **stochastic optimisation** to account for uncertainty in revenue generation.
- Incorporating **machine learning forecasting** for better budget predictions.
- Adding an interactive **visualisation dashboard** for better data interpretation.
