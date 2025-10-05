from typing import TypedDict, List, Dict
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel
import numpy as np
import time
import pandas as pd

# 1. TypedDict
class UserTypedDict(TypedDict):
    id: int
    name: str
    age: int
    email: str
    is_active: bool
    roles: List[str]
    profile: Dict[str, str]

# 2. namedtuple
UserNamedTuple = namedtuple(
    "UserNamedTuple",
    [
        "id", "name", "age", "email", "is_active", "roles", "profile"
    ]
)

# 3. dataclass
@dataclass
class UserDataClass:
    id: int
    name: str
    age: int
    email: str
    is_active: bool
    roles: List[str]
    profile: Dict[str, str]

# 4. pydantic
class UserPydantic(BaseModel):
    id: int
    name: str
    age: int
    email: str
    is_active: bool
    roles: List[str]
    profile: Dict[str, str]

# List with numbers
py_list = [10, 20, 30, 40, 50]

# NumPy array
np_array = np.array([10, 20, 30, 40, 50])

# Decorator for timing functions
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def scalar_vector_list(scalar, vector):
    return [scalar * x for x in vector]

@timing_decorator
def scalar_vector_numpy(scalar, vector):
    return scalar * vector

# Test timings
print("List multiplication result:", scalar_vector_list(3, py_list))
print("NumPy multiplication result:", scalar_vector_numpy(3, np_array))

# Load and print CSV
def load_and_print_csv():
    df = pd.read_csv('user.csv')
    print("\nCSV file contents:\n", df)

load_and_print_csv()
