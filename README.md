# tft_helper

**개요**

손이 느려서 리롤덱을 못하시는 분들을 위해 제작하였습니다.

**사용방법**

1. 구매를 원하는 챔피언을 체크합니다.
2. 자동 리롤을 원한다면 체크합니다.
3. 시작 버튼을 클릭합니다.

**필요설정**

해상도 : 1600 * 900

절대좌표로 이미지 서치, 따라서 게임 화면을 움직여서는 안됨

**필요개선사항**

1. pyautogui : 소프트웨어 내 상대좌표 검색이 가능한가?
2. 속도개선 : 1번에 귀속되어 최소한의 이미지서치로 속도 향상 필요
3. 스레드 사용으로 일시정지 기능 추가 필요
4. 멀티 코어 스레드 환경 구축 => kuda 를 통한 이미지 처리

**현재 진행사항**
현재 그래픽카드가 없어서 kuda 사용 불가능.. 

**개발 잠정 중단**