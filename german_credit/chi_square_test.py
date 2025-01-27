import pandas as pd
from scipy import stats

# 카이테곱 검정정
# 두 범주형 변수 간의 독립성을 검정하는 방법법

df = pd.read_csv('german_credit.csv')

# Housing과 Risk 간의 카이제곱 검정
contingency_table = pd.crosstab(df['Housing'], df['Risk'])
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

if p_value < 0.05:
    print(f"Chi-squared statistic: {chi2_stat}")
    print(f"P-value: {p_value}")
    print("주택 소유 여부와 신용 위험도 간에 유의미한 관계가 있다고 할 수 있습니다.")
else :
    print("무의미")
