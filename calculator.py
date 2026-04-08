import config

class MachineryCostCalculator:
    def __init__(self, 
                 equipment_value: float, 
                 freight_and_customs: float, 
                 depreciation_years: int, 
                 fuel_consumption_per_shift: float, 
                 fuel_unit_price: float):
        
        if depreciation_years <= 0:
            raise ValueError("Depreciation years must be greater than 0.")
            
        self.equipment_value = equipment_value
        self.freight_and_customs = freight_and_customs
        self.depreciation_years = depreciation_years
        self.fuel_consumption_per_shift = fuel_consumption_per_shift
        self.fuel_unit_price = fuel_unit_price

    def calc_depreciation_per_shift(self) -> float:
        total_landed_value = self.equipment_value + self.freight_and_customs
        salvage_factor = 1 - config.DEFAULT_RESIDUAL_VALUE_RATE
        total_working_days = self.depreciation_years * config.DEFAULT_ANNUAL_WORKING_DAYS
        return (total_landed_value * salvage_factor) / total_working_days

    def calc_maintenance_per_shift(self) -> float:
        base_depreciation = self.calc_depreciation_per_shift()
        repair_rates = config.MAJOR_REPAIR_RATE + config.ROUTINE_REPAIR_RATE
        return base_depreciation * repair_rates * config.OVERSEAS_MAINTENANCE_COEFFICIENT

    def calc_first_category_costs(self) -> float:
        return self.calc_depreciation_per_shift() + self.calc_maintenance_per_shift()

    def calc_second_category_costs(self) -> float:
        fuel_cost = self.fuel_consumption_per_shift * self.fuel_unit_price
        return fuel_cost + config.DAILY_OPERATOR_COST_USD

    def calc_total_shift_cost(self) -> float:
        return self.calc_first_category_costs() + self.calc_second_category_costs()

    def calc_hourly_rate(self) -> float:
        return self.calc_total_shift_cost() / config.HOURS_PER_SHIFT
