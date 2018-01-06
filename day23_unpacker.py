import sys

packed_file = bytearray(open("onlyperl.com", "rb").read())

#Unpack
for i in range(0x1a, 0x1a + 0x30e):
	packed_file[i] ^= 0x4d

#Disable unpacking
packed_file[0x12] = 0x00

open("onlyperl_unpacked.com", "wb").write(packed_file)