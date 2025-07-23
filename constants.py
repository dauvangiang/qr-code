from enum import Enum

class InitMethod(Enum):
    STATIC = '11'
    DYNAMIC = '12'

class PaymentSystem(Enum):
    VIETQR = ("38", "A000000727", "VietQR / NAPAS")
    UNIONPAY = ("", "", "UnionPay")
    # Các hệ thống khác

    def __init__(self, evmcoId: str, guid: str, label: str):
        self.evmcoId = evmcoId
        self.guid = guid
        self.label = label

class TransferType(Enum):
    NAPAS247_QR_TO_ACCOUNT = "QRIBFTTA"       # Chuyển nhanh NAPAS247 bằng mã QR đến số tài khoản
    NAPAS247_QR_TO_CARD = "QRIBFTTC"      # Chuyển nhanh NAPAS247 bằng mã QR đến thẻ
    MYQR = "MYQR"
    # Các hình thức khác

class Currency(Enum):
    """
    Enum for Transaction Currency Codes
    """
    VND = 704
    USD = 840
    JPY = 392
    CNY = 156

class Country(Enum):
    """
    Enum for Country Codes
    """
    VN = "VN"
    US = "US"

class TipConvenienceIndicator(Enum):
    CUSTOMER_ENTER_TIP = '01'           # Khách hàng nhập tiền tip trên ứng dụng di động
    FIXED_CONVENIENCE_FEE = '02'        # ĐVCNTT thu phí cố định được quy định (convenience_fee_fixed)
    PERCENTAGE_CONVENIENCE_FEE = '03'   # ĐVCNTT thu phí tỷ lệ phần trăm (convenience_fee_percentage)

