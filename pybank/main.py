import pandas as pd
from pathlib import Path
raw = pd.read_csv(Path("../Resources/budget_data.csv"))
raw.head()

print("Financial Analysis")
print("----------------------------")
months = len(raw['Date'])
print(f"Total Months: {months}")

net = raw['Profit/Losses'].sum()
print(f"Total: ${net}")

aver = raw['Profit/Losses'].mean()
print(f"Average Change: ${aver}")

inpl = raw['Profit/Losses'].max()
inmo = raw.loc[raw['Profit/Losses'].idxmax(), 'Date']
print(f"Greatest Increase in Profits: {inmo} (${inpl})")

depl = raw['Profit/Losses'].min()
demo = raw.loc[raw['Profit/Losses'].idxmin(), 'Date']
print(f"Greatest Decrease in Profits: {demo} (${depl})")
