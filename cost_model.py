import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor

df = pd.read_csv("sample_data.csv")

X = df.drop("cost_to_serve", axis=1)
y = df["cost_to_serve"]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            ["warehouse", "carrier"]
        ),
        (
            "num",
            "passthrough",
            ["order_value", "distance", "weight"]
        )
    ]
)

model = Pipeline([
    ("prep", preprocessor),
    ("xgb", XGBRegressor(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1
    ))
])

model.fit(X, y)

joblib.dump(model, "cts_model.pkl")

print("Model trained and saved!")