import sys
sys.stdin = open('input.txt')

'''
네트워크에 연결된 컴퓨터들은 각 ip주소가 있음
이런 컴퓨터가 여러개 모여서 네트워크를 구성함
네트우크 주소와 네트워크 마스크라는 두개의 정보로 표현

주소를 2진수로 이해하면 된다. => 각각의 바이트를 8자로 이진수로 나타내고, 이를 네개 붙여놓은 32자리의 이진수
194.85.160.177
=> 2진수 8자리 * 4개
=> 2진수 32자리
IP는 기본적으로 2^m개의 컴퓨터가 할당
그럼 거꾸로 2^16개의 컴퓨터가 할당되려면
네트워크 주소 : 앞에 32-16 자리가 임의의 수로 구성, 나머지는 0
네트워크 마스크 : 앞에 32-16 자리가 1로 구성 뒤의 m은 0으로 채워짐
이와같은 IP 네트워크에는 앞의 32자리가 네트워크 주소와 일치하는 모든 IP가 포함
=> 어떤 네트워크의 IP 주소들이 주어졌을 때, 네트워크 주소와 마스크를 구해내는 프로그ㅐㅁ
최대 1000개의 컴퓨터
'''

n = int(input())
ips = [list(input().split('.')) for _ in range(n)]
address = []
mask = []
for i in range(4):
    mini = int(ips[0][i])
    maxi = int(ips[0][i])
    for ip in ips:
        if maxi < int(ip[i]):
            maxi = int(ip[i])
        elif mini > int(ip[i]):
            mini = int(ip[i])
    if 255 == 256 + (~maxi^mini):
        mask.append(255)
    else:
        for j in range(9):
            if -(~maxi^mini) <= 1 <<j:
                mask.append(256-(1<<j))
                for k in range(3):
                    mask.append(0)
                break
    address.append(int(ips[0][i])&mask[i])
mask = mask[:4]
print(f'{address[0]}.{address[1]}.{address[2]}.{address[3]}')
print(f'{mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}')
