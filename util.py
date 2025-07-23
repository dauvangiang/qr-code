import crcmod
import io
import base64

def calculate_crc(data: str):
    '''
    Data phải kết thúc bằng '6304'
    '''
    crc16 = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
    data = data.encode('utf-8')
    crc = crc16(data)
    return format(crc, '04X')

def base64_encode(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")

    # Mã hóa sang base64
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    # print(img_base64)
    return img_base64
