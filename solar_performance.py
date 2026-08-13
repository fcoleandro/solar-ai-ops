"""
Solar AI Ops
Solar Performance Analyzer

A simple open-source tool for evaluating photovoltaic
system generation against expected generation.
"""

from dataclasses import dataclass


@dataclass
class SolarPlant:
    name: str
    installed_capacity_kwp: float
    expected_generation_kwh: float
    actual_generation_kwh: float


def analyze_performance(plant: SolarPlant) -> dict:
    """Analyze photovoltaic generation performance."""

    if plant.expected_generation_kwh <= 0:
        raise ValueError("Expected generation must be greater than zero.")

    performance = (
        plant.actual_generation_kwh
        / plant.expected_generation_kwh
        * 100
    )

    deficit = max(
        plant.expected_generation_kwh
        - plant.actual_generation_kwh,
        0
    )

    if performance >= 95:
        status = "NORMAL"
        message = "Generation is within the expected range."
    elif performance >= 85:
        status = "ATTENTION"
        message = "Generation is slightly below the expected range."
    elif performance >= 70:
        status = "WARNING"
        message = "Possible underperformance detected."
    else:
        status = "CRITICAL"
        message = "Significant underperformance detected."

    return {
        "plant": plant.name,
        "installed_capacity_kwp": plant.installed_capacity_kwp,
        "expected_generation_kwh": plant.expected_generation_kwh,
        "actual_generation_kwh": plant.actual_generation_kwh,
        "performance_percent": round(performance, 2),
        "generation_deficit_kwh": round(deficit, 2),
        "status": status,
        "message": message,
    }


if __name__ == "__main__":

    example = SolarPlant(
        name="Example Solar Plant",
        installed_capacity_kwp=10.0,
        expected_generation_kwh=1450.0,
        actual_generation_kwh=1180.0,
    )

    result = analyze_performance(example)

    print("\nSolar AI Ops — Performance Analysis\n")

    for key, value in result.items():
        print(f"{key}: {value}")
