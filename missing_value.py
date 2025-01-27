import seaborn as sns
import matplotlib.pyplot as plt
from value import df, numeric_cols

# 결측치 확인
print("\n 결측치 확인:")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing value Heatmap")
plt.show()

df.fillna(df.mean(), inplace=True)

# 수치형 변수의 이상치 시각화
plt.figure(figsize=(12, 6))
for i, col in enumerate(numeric_cols):
    plt.subplot(1, len(numeric_cols), i+1)
    sns.boxplot(y=df[col])
    plt.title(f"{col} Boxplot")
plt.tight_layout()
plt.show()
