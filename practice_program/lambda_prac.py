names = ['Supreme', 'rahul', 'aayam']

list(map(lambda x: x.upper(), names))

list(map(lambda x: x.upper(), names))

def rev_name(name):
    y = name.split()
    rev = y[::-1]
    return"".join(rev)