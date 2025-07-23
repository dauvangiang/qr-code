from models.merchant import Merchant
from constants import InitMethod, Currency
from templates.additionalData import AdditionalDataTemplate
from templates.convenienceData import ConvenienceTemplate

class QRData:
    def __init__(self, merchant: Merchant, transaction_amount: str, format_indicator: str = '01', init_method: InitMethod = InitMethod.DYNAMIC, currency: Currency = Currency.VND, additional_data: AdditionalDataTemplate = AdditionalDataTemplate(), convenience_data: ConvenienceTemplate = None):
        self.format_indicator = format_indicator
        self.init_method = init_method
        self.merchant = merchant
        self.currency = currency
        self.transaction_amount = transaction_amount
        self.additional_data = additional_data
        self.convenience_data = convenience_data
