N, B = map(int, input().split())
def int_to_base(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    while num:
        num, remainder = divmod(num, base)
        result.append(digits[remainder])
    
    return ''.join(reversed(result))

print(int_to_base(N , B))
