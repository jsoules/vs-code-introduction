def letc(a, s):
    if not check_input_validity(a, s):
        return False
    return len([l for l in s if l == a])

def findc(a, s):
    if not check_input_validity(a, s):
        return False
    n = []
    for i in range(0, len(s)):
        if s[i] != a: continue
        n.append(i)
    return n

def check_input_validity(a, s):
    v = True
    if not isinstance(s, str):
        v = False
    if len(s) == 0:
        v = False
    if not isinstance(a, str):
        v = False
    if len(a) != 1:
        v = False
    return v

if __name__ == '__main__':
    print(letc('a', 'aardvark'))
    print(findc('a', 'aardvark'))
