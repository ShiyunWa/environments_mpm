import pandas as pd
from envtest import show_dataframe


csv_data = """
Name,Age,Occupation
Alice,28,Engineer
Bob,22,Data Scientist
Charlie,30,Designer
David,35,Manager
"""

with open("sample_data.csv", "w") as f:
    f.write(csv_data)

show_dataframe("sample_data.csv")

import os
os.remove("sample_data.csv")
