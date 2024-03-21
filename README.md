# abtest-backend

## Description

This is a simple AB test backend service. It is an API that provides endpoints to do hypothesis testing, sample size calculation, and other statistical analysis.

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the server locally, run the following command:

```bash
uvicorn main:app --reload
```

## Endpoints

The API provides the following endpoints:

### Hypothesis Testing

- **URL**: `/conversion-hypothesis-testing`
- **Method**: `POST`
- **Request Body**:
  - `control_group_size`: int
  - `control_group_conversion`: int
  - `treatment_group_size`: int
  - `treatment_group_conversion`: int
  - `alpha`: float
  - `alternative`: str
- **Response**:
  - `p_value`: float
  - `statistical_significance`: bool
  - `confidence_interval`: list[float]
- **Description**: This endpoint performs a hypothesis test to compare the conversion rates of two groups. It returns the p-value, statistical significance, confidence interval, and effect size.

### Sample Size Calculation

- **URL**: `/proportion-sample-size-calculation`
- **Method**: `POST`
- **Request Body**:
  - `control_group_conversion`: float
  - `treatment_group_conversion`: float
  - `alpha`: float
  - `beta`: float
  - `alternative`: str
  - `split`: float
- **Response**:
  - `control_group_size`: int
  - `treatment_group_size`: int
  - `total_size`: int
- **Description**: This endpoint calculates the sample size required for a given effect size and significance level.
