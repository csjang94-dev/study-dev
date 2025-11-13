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

cnt_class1 = 0; cnt_class2 = 0; cnt_class3 = 0
cnt_class1_dead = 0; cnt_class2_dead = 0; cnt_class3_dead = 0

cnt_nans = 0; cnt_0s = 0; cnt_10s = 0; cnt_20s = 0; cnt_30s = 0
cnt_40s = 0; cnt_50s = 0; cnt_60s = 0; cnt_70s = 0; cnt_80s = 0
cnt_nans_dead = 0; cnt_0s_dead = 0; cnt_10s_dead = 0; cnt_20s_dead = 0; cnt_30s_dead = 0
cnt_40s_dead = 0; cnt_50s_dead = 0; cnt_60s_dead = 0; cnt_70s_dead = 0; cnt_80s_dead = 0

cnt_s = 0; cnt_c = 0; cnt_q = 0
cnt_s_dead = 0; cnt_c_dead = 0; cnt_q_dead = 0

for i in df.index:
    if df["Sex"][i] == 1:            # 남자인지 확인
        cnt_male += 1
        if df["Survived"][i] == 0:
            cnt_male_dead += 1       # 사망자 확인
    else:                            # 여자인지 확인
        cnt_female += 1
        if df["Survived"][i] == 1:
            cnt_female_alive += 1    # 생존자 확인

    # 클래스별 사망자 수 추출
    if df["Pclass"][i] == 1:
        cnt_class1 += 1             # 클래스1에 속한 사람 수
        if df["Survived"][i] == 0:
            cnt_class1_dead += 1    # 클래스1 사망자
    elif df["Pclass"][i] == 2:
        cnt_class2 += 1             # 클래스2에 속한 사람 수
        if df["Survived"][i] == 0:
            cnt_class2_dead += 1    # 클래스2 사망자
    else:
        cnt_class3 += 1             # 클래스3에 속한 사람 수
        if df["Survived"][i] == 0:
            cnt_class3_dead += 1    # 클래스3 사망자

    # 10단위 나이대별 사망자 수 추출
    if (df["Age"][i] >= 0) and (df["Age"][i] <= 9):
        cnt_0s += 1
        if df["Survived"][i] == 0:
            cnt_0s_dead += 1
    elif (df["Age"][i] >= 10) and (df["Age"][i] <= 19):
        cnt_10s += 1
        if df["Survived"][i] == 0:
            cnt_10s_dead += 1
    elif (df["Age"][i] >= 20) and (df["Age"][i] <= 29):
        cnt_20s += 1
        if df["Survived"][i] == 0:
            cnt_20s_dead += 1
    elif (df["Age"][i] >= 30) and (df["Age"][i] <= 39):
        cnt_30s += 1
        if df["Survived"][i] == 0:
            cnt_30s_dead += 1
    elif (df["Age"][i] >= 40) and (df["Age"][i] <= 49):
        cnt_40s += 1
        if df["Survived"][i] == 0:
            cnt_40s_dead += 1
    elif (df["Age"][i] >= 50) and (df["Age"][i] <= 59):
        cnt_50s += 1
        if df["Survived"][i] == 0:
            cnt_50s_dead += 1
    elif (df["Age"][i] >= 60) and (df["Age"][i] <= 69):
        cnt_60s += 1
        if df["Survived"][i] == 0:
            cnt_60s_dead += 1
    elif (df["Age"][i] >= 70) and (df["Age"][i] <= 79):
        cnt_70s += 1
        if df["Survived"][i] == 0:
            cnt_70s_dead += 1
    elif (df["Age"][i] >= 80) and (df["Age"][i] <= 89):
        cnt_80s += 1
        if df["Survived"][i] == 0:
            cnt_80s_dead += 1
    else:
        cnt_nans += 1
        if df["Survived"][i] == 0:
            cnt_nans_dead += 1

    # 정박지별 사망자 수 추출
    if df["Embarked"][i] == "S":
        cnt_s += 1
        if df["Survived"][i] == 0:
            cnt_s_dead += 1
    elif df["Embarked"][i] == "C":
        cnt_c += 1
        if df["Survived"][i] == 0:
            cnt_c_dead += 1
    else:
        cnt_q += 1
        if df["Survived"][i] == 0:
            cnt_q_dead += 1

print(f"탑승자 남성의 총수: {cnt_male}")
print(f"탑승자 여성의 총수: {cnt_female}")
print(f"탑승자 남성과 여성의 비율: 남성[{round(((cnt_male/891)*100),2)}%] / 여성[{round(((cnt_female/891)*100),2)}%]")
print(f"탑승자 남성의 사망자 비율: {round(((cnt_male_dead/cnt_male)*100),2)}%")
print(f"탑승자 여성의 생존자 비율: {round(((cnt_female_alive/cnt_female)*100),2)}%")

print(f"탑승자 0등실별 사망자 비율: 클래스(1)[{round(((cnt_class1_dead/cnt_class1)*100),2)}%] / "
      f"클래스(2)[{round(((cnt_class2_dead/cnt_class2)*100),2)}%] / 클래스(3)[{round(((cnt_class3_dead/cnt_class3)*100),2)}%]")

print("탑승자 나이별(10대 단위) 사망자 비율")
print(f"유년기[{round(((cnt_0s_dead/cnt_0s)*100),2)}%] / 10대[{round(((cnt_10s_dead/cnt_10s)*100),2)}%] / 20대[{round(((cnt_20s_dead/cnt_20s)*100),2)}%]")
print(f"30대[{round(((cnt_30s_dead/cnt_30s)*100),2)}%] / 40대[{round(((cnt_40s_dead/cnt_40s)*100),2)}%] / 50대[{round(((cnt_50s_dead/cnt_50s)*100),2)}%]")
print(f"60대[{round(((cnt_60s_dead/cnt_60s)*100),2)}%] / 70대[{round(((cnt_70s_dead/cnt_70s)*100),2)}%] / 80대[{round(((cnt_80s_dead/cnt_80s)*100),2)}%]")
print(f"나이모름[{round(((cnt_nans_dead/cnt_nans)*100),2)}%]")

print(f"탑승자 Embarked(정박지)별 사망자 비율: 정박지S[{round(((cnt_s_dead/cnt_s)*100),2)}%] / "
      f"정박지C[{round(((cnt_c_dead/cnt_c)*100),2)}%] / 정박지Q[{round(((cnt_q_dead/cnt_q)*100),2)}%]")




