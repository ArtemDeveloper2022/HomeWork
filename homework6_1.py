def bin_or_int (n, m):
    if m == 'bin':
        binary = ""
        while n > 0:
            s1 = str(int(n % 2))
            binary = binary + s1
            n /= 2
            result = binary[::-1]
        result = result.lstrip('0')
        return result
    elif m == 'int':
        n = str(n)
        leng = len(n)
        n = n[::-1]

        print(n)
q = bin_or_int(10110, 'int')

print(q)