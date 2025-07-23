from models.account_info import AccountInfo

class Merchant:
    def __init__(self, name, account_info: AccountInfo, category_code: str=None, city: str=None, postal_code: str = None):
        self.name = name
        self.account_info = account_info
        self.category_code = category_code
        self.city = city
        self.postal_code = postal_code
