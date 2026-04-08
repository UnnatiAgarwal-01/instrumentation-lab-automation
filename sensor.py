#sensor simulation
import random

def get_temperature():
    return round(random.uniform(20, 100), 2)

def get_pressure():
    return round(random.uniform(1, 10), 2)

def get_flow():
    return round(random.uniform(10, 50), 2)