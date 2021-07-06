def letc(a, s):
    v = True
    if not isinstance(s, str):
        v = False
    if len(s) == 0:
        v = False
    if not isinstance(a, str):
        v = False
    if len(a) != 1:
        v = False
    if not v:
        return False
    return len([l for l in s if l == a])

def findc(a, s):
    v = True
    if not isinstance(s, str):
        v = False
    if len(s) == 0:
        v = False
    if not isinstance(a, str):
        v = False
    if len(a) != 1:
        v = False
    if not v:
        return False
    n = []
    for i in range(0, len(s)):
        if s[i] != a: continue
        n.append(i)
    return n

if __name__ == '__main__':
    print(letc('a', 'aardvark'))
    print(findc('a', 'aardvark'))
