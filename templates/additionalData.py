
class AdditionalDataTemplate:
    '''
    Để nhắc người dùng nhập bất kỳ trường thông tin nào, truyền vào giá trị: '***'. Ví dụ: purpose='***' => Nhắc người dùng nhập nội dung chuyển khoản
    '''
    def __init__(self, bill_number: str = None, mobile_number: str = None, store_label: str = None, loyalty_number: str = None, ref_label: str = None, customer_label: str = None, terminal_label: str = None, add_consumer_data: str = None, purpose: str = "Thanh toan hoa don"):
        self.bill_number = bill_number
        self.mobile_number = mobile_number
        self.store_label = store_label
        self.loyalty_number = loyalty_number
        self.ref_label = ref_label
        self.customer_label = customer_label
        self.terminal_label = terminal_label
        self.purpose = purpose
        self.add_consumer_data = add_consumer_data

    def gen_data_for_qr_code(self):
        data = ''
        if self.bill_number:
            data += f'01{len(self.bill_number):02}{self.bill_number}'
        if self.mobile_number:
            data += f'02{len(self.mobile_number):02}{self.mobile_number}'
        if self.store_label:
            data += f'03{len(self.store_label):02}{self.store_label}'
        if self.loyalty_number:
            data += f'04{len(self.loyalty_number):02}{self.loyalty_number}'
        if self.ref_label:
            data += f'05{len(self.ref_label):02}{self.ref_label}'
        if self.customer_label:
            data += f'06{len(self.customer_label):02}{self.customer_label}'
        if self.terminal_label:
            data += f'07{len(self.terminal_label):02}{self.terminal_label}'
        if self.purpose:
            data += f'08{len(self.purpose):02}{self.purpose}'
        if self.add_consumer_data:
            data += f'09{len(self.add_consumer_data):02}{self.add_consumer_data}'

        if (len(data) == 0):
            return ''
        return f'62{len(data):02}{data}'