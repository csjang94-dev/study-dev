import os.path
import pandas as pd

df = pd.read_csv(os.path.join("./Titanic.csv"))

pd.set_option('display.max_rows', None) # 불러온 데이터 값에서 최대 행 표시 제한 x
pd.set_option('display.max_columns', None) # 불러온 데이터 값에서 최대 열 표시 제한 x
pd.set_option('display.expand_frame_repr', False) # 데이터 출력할 때 행이 길어지면 줄바꿈 x


def change_value(row): # 성별을 판별하기 위해
    if row["Sex"] == "male":
        row["Sex"] = 1
    else:
        row["Sex"] = 0
    return row

df = df.apply(change_value, axis=1)



cnt_male = 0; cnt_female = 0

cnt_male_dead = 0; cnt_female_alive = 0

cnt_class1_dead = 0; cnt_class2_dead = 0; cnt_class3_dead = 0

cnt_nans_dead = 0; cnt_0s_dead = 0; cnt_10s_dead = 0; cnt_20s_dead = 0; cnt_30s_dead = 0
cnt_40s_dead = 0; cnt_50s_dead = 0; cnt_60s_dead = 0; cnt_70s_dead = 0; cnt_80s_dead = 0

cnt_s_dead = 0; cnt_c_dead = 0; cnt_q_dead = 0



for i in df.index:
    if df["Sex"][i] == 1: # 남자인지 확인
        cnt_male += 1
    else: # 여자인지 확인
        cnt_female += 1

    if (df["Sex"][i] == 1) and (df["Survived"][i] == 0): # 남자인 사망자
        cnt_male_dead += 1
    elif (df["Sex"][i] == 0) and (df["Survived"][i] == 1): # 여자인 생존자
        cnt_female_alive += 1

    # 클래스별 사망자 수 추출
    if (df["Pclass"][i] == 1) and (df["Survived"][i] == 0): # 클래스1 사망자
        cnt_class1_dead += 1
    elif (df["Pclass"][i] == 2) and (df["Survived"][i] == 0): # 클래스2 사망자
        cnt_class2_dead += 1
    elif (df["Pclass"][i] == 3) and (df["Survived"][i] == 0): # 클래스3 사망자
        cnt_class3_dead += 1

    # 10단위 나이대별 사망자 수 추출
    if (df["Age"][i] >= 0) and (df["Age"][i] <= 9) and (df["Survived"][i] == 0):
        cnt_0s_dead += 1
    elif (df["Age"][i] >= 10) and (df["Age"][i] <= 19) and (df["Survived"][i] == 0):
        cnt_10s_dead += 1
    elif (df["Age"][i] >= 20) and (df["Age"][i] <= 29) and (df["Survived"][i] == 0):
        cnt_20s_dead += 1
    elif (df["Age"][i] >= 30) and (df["Age"][i] <= 39) and (df["Survived"][i] == 0):
        cnt_30s_dead += 1
    elif (df["Age"][i] >= 40) and (df["Age"][i] <= 49) and (df["Survived"][i] == 0):
        cnt_40s_dead += 1
    elif (df["Age"][i] >= 50) and (df["Age"][i] <= 59) and (df["Survived"][i] == 0):
        cnt_50s_dead += 1
    elif (df["Age"][i] >= 60) and (df["Age"][i] <= 69) and (df["Survived"][i] == 0):
        cnt_60s_dead += 1
    elif (df["Age"][i] >= 70) and (df["Age"][i] <= 79) and (df["Survived"][i] == 0):
        cnt_70s_dead += 1
    elif (df["Age"][i] >= 80) and (df["Age"][i] <= 89) and (df["Survived"][i] == 0):
        cnt_80s_dead += 1
    elif (not (df["Age"][i] >= 0)) and (not (df["Age"][i] <= 100)) and (df["Survived"][i] == 0):
        cnt_nans_dead += 1

    # 정박지별 사망자 수 추출
    if (df["Embarked"][i] == "S") and (df["Survived"][i] == 0):
        cnt_s_dead += 1
    elif (df["Embarked"][i] == "C") and (df["Survived"][i] == 0):
        cnt_c_dead += 1
    elif (df["Embarked"][i] == "Q") and (df["Survived"][i] == 0):
        cnt_q_dead += 1



print(f"탑승자 남성의 총수: {cnt_male}")
print(f"탑승자 여성의 총수: {cnt_female}")

print(f"탑승자 남성과 여성의 비율: 남성[{round(((cnt_male/891)*100),2)}%] / 여성[{round(((cnt_female/891)*100),2)}%]")

print(f"탑승자 남성의 사망자 비율: {round(((cnt_male_dead/cnt_male)*100),2)}%")
print(f"탑승자 여성의 생존자 비율: {round(((cnt_female_alive/cnt_female)*100),2)}%")

print(f"탑승자 0등실별 사망자 비율: 클래스(1)[{round(((cnt_class1_dead/549)*100),2)}%] / "
f"클래스(2)[{round(((cnt_class2_dead/549)*100),2)}%] / 클래스(3)[{round(((cnt_class3_dead/549)*100),2)}%]")

print("탑승자 나이별(10대 단위) 사망자 비율")
print(f"유년기[{round(((cnt_0s_dead/549)*100),2)}%] / 10대[{round(((cnt_10s_dead/549)*100),2)}%] / 20대[{round(((cnt_20s_dead/549)*100),2)}%]")
print(f"30대[{round(((cnt_30s_dead/549)*100),2)}%] / 40대[{round(((cnt_40s_dead/549)*100),2)}%] / 50대[{round(((cnt_50s_dead/549)*100),2)}%]")
print(f"60대[{round(((cnt_60s_dead/549)*100),2)}%] / 70대[{round(((cnt_70s_dead/549)*100),2)}%] / 80대[{round(((cnt_80s_dead/549)*100),2)}%]")
print(f"나이모름[{round(((cnt_nans_dead/549)*100),2)}%]")

print(f"탑승자 Embarked(정박지)별 사망자 비율: 정박지S[{round(((cnt_s_dead/549)*100),2)}%] / "
f"정박지C[{round(((cnt_c_dead/549)*100),2)}%] / 정박지Q[{round(((cnt_q_dead/549)*100),2)}%]")