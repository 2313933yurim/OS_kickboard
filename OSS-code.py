from flask import Flask, render_template, jsonify
import requests
import csv
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# 킥보드 주차구역 데이터를 저장할 리스트
kickboard_parking_areas = []

# Traccar 서버 URL
traccar_url = 'http://192.168.219.156:8082/api/positions'  # Traccar 서버의 URL에 맞게 수정

# Traccar 서버의 인증 정보
username = 'hwtree@sookmyung.ac.kr'  # Traccar 서버의 사용자 이름
password = 'hw03024652s!'  # Traccar 서버의 비밀번호

# GPS 데이터 가져오기: 모든 기기의 최신 위치 정보
def fetch_latest_positions():
    try:
        response = requests.get(traccar_url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch GPS data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GPS data: {e}")
        return None

# CSV 파일에서 킥보드 주차 구역 데이터 로드
def load_kickboard_parking_areas():
    try:
        with open('kickboard_parking_areas.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    lat = float(row['latitude'])
                    lng = float(row['longitude'])
                    kickboard_parking_areas.append({
                        'name': row['name'],
                        'lat': lat,
                        'lng': lng
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Error while loading CSV: {e}")

# 메인 페이지 라우트
@app.route('/')
def kickboardParkingAreas_index():
    load_kickboard_parking_areas()  # 킥보드 주차 구역 데이터 로드
    return render_template('kickboardParkingAreas_index.html', kickboard_parking_areas=kickboard_parking_areas)

# API 엔드포인트: 킥보드 주차 구역 데이터 제공
@app.route('/data')
def get_data():
    return jsonify(kickboard_parking_areas)

# API 엔드포인트: 모든 기기의 최신 GPS 데이터 제공
@app.route('/gps_data')
def get_all_gps_data():
    gps_data = fetch_latest_positions()
    if gps_data:
        return jsonify(gps_data)
    else:
        return jsonify({'error': 'Failed to fetch GPS data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
