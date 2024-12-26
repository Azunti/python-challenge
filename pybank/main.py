import pandas as pd
from pathlib import Path
raw_df = pd.read_csv(Path("../Resources/budget_data.csv"))
raw_df.head()
