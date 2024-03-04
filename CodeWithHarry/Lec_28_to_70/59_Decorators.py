


def newdiv(func):
    def n(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return n

@newdiv
def div(a,b):
    print(a/b)


div(2,4)