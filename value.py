import pandas as pd

data_path = "german_credit.csv"
df = pd.read_csv(data_path)

# 데이터 구조 및 기본 정보 확인
print(df.info())
print(df.head())
print(df.describe())

# 1. 데이터 요약 : 데이터 타입에 따른 통계
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
categorical_cols = df.select_dtypes(include=["object", "category"]).columns
print("\n수치형 변수 통계 요약:")
print(df[numeric_cols].describe())

print("\n범주형 변수 고유값 및 빈도수 요약:")
for col in categorical_cols:
    print(f"\n[col] 고유값:")
    print(df[col].value_counts())

    