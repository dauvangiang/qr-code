class Merchant:
    def __init__(self, merchant_name, country, bin_code, account_id, account_type):
        self.merchant_name = merchant_name
        self.country = country
        self.bin_code = bin_code
        self.account_id = account_id
        self.account_type = account_type # Loại tài khoản: 0 - Tài khoản ngân hàng, 1 - Thẻ
