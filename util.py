import pandas as pd
from pandas import read_csv

def get_tables(path):
    tables = read_csv(path, sep=':')
    return tables.query("to_be_loaded == 'yes'")
