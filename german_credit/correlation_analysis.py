import pandas as pd
from scipy import stats

# 데이터 로드
df = pd.read_csv('german_credit.csv')

# 상관관계 분석
# 변수 간의 관계가 얼마나 강한지 파악하는 데 유용.
# Pearson 상관계수 또는 Spearman 순위 상관계수를 사용하여 연속형 변수 간의 관계를 분석 할 수 있음.
correlation_matrix = df[['Duration', 'Credit amount', 'Age']].corr()

# Pearson 상관계수 확인
for col1 in correlation_matrix.columns:
    for col2 in correlation_matrix.index:
        correlation_value = correlation_matrix.loc[col2, col1]
        
        # 상관계수 값에 따라 출력
        if correlation_value == 1:
            print(f"{col1}와 {col2}는 완전한 양의 상관관계입니다.")
        elif correlation_value == -1:
            print(f"{col1}와 {col2}는 완전한 음의 상관관계입니다.")
        elif correlation_value == 0:
            print(f"{col1}와 {col2}는 상관관계가 없습니다.")
        else:
            print(f"{col1}와 {col2}의 상관계수: {correlation_value}")
