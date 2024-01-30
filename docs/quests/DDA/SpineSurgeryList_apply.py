import pandas as pd

get_data = pd.read_csv("docs\data\SpineSurgeryList.csv")
'''
get_data.columns
Index(['Unnamed: 0', '환자ID', 'Large Lymphocyte', 'Location of herniation',
       'ODI', '가족력', '간질성폐질환', '고혈압여부', '과거수술횟수', '당뇨여부', '말초동맥질환여부', '빈혈여부',
       '성별', '스테로이드치료', '신부전여부', '신장', '심혈관질환', '암발병여부', '연령', '우울증여부', '입원기간',
       '입원일자', '종양진행여부', '직업', '체중', '퇴원일자', '헤모글로빈수치', '혈전합병증여부', '환자통증정도',
       '흡연여부', '통증기간(월)', '수술기법', '수술시간', '수술실패여부', '수술일자', '재발여부', '혈액형',
       '전방디스크높이(mm)', '후방디스크높이(mm)', '지방축적도', 'Instability', 'MF + ES',
       'Modic change', 'PI', 'PT', 'Seg Angle(raw)', 'Vaccum disc', '골밀도',
       '디스크단면적', '디스크위치', '척추이동척도', '척추전방위증'],
      dtype='object')
'''
# 시간 변환 함수
def cal_time(num):
    answer = 0
    time = num
    if time >= 60:
        hour = int(time//60)
        min = int(time%60)
        answer = f"{hour}시간 {min}분"
    else:
        try:
            answer = f"{int(time)}분"
        except:
            answer = f""
    return answer

cal_data = get_data[['체중','신장']]    # 체중과 신장 추출
cal_data['BMI'] = cal_data.apply(lambda x: x['체중']/(x['신장']/100)**2, axis=1)    # 시간과 체중으로 BMI설정

operation_time = get_data['수술시간'].apply(cal_time) # 시간 변환
cal_data['수술시간_시간변환'] = operation_time

print(cal_data)