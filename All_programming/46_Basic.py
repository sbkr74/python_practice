# # read img and find resolution
# def img_dim(image):
#     with open(image,'rb') as img_file:
#         img_file.seek(163)
#         a = img_file.read(2)
#         height = (a[0] << 8) + a[1]
#         a = img_file.read(2)
#         width = (a[0] << 8) + a[1]
#     print("resolution:",width,"X",height)
# img_dim("All_programming\java.JPG")
# =========================================================================
def img_dim(image):
    with open(image, 'rb') as img_file:
        img_file.read(2)  # Skip the first two bytes (JPEG header)
        
        while True:
            marker, code, length = img_file.read(1), img_file.read(1), img_file.read(2)
            if marker != b'\xff':
                raise ValueError('Invalid JPEG file')
            code = ord(code)
            length = int.from_bytes(length, byteorder='big') - 2
            if 0xc0 <= code <= 0xcf and code != 0xc4 and code != 0xcc:
                img_file.read(1)  # Precision
                height = int.from_bytes(img_file.read(2), byteorder='big')
                width = int.from_bytes(img_file.read(2), byteorder='big')
                print(f"resolution: {width} X {height}")
                return
            else:
                img_file.read(length)

img_dim("All_programming/java.JPG")
