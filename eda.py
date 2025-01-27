import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('german_credit.csv')

# 1. 나이(Age) 열의 평균값
print("1. 나이(Age) 평균값:", df['Age'].mean())

# 2. 직업(Job) 그룹화 후, 대출금액(Credit amount) 평균값 출력
job_group = df.groupby('Job')['Credit amount'].mean()
print("직업(Job)에 따른 대출금액 평균값:" , job_group)

# 3. 'Duration' 범주화 후, 범주별 신용금액 평균값 출력
df['Duration_category'] = pd.cut(df['Duration'], bins=[0, 12, 24, 36, 48, 60, 72],
                                 labels=['0-12', '12-24', '24-36', '36-48', '48-60', '60-72'])
duration_group = df.groupby('Duration_category')['Credit amount'].mean()
print("\n3. 대출기간(Duration) 범주화별 평균값:\n", duration_group)

# 4. 대출 목적(Purpose)별 월 평균 신용금액 시계열 그래프
# 시계열 : 일정 시간 간격으로 배치된 데이터들의 수열
purpose_monthly = df.groupby('Purpose')['Credit amount'].mean()
purpose_monthly.plot(kind='line', title='Average monthly credit amount by loan purpose', ylabel='Average credit amount', xlabel='Purpose')

# 5. 성별(Sex)과 주택 소유 여부(Housing)에 따른 신용금액 상자그림
sns.boxplot(x='Sex', y='Credit amount', hue='Housing', data=df)
plt.title('Credit amount by gender and homeownership')


# 6. 신용금액(Credit amount)과 대출 기간(Duratoin) 상관관계 산점도
sns.scatterplot(x='Duration', y='Credit amount', data=df)
plt.title("Credit amount vs Loan period")
plt.xlabel("Loan period (Duration)")
plt.ylabel("Credit amount (Credit amount)")
plt.show()

# 10. 직업(Job)에 따른 생존율(Survival Rate) 막대 그래프
# job_survival = df.groupby('Job')['Survival Rate'].mean()
# job_survival.plot(kind='bar', title='직업별 생존율')
# plt.ylabel('생존율')
# plt.show()

# 11. RISK 열의 분포 히스토그램
df['Risk'].hist(bins=10, color='skyblue')
plt.title("Distribution of RISK columns")
plt.xlabel("RISK")
plt.ylabel("frequency")
plt.show()

# 12. 나이를 기준으로 대출 목적에 따른 상자그림
sns.boxplot(x='Purpose', y='Age', data=df)
plt.title("Age distribution according to loan purpose")
plt.show()

# 13. 성별과 직업에 따른 대출 기간 평균값 히트맵
sex_job_duration = df.pivot_table(index='Sex', columns='Job', values='Duration', aggfunc='mean')
sns.heatmap(sex_job_duration, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Average loan term by gender and occupation")
plt.show()

# 14. 직업(Job)에 따른 나이 상자그림
sns.boxplot(x='Job', y='Age', data=df)
plt.title("Age distribution by occupation")
plt.show()

# 15. Saving accounts 그룹화 후, 신용금액 평균값 출력
saving_accounts = df.groupby('Saving accounts')['Credit amount'].mean()
print("\n15. Saving accounts 그룹별 평균값:\n", saving_accounts)

# 16. 주택 소유 여부와 대출 목적에 따른 신용금액 히트맵
housing_purpose = df.pivot_table(index='Housing', columns='Purpose', values='Credit amount', aggfunc='mean')
sns.heatmap(housing_purpose, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("Credit amount depending on home ownership and loan purpose")
plt.show()

# 17. Checking account 범주화 후, 대출 기간 평균값 출력
checking_account = df.groupby('Checking account')['Duration'].mean()
print("\n17. Checking account 범주별 대출 기간 평균값:\n", checking_account)

# 18. 성별에 따른 나이 평균값 출력
sex_age_mean = df.groupby('Sex')['Age'].mean()
print("\n18. 성별에 따른 나이 평균값:\n", sex_age_mean)

# 19. 주택 소유 여부에 따른 나이 상자그림
sns.boxplot(x='Housing', y='Age', data=df)
plt.title("Age distribution by homeownership")
plt.show()

# 20. RISK 컬럼에 따른 월 평균 신용금액 막대 그래프
risk_credit_mean = df.groupby('RISK')['Credit amount'].mean()
risk_credit_mean.plot(kind='bar', title='RISK에 따른 월 평균 신용금액')
plt.ylabel('Average credit amount')