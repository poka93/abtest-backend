from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from statsmodels.stats.proportion import proportions_ztest

app = FastAPI()


# Data Models
class ZTestData(BaseModel):
    control_group_size: int
    control_group_conversion: float  # Proportion
    treatment_group_size: int
    treatment_group_conversion: float  # Proportion
    alpha: float = 0.05
    alternative: str = "two-sided"  # Other options: "smaller", "larger"


# API Endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the A/B Testing API"}


@app.post("/conversion-hypothesis-testing")
async def conversion_hypothesis_testing(data: ZTestData):
    """
    Perform Z-test for proportions to determine if the difference in conversion rates between two groups is statistically significant.
    """
    if (
        not data.control_group_size > 0
        or not data.control_group_conversion >= 0
        or not data.treatment_group_size > 0
        or not data.control_group_conversion >= 0
    ):
        raise HTTPException(status_code=400, detail="Invalid data")

    control_group_size = data.control_group_size
    control_group_conversion = data.control_group_conversion
    treatment_group_size = data.treatment_group_size
    treatment_group_conversion = data.treatment_group_conversion
    alpha = data.alpha
    alternative = data.alternative

    # Perform Z-test for proportions
    count = [
        control_group_conversion * control_group_size,
        treatment_group_conversion * treatment_group_size,
    ]
    nobs = [control_group_size, treatment_group_size]
    z_stat, p_value = proportions_ztest(count, nobs, alternative=alternative)

    # Determine statistical significance
    statistical_significance = True if p_value < alpha else False

    return {
        "p_value": round(p_value, 4),
        "statistical_significance": statistical_significance,
        "z_stat": round(z_stat, 4),
    }
