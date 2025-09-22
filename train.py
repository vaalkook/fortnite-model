from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path("Fortnite Statistics.csv"))

def classify_style(row):
    if row["Damage to Players"] > row["Damage to Structures"] and row["Damage to Players"] > row["Materials Used"]:
        return "agresivo"
    elif row["Materials Used"] > row["Damage to Players"]:
        return "constructor"
    else:
        return "defensivo"

df["playstyle"] = df.apply(classify_style, axis=1)

X = df[["Materials Gathered", "Materials Used", "Damage to Structures", "Damage to Players"]]
y = df["playstyle"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Entrenando modelo...")
clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)
clf.fit(X_train, y_train)

print("Guardando modelo...")
dump(clf, pathlib.Path("model/fortnite-style.joblib"))
