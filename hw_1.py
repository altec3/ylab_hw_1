from itertools import combinations, combinations_with_replacement
import re
from math import prod


def domain_name(url: str) -> str:
    prefix = r'(https?://)?(www.)?([A-Za-z_0-9-]+).*'
    return re.search(prefix, url).group(3)


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
    result: int = 0
    while num > 0:
        num //= 5
        result += num
    return result


def bananas(s: str) -> set:
    result = set()
    target = "banana"
    if len(target) > len(s):
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


if __name__ == "__main__":
    print(bananas(" banana"))
