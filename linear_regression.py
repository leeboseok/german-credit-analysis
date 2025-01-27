import statsmodels.api as sm
import pandas as pd

# 선형 회귀
# 독립 변수와 종속 변수 간의 관계를 모델링하는 방법
# 독립변수 (Duration) , 종속변수 (Credit amount) 선형 회귀 분석 .

df = pd.read_csv('german_credit.csv')
# 독립 변수와 종속 변수 설정
X = df['Duration']
y = df['Credit amount']

# 상수항 추가
X = sm.add_constant(X)

# 선형 회귀 모델 적합
model = sm.OLS(y, X).fit()

# 결과 출력
print(model.summary())


