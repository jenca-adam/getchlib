class CtrlKey:
    def __init__(self,code):
        
        if code.upper() not in CTRLI:
            if code not in CTRLS:
                raise LookupError("not a control key")
            self.name=CTRLS[code]
            self.char=code
        else:
            self.char=CTRLI[code.upper()]
            self.name=code.upper()
    def __str__(self):
        return self.char
    def __repr__(self):
        return self.name
    def __eq__(self,t):
        if isinstance(t,str):
            return t==self.char or t.upper()==self.name
        elif isinstance(t,self.__class__):
            return t.char==self.char and t.name.upper() == self.name
        
def parse_key(key):
    if key in CTRLS:
        key=CtrlKey(CTRLS[key])
    return key
CTRLS={}
CTRLI={}
CTRLIN={}
for __h in range(1,27):
    if __h not in {9,10}:
        CTRLS[chr(__h)]='CTRL-'+chr(__h+64)
        CTRLI['CTRL-'+chr(__h+64)]=chr(__h)
    CTRLIN['CTRL-'+chr(__h+64)]=chr(__h)
for __a in range(97,123):
    CTRLS['\x1b'+chr(__a)]='ALT-'+chr(__a).upper()
    CTRLI['ALT-'+chr(__a).upper()]='\x1b'+chr(__a)
    CTRLIN['ALT-'+chr(__a).upper()]='\x1b'+chr(__a)


