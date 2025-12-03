# Battery Quality Control & Reliability Analysis Project

## Project Overview

This project implements a comprehensive statistical analysis framework for battery quality control and reliability assessment in smartwatch manufacturing. The analysis follows a complete industrial quality management chain from individual product inspection to batch quality assessment and lifetime prediction.

**Core Concept:** Using NASA's battery aging datasets, we simulate a smartwatch battery factory scenario to demonstrate how probability theory and mathematical statistics can be applied to real-world industrial quality problems.

## Key Features

- **End-to-end analysis pipeline** from raw data to decision support
- **Multiple statistical methods** integrated naturally within an industrial context
- **Real NASA battery data** combined with simulated quality metrics
- **Complete visualization** of statistical concepts and results
- **Reproducible research** with modular Python code

## Analysis Framework

### Part 1: Data Description & Random Event Definition
- Descriptive statistics for battery lifetime data
- Histogram visualization and basic statistical measures
- Definition of random events (defective items, lifetime thresholds)

### Part 2: Bayesian Analysis for Quality Tracing
- Application of total probability and Bayes' theorem
- Machine attribution analysis for defective products
- Prior-posterior analysis in quality control context

### Part 3: Lifetime Distribution Modeling
- Weibull distribution fitting for battery lifetimes
- Derivation of charging cycle distributions
- Bivariate analysis (lifetime vs. voltage drop correlation)
- Random variable transformations and function distributions

### Part 4: Batch Quality Statistical Inference
- Sampling distributions for defect rates
- Point estimation (MLE) and interval estimation
- Hypothesis testing for batch acceptance
- Power analysis for quality tests

### Part 5: Lifetime Prediction & Central Limit Theorem
- Law of Large Numbers demonstration
- Central Limit Theorem verification through simulation
- Confidence interval construction for mean lifetime
- Monte Carlo simulations for statistical properties

## Project Structure

```
battery-quality-analysis/
│
├── data/                          # NASA battery datasets
│   └── Battery Data Set/          # Original NASA data files
│
├── utils.py                       # Utility functions and classes
│
├── 1_data_description.ipynb       # Part 1: Data exploration
├── 2_bayesian_analysis.ipynb      # Part 2: Bayesian methods
├── 3_lifetime_distribution.ipynb  # Part 3: Distribution modeling
├── 4_batch_quality.ipynb          # Part 4: Statistical inference
├── 5_clt_demonstration.ipynb      # Part 5: CLT applications
├── 6_comprehensive_analysis.ipynb # Complete workflow
│
├── results/                       # Generated results
│   ├── figures/                   # All visualization outputs
│   └── analysis_results.pkl       # Serialized analysis results
│
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook/Lab

### Environment Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/battery-quality-analysis.git
cd battery-quality-analysis
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Required Packages
- numpy>=1.21.0
- pandas>=1.3.0
- scipy>=1.7.0
- matplotlib>=3.4.0
- jupyter>=1.0.0

## Dataset Information

### Primary Dataset: NASA Battery Aging Dataset
- **Source:** NASA Prognostics Center of Excellence (PCoE)
- **Content:** Li-ion battery charge/discharge cycles under different temperatures
- **Files:** Multiple .mat files (MATLAB format) containing cycle-by-cycle data
- **Key Variables:** Capacity, impedance, temperature, cycle count

### Data Preparation
1. Download the NASA battery dataset from the official repository
2. Extract files to `data/Battery Data Set/` directory
3. The code will automatically load and preprocess the data

## Usage Guide

### Quick Start
1. Ensure NASA data is placed in the correct directory
2. Open Jupyter Notebook:
```bash
jupyter notebook
```
3. Execute notebooks in numerical order (1-6) for complete analysis

### Step-by-Step Execution

1. **Data Loading & Exploration**
```python
# In 1_data_description.ipynb
from utils import BatteryDataLoader
lifetimes, capacities = BatteryDataLoader.extract_lifetimes_from_folder("data/Battery Data Set/1. BatteryAgingARC-FY08Q4")
```

2. **Bayesian Analysis**
```python
# In 2_bayesian_analysis.ipynb
# Simulates production line with two machines
# Calculates posterior probabilities for defect attribution
```

3. **Distribution Modeling**
```python
# In 3_lifetime_distribution.ipynb
from scipy.stats import weibull_min
# Fits Weibull distribution to battery lifetime data
```

4. **Statistical Inference**
```python
# In 4_batch_quality.ipynb
# Performs hypothesis testing on defect rates
# Constructs confidence intervals
```

5. **CLT Demonstration**
```python
# In 5_clt_demonstration.ipynb
# Visualizes Central Limit Theorem through sampling
```

## Expected Outputs

### Generated Visualizations
1. **Lifetime Distribution Histograms** - Shows battery lifespan patterns
2. **Bayesian Prior-Posterior Plots** - Demonstrates belief updating
3. **Weibull Distribution Fits** - Visualizes lifetime modeling
4. **Confidence Interval Plots** - Shows estimation uncertainty
5. **CLT Demonstration Graphs** - Illustrates sampling distributions
6. **Comprehensive Summary Dashboard** - Integrates all results

### Statistical Results
- Estimated Weibull parameters (k, λ)
- Defect rate estimates with confidence intervals
- Hypothesis test decisions (accept/reject)
- Correlation coefficients between variables
- Power analysis for quality tests

## Academic Applications

This project serves as an excellent case study for:
- **Probability & Statistics courses** - Real-world application of theoretical concepts
- **Quality Engineering programs** - Statistical process control demonstration
- **Data Science education** - Complete analytical workflow
- **Industrial Engineering** - Reliability assessment methods

## 🔍 Key Statistical Concepts Demonstrated

### Probability Theory
- Random events and probability calculations
- Total probability and Bayes' theorem
- Random variables and distributions
- Expectation, variance, covariance

### Mathematical Statistics
- Point estimation (MLE, method of moments)
- Interval estimation (confidence intervals)
- Hypothesis testing (proportion tests)
- Sampling distributions
- Law of Large Numbers
- Central Limit Theorem

## Citation & References

### Dataset Citation
```bibtex
@dataset{nasa_battery,
  author = {Saha, B. and Goebel, K.},
  title = {Battery Data Set},
  year = {2007},
  publisher = {NASA Prognostics Data Repository},
  address = {NASA Ames Research Center, Moffett Field, CA}
}
```

### Related Publications
- Saha, B., & Goebel, K. (2007). "Battery Data Set", NASA Prognostics Data Repository
- Original paper methodology based on standard statistical textbooks
- Industrial quality control references from Six Sigma literature

## Contributing

Contributions are welcome! Please feel free to:
1. Report bugs or issues
2. Suggest new features or analyses
3. Submit pull requests with improvements
4. Share additional datasets or applications

## License

This project is released for academic and educational purposes. The NASA datasets are publicly available for research use with proper attribution.

## Acknowledgments

- NASA Prognostics Center of Excellence for the battery datasets
- Contributors to open-source statistical packages in Python
- Academic advisors and colleagues for valuable feedback

## Contact

For questions, suggestions, or collaborations:
- **GitHub Issues:** [Project Repository Issues]
- **Academic Inquiries:** For educational use and adaptations

---

*This project demonstrates how statistical methods can be systematically applied to solve real industrial quality problems, providing both theoretical understanding and practical implementation.*