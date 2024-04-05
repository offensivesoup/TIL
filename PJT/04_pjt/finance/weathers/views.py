from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create your views here.
def problem1(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path)
    table = pd.DataFrame(df)
    context = {
        'df': df,
        'table' : table
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    # CSV 파일 경로
    csv_path = 'austin_weather.csv'

    # CSV 파일 읽기
    df = pd.read_csv(csv_path)
    # 'Date' 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    x = df["Date"]
    # 일별 최고, 평균, 최저 온도 계산
    y1, y2, y3 = df['TempHighF'], df['TempAvgF'], df['TempLowF']
    # x_lst = ['2014-01','2014-07','2015-01','2015-07','2016-01','2016-07','2017-01','2017-07']
    # 선 그래프 그리기
    plt.switch_backend('Agg')
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xticks()
    plt.grid()
    plt.legend(['Max Temperature', 'Avg Temperature', 'Min Temperature'], loc='lower center')
    # 그래프를 이미지로 변환하여 HTML에 삽입
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    graph_url = 'data:image/png;base64,{}'.format(graph)

    # 컨텍스트에 그래프 URL 추가
    context = {
        'graph_url': graph_url
    }

    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    # CSV 파일 경로
    csv_path = 'austin_weather.csv'

    # CSV 파일 읽기
    df = pd.read_csv(csv_path)

    # 'Date' 열을 날짜 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])
    # 월별 최고, 평균, 최저 온도의 평균 계산
    monthly_temp = df.groupby(df['Date'].dt.to_period('M')).agg({'TempHighF': 'mean', 'TempAvgF': 'mean', 'TempLowF': 'mean'})
    # 선 그래프 그리기
    x = monthly_temp.index.to_timestamp()
    plt.figure(figsize=(10, 6))
    plt.plot(x,monthly_temp['TempHighF'])
    plt.plot(x,monthly_temp['TempAvgF'])
    plt.plot(x,monthly_temp['TempLowF'])
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(['Max Temperature', 'Avg Temperature', 'Min Temperature'], loc='lower right')
    plt.grid()
    # 그래프를 이미지로 변환하여 HTML에 삽입
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    graph_url = 'data:image/png;base64,{}'.format(graph)

    # 컨텍스트에 그래프 URL 추가
    context = {
        'graph_url': graph_url
    }

    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    # CSV 파일 경로
    csv_path = 'austin_weather.csv'

    # CSV 파일 읽기
    df = pd.read_csv(csv_path)

    # 'Events' 열의 결측치를 빈 문자열로 대체
    df['Events'] = df['Events'].fillna('').astype(str)

    # 'Events' 열을 문자열로 변환하고 각 이벤트를 분할하여 리스트로 저장
    events_list = df['Events'].str.split(',').apply(lambda x: ['No events' if event.strip() == '' else event.strip() for event in x])

    # 모든 이벤트를 하나의 리스트로 펼침
    all_events = [event for sublist in events_list for event in sublist]

    # 이벤트 발생 횟수를 계산하여 Series 생성
    event_counts = pd.Series(all_events).value_counts()
    
    # 히스토그램 그리기
    plt.figure(figsize=(10, 6))
    event_counts.plot(kind='bar')
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.xticks(rotation=360)
    plt.ylabel('Count')
    plt.grid()

    # 그래프를 이미지로 변환하여 HTML에 삽입
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    graph_url = 'data:image/png;base64,{}'.format(graph)

    # 컨텍스트에 그래프 URL 추가
    context = {
        'graph_url': graph_url
    }
    return render(request, 'weathers/problem4.html', context)
