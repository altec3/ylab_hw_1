from itertools import combinations, combinations_with_replacement
from math import prod


def domain_name(url: str) -> str:
    http = "http://"
    https = "https://"
    www = "www."
    temp: str = ""
    if http in url:
        temp += url.replace(http, "")
    elif https in url:
        temp += url.replace(https, "")
    if www in temp:
        temp = temp.replace(www, "")
        result = temp.split(".")
        return result[0]
    if www in url:
        temp += url.replace(www, "")
    result = temp.split(".")
    return result[0]


def int32_to_ip(int32: int) -> str:
    bytes_count = 4
    bits = []
    ip = []
    # convert integer to binary
    while True:
        bit: int = int32 % 2
        bits.append(bit)
        int32 //= 2
        if len(bits) == 8*bytes_count:
            break
    # convert binary to IP
    for n in range(bytes_count):
        byte: list = bits[8*n: 8*n+8]
        octet = 0
        for num, bit in enumerate(byte):
            octet += bit * 2 ** num
        ip.append(str(octet))
    ip.reverse()
    return ".".join(ip)


def zeros(num: int) -> int:
    i = 1
    result: float = 0
    while num >= i:
        i *= 5
        result += num / i
    return int(result)


def bananas(s: str) -> set:
    result = set()
    target = "banana"
    if target > s:
        return result
    for i in combinations(range(0, len(s)), len(s) - len(target)):
        lst = list(s)
        for j in i:
            lst[j] = '-'
        if [k for k in lst if k != '-'] == list(target):
            result.add(''.join(lst))
    return result


def count_find_num(primes_l: list, limit: int = 500) -> list:
    n = len(primes_l)
    result_comb = []
    result_mult = []
    while True:
        lst_comb = []
        lst_mult = []
        for comb in combinations_with_replacement(primes_l, n):
            if len(set(comb)) == len(set(primes_l)):
                if prod(comb) <= limit:
                    lst_comb.append(comb)
                    lst_mult.append(prod(comb))
        if lst_comb:
            result_comb.extend(lst_comb)
            result_mult.extend(lst_mult)
            n += 1
        else:
            break
    if result_comb:
        return [len(result_comb), max(result_mult)]
    return []
