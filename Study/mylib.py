def pow(x=None , y=2, *args):
    """Function takes two arguments (x, y) and returns x ^ y. By default, y == 2."""

    if x is None:
        return f'\n\nexp() ERROR: the first argument is mandatory. None was given.\n\n'
    elif args != ():
        if str(len(args))[-1] == '1':
            return f'\n\nexp() ERROR: function takes 2 arguments, {len(args)} additional was given.\n\n'
        else:
            return f'\n\nexp() ERROR: function takes 2 arguments, {len(args)} additional were given.\n\n'
    try:
        if (x ** y) % 1 == 0:
            return int(x ** y)
        else:
            return x ** y
    except TypeError:
        if (type(x) not in [int, float]) and (type(y) not in [int, float]):            
            t_x = str(type(x)).replace('<class ', '').replace('>', '')
            t_y = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nexp() ERROR: both arguments have to be \'int\' or \'float\'. Instead, {t_x} and {t_y} were given.\n\n'
        
        elif type(x) not in [int, float]:            
            t = str(type(x)).replace('<class ', '').replace('>', '')
            return f'\n\nexp() ERROR: the first argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'
        
        elif type(y) not in [int, float]:            
            t = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nexp() ERROR: the second argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'
    


def root(x=None, y=2, *args):
    """Function takes two arguments (x, y) and returns ʸ√x. By default, y == 2."""

    if x is None:
        return f'\n\nroot() ERROR: the first argument is mandatory. None was given.\n\n'
    elif args != ():
        if str(len(args))[-1] == '1':
            return f'\n\nroot() ERROR: function takes 2 arguments, {len(args)} additional was given.\n\n'
        else:
            return f'\n\nroot() ERROR: function takes 2 arguments, {len(args)} additional were given.\n\n'
    try:
        if x ** (1 / y) % 1 == 0:
            return int(x ** (1 / y))
        else:
            return x ** (1 / y)
    except TypeError:
        if (type(x) not in [int, float]) and (type(y) not in [int, float]):            
            t_x = str(type(x)).replace('<class ', '').replace('>', '')
            t_y = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: both arguments have to be \'int\' or \'float\'. Instead, {t_x} and {t_y} were given.\n\n'
        
        elif type(x) not in [int, float]:            
            t = str(type(x)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: the first argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'
        
        elif type(y) not in [int, float]:            
            t = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: the second argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'



def distance(x1=None, y1=None, x2=None, y2=None, *args):
    """Function takes four mandatory arguments (x1, y1, x2, y2) and returns the distance between two points."""

    if x1 is None:
        return f'\n\ndistance() ERROR: the first argument (x1) is mandatory. None was given.\n\n'
    if y1 is None:
        return f'\n\ndistance() ERROR: the second argument (y1) is mandatory. None was given.\n\n'
    if x2 is None:
        return f'\n\ndistance() ERROR: the third argument (x2) is mandatory. None was given.\n\n'
    if y2 is None:
        return f'\n\ndistance() ERROR: the fourth argument (y2) is mandatory. None was given.\n\n'
    elif args != ():
        if str(len(args))[-1] == '1':
            return f'\n\ndistance() ERROR: function takes 4 arguments, {len(args)} additional was given.\n\n'
        else:
            return f'\n\ndistance() ERROR: function takes 4 arguments, {len(args)} additional were given.\n\n'
    try:
        if (((x2-x1)**2 + (y2-y1)**2)**0.5) % 1 == 0:
            return int(((x2-x1)**2 + (y2-y1)**2)**0.5)
        else:
            return ((x2-x1)**2 + (y2-y1)**2)**0.5
    except TypeError:
        if (type(x1) not in [int, float]) or (type(y1) not in [int, float]) or (type(x2) not in [int, float]) or (type(y2) not in [int, float]):            
            t_x1 = str(type(x1)).replace('<class ', '').replace('>', '')
            t_y1 = str(type(y1)).replace('<class ', '').replace('>', '')
            t_x2 = str(type(x2)).replace('<class ', '').replace('>', '')
            t_y2 = str(type(y2)).replace('<class ', '').replace('>', '')
            return f'\n\ndistance() ERROR: both arguments have to be \'int\' or \'float\'. Instead, |{t_x1}; {t_y1}; {t_x2}; {t_y2}| were given.\n\n'
    

def mult(x:list, y=1, *args) -> float:
    """Function takes a list and multiplies it's elements. If one of the elements is not \'int\' or \'float\', raises TypeError"""

    if x is None:
        return f'\n\nroot() ERROR: the first argument is mandatory. None was given.\n\n'
    elif args != ():
        if str(len(args))[-1] == '1':
            return f'\n\nroot() ERROR: function takes 2 arguments, {len(args)} additional was given.\n\n'
        else:
            return f'\n\nroot() ERROR: function takes 2 arguments, {len(args)} additional were given.\n\n'
    try:
        if x ** (1 / y) % 1 == 0:
            return int(x ** (1 / y))
        else:
            return x ** (1 / y)
    except TypeError:
        if (type(x) not in [int, float]) and (type(y) not in [int, float]):            
            t_x = str(type(x)).replace('<class ', '').replace('>', '')
            t_y = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: both arguments have to be \'int\' or \'float\'. Instead, {t_x} and {t_y} were given.\n\n'
        
        elif type(x) not in [int, float]:            
            t = str(type(x)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: the first argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'
        
        elif type(y) not in [int, float]:            
            t = str(type(y)).replace('<class ', '').replace('>', '')
            return f'\n\nroot() ERROR: the second argument has to be \'int\' or \'float\'. Instead, {t} was given.\n\n'


def list_prod(numlist, alt=0):
    """Function gets a list of ints or floats and returns their product. If list is empty, returns alt. Alt == 0 by default."""
    if numlist:
        try:    
            prod = 1
            for i in numlist:
                prod *= i
            return prod
        except:
            return 'TypeError: operation unavailible'
    else:
        return alt
def list_gometric_mean(numlist):
    return int(list_prod(numlist=numlist) ** (1/len(numlist))) if not(list_prod(numlist=numlist) ** (1/len(numlist)) % 1) else list_prod(numlist=numlist) ** (1/len(numlist))


def func_check():
    if list_prod([1, 2, 3, 4, 5]) == 120:
        print('Test 1 passed')
    else:
        print('Test 1 failed')
    if list_prod([0.5, 0.25, 0.33]) == 0.04125:
        print('Test 2 passed')
    else:
        print('Test 2 failed')
    if list_prod([0.5, 0.25, 8]) == 1:
        print('Test 3 passed')
    else:
        print('Test 3 failed')
    if list_prod([12, 32, 23, 2332, 0], 12) == 0:
        print('Test 4 passed')
    else:
        print('Test 4 failed')
    if list_prod([], 'Nothing') == 'Nothing':
        print('Test 5 passed')
    else:
        print('Test 5 failed')

print(list_gometric_mean([3, 5, 43, 545, 345]))
