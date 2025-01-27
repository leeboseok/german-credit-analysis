from scipy import stats
import pandas as pd

# T-test
# 두 그룹 간에 평균 차이가 있는지 확인하는 통계적 방법

df = pd.read_csv('german_credit.csv')

# 성별에 따른 신용금액 차이 검정
male_loan = df[df['Sex'] == 'male']['Credit amount']
female_loan = df[df['Sex'] == 'female']['Credit amount']

t_stat, p_value = stats.ttest_ind(male_loan, female_loan)

if p_value < 0.05:
    print('성별에 따른 신용금액의 차이가 유의미함.')
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
else:
    print('무의미한 차이')
