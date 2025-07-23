import qrcode
from templates.qrData import QRData
from util import calculate_crc, base64_encode
from models.account_info import AccountInfo
from models.merchant import Merchant
from constants import TransferType, InitMethod

class QRGenerater:
    def __init__(self):
        self.generater = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

    def gen_data_str(self, data: QRData):
        data_str = f'0002{data.format_indicator}0102{data.init_method.value}{data.merchant.account_info}'

        if data.merchant.category_code:
            data_str += f'5204{data.merchant.category_code}'

        data_str += f'5303{data.currency.value}'
        data_str += f'54{len(data.transaction_amount):02}{data.transaction_amount}'

        # if (data.convenience_data):

        data_str += f'5802{data.merchant.account_info.country.value}'

        if data.merchant.account_info.account_name:
            data_str += f'59{len(data.merchant.account_info.account_name):02}{data.merchant.account_info.account_name}'

        if data.merchant.city:
            data_str += f'60{len(data.merchant.city):02}{data.merchant.city}'
        
        if data.merchant.postal_code:
            data_str += f'61{len(data.merchant.postal_code):02}{data.merchant.postal_code}'

        if data.additional_data:
            data_str += data.additional_data.gen_data_for_qr_code()

        data_str += '6304'
        return data_str



    def generate_qr_code_img(self, data: QRData, fill_color="black", back_color="white"):
        data_str = self.gen_data_str(data)
        crc = calculate_crc(data_str)

        # print(data_str)
        # print(crc)

        self.generater.add_data(data_str + crc)
        self.generater.make(fit=True)

        return self.generater.make_image(fill_color=fill_color, back_color=back_color)
    
    def generate_qr_code_base64(self, data: QRData, fill_color="black", back_color="white"):
        img = self.generate_qr_code_img(data, fill_color, back_color)
        return base64_encode(img)

    def save_qr_code(self, file_path):
        # Code to save QR code
        pass

if __name__ == '__main__':
    account_info = AccountInfo(
        bin_code='970422',
        account_number='040204020694'
    )

    # account_info = AccountInfo(
    #     bin_code='momo',
    #     account_number='0961672190',
    #     transfer_type=TransferType.MYQR
    # )

    merchant = Merchant(
        name='DAU VAN GIANG',
        account_info=account_info
    )

    data = QRData(
        init_method=InitMethod.STATIC,
        merchant=merchant,
        transaction_amount='1000'
    )
    qr = QRGenerater()
    # img = qr.generate_qr_code_img(data)
    img_base64 = qr.generate_qr_code_base64(data)
    print(img_base64)
    # img.show()
