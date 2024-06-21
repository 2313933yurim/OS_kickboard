# OS_kickboard
2312724 김민지 2313655 김혜원 2312705 임도연 2313933 황유림

</br></br></br>
helmet_detection 모듈
---
 - `html 웹 형성`\
  -카메라로 탑승자 이미지 캡쳐
![webp](https://github.com/2313933yurim/OS_kickboard/assets/165886079/1600b9a9-75e2-499f-9924-0a45a5c74a07)   ![webpage](https://github.com/2313933yurim/OS_kickboard/assets/165886079/11b1dd82-30af-4507-b83c-2f74dfeae12d)

 - `Custom Yolov4`\
  -이미지를 데이터로 전환 시 헬멧 착용 여부 인식 가능
![predictions (3)](https://github.com/2313933yurim/OS_kickboard/assets/165886079/838e4973-ad35-4b9d-8c6a-69ae3d1b6668) ![predictions](https://github.com/2313933yurim/OS_kickboard/assets/165886079/c437f1cd-e5d4-48f7-89b5-e8efd55d332e)

GPS기반 전동킥보드 불법주차 감지 모듈
---
 - `구글맵 API로 지도 생성`
```python
folium.Map #Folium 라이브러리를 사용해 지도 객체 초기화
location = [37.5665, 126.978] #서울을 지도의 중심으로 설정
zoom_start = 12 #초기 확대 수준 설정
```
 - `킥보드 주차장을 파란색 마커로 설정`
```python
folium.Marker #Folium 라이브러리로 마커 추가
popup=area['name'] #마커 클릭 시 표시되는 팝업에 주차구역 이름 설정
```
 - `사용자의 위치 트래킹`
```
traccar_url = 'http://192.168.219.156:8082/api/positions'  # Traccar 서버의 URL에 맞게 수정
response = requests.get(traccar_url)  # Traccar 서버의 위치 데이터 요청
return jsonify(gps_data)  #최신 gps 데이터의 형식 변환 후 HTTP 응답으로 반환
```
- `마커 모양 및 색상 변경 + 이벤트 알림 설정`
</br></br></br>
![KakaoTalk_20240621_140219384](https://github.com/2313933yurim/OS_kickboard/assets/165886079/1da276f4-5bae-45fc-a2f4-d019f73c230c)
![KakaoTalk_20240621_140219384_01](https://github.com/2313933yurim/OS_kickboard/assets/165886079/078a1c26-cb91-4613-bcf7-e9ea0f5852fa)
```
gps-marker {  # gps 데이터 위치 마커는 파란색으로 설정
background-color: blue;
parking-area-marker {  # 주차구역 위치 마커는 빨간색으로 설정
background-color: red; 
L.circle([area.lat, area.lng], {  # 반경 100m 주차구역 원 추가
                radius: 100
marker.bindPopup(`Device ID: ${position.deviceId}<br>주차 구역입니다`);  # 주차 구역이 맞다는 이벤트 알림 표시
marker.bindPopup(`Device ID: ${position.deviceId}<br>주차 구역이 아닙니다. 주차 금지!`);  # 주차 구역이 아니라는 이벤트 알림 표시
```
