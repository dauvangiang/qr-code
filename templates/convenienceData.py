from constants import TipConvenienceIndicator

class ConvenienceTemplate:
    def __init__(self, indicator: TipConvenienceIndicator, tip_or_convenience_fee: str, convenience_fee_fixed: str, convenience_fee_percentage: str):
        self.indicator = indicator
        self.tip_or_convenience_fee = tip_or_convenience_fee
        self.convenience_fee_fixed = convenience_fee_fixed
        self.convenience_fee_percentage = convenience_fee_percentage
