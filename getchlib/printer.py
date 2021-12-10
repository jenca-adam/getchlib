def _print(a):
    print(a,end='',flush=True)
def print_char(a):
    if a=='\x7f':
        a='\b'
    _print(a)
