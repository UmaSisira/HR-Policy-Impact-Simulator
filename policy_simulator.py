import pandas as pd

df = pd.read_csv("data/policy_data.csv")

df['RetentionImpact'] = df['PolicyScore'] * 0.2 - df['WorkloadIncrease'] * 0.1
df.to_csv("data/policy_simulation_result.csv", index=False)
