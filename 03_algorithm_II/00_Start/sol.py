print(int(10)) # 10진수
print(10)
print(bin(10)) # 2진법
print(type(bin(10))) # => 주의. 문자열임
print(oct(10)) # 8진법
print(hex(18)) # 16진법

# 16진법을 10진법으로
print(int('F', base = 16))
print(bin(8)[2:].zfill(4))
print(bin(1)[2:].zfill(4)) # 나머지를 0으로 채워준다

for i in range(8): # 원하는 범위 내 숫자의 나열
    print(bin(i)[2:].zfill(4))

for i in range(16):
    print(bin(int(hex(i)[2:], base = 16))[2:].zfill(4))


hex_to_dec = {}
for i in range(16):
    # hex_to_dec[2진법 4비트] : 16진법
    # hex_to_dec[bin(i)[2:].zfill(4)]
    print(f'{i:04b}' ,'f-string')
    hex_to_dec[f'{i:04b}'] = hex(i)[2:].upper() # 대문자
    # hex_to_dec[f'{i:04b}'] = hex(i)[2:].replace('0x', '') # 소문자
print(hex_to_dec)

# 반대로

bin_to_hex = {hex(i).replace('0x','').upper() : f'{i:04b}' for i in range(16)}
print(bin_to_hex)
