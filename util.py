import crcmod
from Merchant import Merchant
from constant.Currency import Currency
from constant.Country import Country

def gen_qr_data(merchant: Merchant, currency: Currency, transaction_amount: str, country: Country, add_data: str):
    service_id = 38  # VietQR/Napas
    service_guid = "A000000727"
    receiver_id_type = "QRIBFTTA" if merchant.account_type == 0 else "QRIBFTTC"

    bank_info = f"00{len(merchant.bin_code)}01{len(merchant.account_id)}{merchant.account_id}"
    merchant_account_info = f"00{len(service_guid)}{service_guid}01{len(bank_info)}{bank_info}02{len(receiver_id_type)}{receiver_id_type}"

    '''
    Cấu trúc: [ID][Length][Value]
    - 000201: Bắt buộc cho QR Code (id: 00, length: 02, value: 01)
    - 010212: QR động cho từng giao dịch (id: 01, length: 02, value: 12 (11 cho qr cố định))
    '''
    data = (
        f'000201010212'
        f'{service_id}{len(merchant_account_info)}{merchant_account_info}'
        f'5303{currency.value}'
        f'54{len(transaction_amount)}{transaction_amount}'
        f'5802{len(merchant.country)}{merchant.country}'
        f'620808{len(add_data)}{add_data}'
        f'6304'
    )
    crc = calculate_crc(data)
    return f'{data}{crc}'

def calculate_crc(data):
    crc16 = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
    # Phần QR code đầu vào phải bao gồm "6304" ở cuối
    data = data.encode('utf-8')
    crc = crc16(data)
    return format(crc, '04X')


# data = "00020101021238560010A0000007270138000697042201120402040206940208QRIBFTTA5303704540410005802VN5913DAU VAN GIANG62080804TEST6304"
# print(calculate_crc(data))