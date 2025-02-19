from functools import wraps
from typing import get_type_hints

def wypisz_parametry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hints = get_type_hints(func)
        param_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        
        log_data = {
            name: hints.get(name, type(value)).__name__ 
            for name, value in zip(param_names, args)
        }
        log_data.update({name: hints.get(name, type(value)).__name__ for name, value in kwargs.items()})
        
        print(f"{func.__name__} o parametrach: {log_data}")
        return func(*args, **kwargs)
    
    return wrapper

def funkcja_jeden(a: int, b: str, c: float = 3.14):
    return f"Funkcja 1"

def funkcja_dwa(x: float, b: object, c: object = {}, d: bool = False):
    return f"Funkcja 2"

wrapowana_jedynka = wypisz_parametry(funkcja_jeden)

print(wrapowana_jedynka(42, "hello", c=2.71))
print(wrapowana_jedynka(10, "world"))
print(wrapowana_jedynka(a=5, b="test", c=1.23))

wrapowana_dwojka = wypisz_parametry(funkcja_dwa)

print(wrapowana_dwojka(2.13, {"strach"}, {"się"}, True))
print(wrapowana_dwojka(4.44, {"bool"}))
print(wrapowana_dwojka(8.88, {}, {}))