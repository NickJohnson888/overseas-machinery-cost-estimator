# config.py

# Fixed parameters and constants for the machinery cost estimation system

# Currency conversion rates
CURRENCY_CONVERSION_RATES = {
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.0
}

# Machinery cost estimates
MACHINERY_COST_ESTIMATES = {
    'excavator': 150000,
    'bulldozer': 120000,
    'crane': 300000,
}

# Operational parameters
OPERATIONAL_PARAMETERS = {
    'daily_hours': 8,
    'weekly_days': 5,
    'monthly_weeks': 4,
}

# Depreciation rates
DEPRECIATION_RATES = {
    'excavator': 0.15,
    'bulldozer': 0.12,
    'crane': 0.10,
}

# Maintenance costs
MAINTENANCE_COSTS = {
    'excavator': 3000,
    'bulldozer': 2500,
    'crane': 5000,
}