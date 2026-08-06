import pandas as pd
import numpy as np

np.random.seed(42)

rows = 500

df = pd.DataFrame({
    "order_value": np.random.randint(1000, 10000, rows),
    "distance": np.random.randint(10, 2000, rows),
    "weight": np.random.randint(1, 30, rows),
    "warehouse": np.random.choice(
        ["Delhi", "Mumbai", "Bangalore"], rows
    ),
    "carrier": np.random.choice(
        ["BlueDart", "Delhivery", "Ekart"], rows
    )
})

df["cost_to_serve"] = (
    df["distance"] * 0.25 +
    df["weight"] * 15 +
    np.random.randint(50, 300, rows)
)

df.to_csv("sample_data.csv", index=False)

print("Dataset generated successfully!")