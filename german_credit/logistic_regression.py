from sklearn.linear_model import LogisticRegression
import pandas as pd

# 로지스틱 회기
# 이진 분류 문제에 적합함.
# 위험도를 낮은위험 0, 높은위험 1으로 설정하고
# 여러 변수들(Age, Duration, Credit amount 등)을 독립변수로 사용한다.
df = pd.read_csv('german_credit.csv')

# 독립변수(X)와 종속변수(y)
X = df[['Age', 'Duration', 'Credit amount']]
y = df['Risk']

# 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X, y)

# 회귀 계수 출력
coef = model.coef_[0]  # 각 변수의 계수
intercept = model.intercept_[0]  # 절편

# 출력
print("로지스틱 회귀 모델의 회귀 계수 및 절편:")
print(f"Age의 회귀 계수: {coef[0]:.4f}")
print(f"Duration의 회귀 계수: {coef[1]:.4f}")
print(f"Credit amount의 회귀 계수: {coef[2]:.4f}")
print(f"모델의 절편: {intercept:.4f}")

# 추가적으로, 각 변수의 영향력을 설명
print("\n각 변수의 영향력:")
if coef[0] > 0:
    print(f"Age가 증가할수록 높은 위험을 가질 확률이 높아집니다.")
else:
    print(f"Age가 증가할수록 낮은 위험을 가질 확률이 높아집니다.")

if coef[1] > 0:
    print(f"Duration이 증가할수록 높은 위험을 가질 확률이 높아집니다.")
else:
    print(f"Duration이 증가할수록 낮은 위험을 가질 확률이 높아집니다.")

if coef[2] > 0:
    print(f"Credit amount가 증가할수록 높은 위험을 가질 확률이 높아집니다.")
else:
    print(f"Credit amount가 증가할수록 낮은 위험을 가질 확률이 높아집니다.")

# 결과 요약
# Age의 회귀 계수: 나이가 증가할수록 신용 위험이 감소하는 경향이 있습니다. (음수 계수)
# Duration의 회귀 계수: 대출 기간이 길어질수록 신용 위험이 증가하는 경향이 있습니다. (양수 계수)
# Credit amount의 회귀 계수: 대출 금액이 많을수록 신용 위험이 증가하는 경향이 있습니다. (양수 계수)

