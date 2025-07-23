from constants import PaymentSystem
from constants import TransferType
from constants import Country

class AccountInfo:
    def __init__(self, bin_code: str, account_number: str, account_name: str = None, country: Country = Country.VN, payment_sys: PaymentSystem = PaymentSystem.VIETQR, transfer_type: TransferType = TransferType.NAPAS247_QR_TO_ACCOUNT):
        self.payment_sys = payment_sys
        self.bin_code = bin_code
        self.account_name = account_name
        self.account_number = account_number
        self.transfer_type = transfer_type
        self.country = country

    def __str__(self):
        bin_code_str = f'00{len(self.bin_code):02}{self.bin_code}'
        account_number_str = f'01{len(self.account_number):02}{self.account_number}'

        payment_sys_str = f'00{len(self.payment_sys.guid):02}{self.payment_sys.guid}'
        beneficiary_bank_str = f'01{len(bin_code_str + account_number_str):02}{bin_code_str + account_number_str}'
        transfer_type_str = '' if self.transfer_type is None else f'02{len(self.transfer_type.value):02}{self.transfer_type.value}'
        
        final_value = payment_sys_str + beneficiary_bank_str + transfer_type_str
        return f'{self.payment_sys.evmcoId}{len(final_value):02}{final_value}'