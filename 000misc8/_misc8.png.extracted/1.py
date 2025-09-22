import zlib
import binascii

id=""
result = binascii.unhexlify(id)
print("2进制",result)
result = zlib.decompress(result)
print(result)


