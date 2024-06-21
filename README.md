# OS_kickboard
2312724 김민지 2313655 김혜원 2312705 임도연 2313933 황유림
### 구현 기능
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
icon=folium.Icon(color='red') #빨간색 아이콘으로 마커 표시
```
 - `사용자의 위치 트래킹`\
   사용자가 타고 있는 킥보드의 위치를 파란 마커로 설정
 - `주차 시 마커 모양 변경+알림 전송`\
  -사용자 주차 이벤트 감지 및 서버로 전송\
  -서버에서 주차 이벤트 감지, 지도의 특정 마커의 모양이나 색상 변경, 관련 사용자에게 알림 전송
