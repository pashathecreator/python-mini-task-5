from typing import Callable
from dataclasses import dataclass

@dataclass
class Vector2D:
    x: int
    y: int

def dot_product(v1: Vector2D, v2: Vector2D):
    return v1.x * v2.x + v1.y * v2.y

def sum(x: int, y: int) -> int:
    return x + y

def multiply(x: int, y: int, z: int):
    return x * y * z

def some_calculation(a, b, c, d=4, e=5):
    return (a + b + c) * d - e


def specialize(f: Callable, *args, **kwargs):
    def specialized_function(*more_args, **more_kwargs):
        combined_args = args + more_args
        combined_kwargs = {**kwargs, **more_kwargs}
        return f(*combined_args, **combined_kwargs)
    return specialized_function

    
    
