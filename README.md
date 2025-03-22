# 점심 메뉴 맨날 선택하기 귀찮아서 홈페이지 만들기

#### 라이브러리
python 3.13
Flask -> web server
Jinja2 -> web component 구조 만들기 위한 라이브러리
Data Storage
MySQL
S3

#### 생각나는 기능
메뉴선택 글 마다 수정, 삭제 비밀번호 db저장 -> password coulmm?

#### 메모
> 객체지향 데이터베이스로 만들기?
> 
> auto number 가게 정보
> 
> 가게 메뉴 multi 선택
> 
>> 메뉴 code, 가게 code, 상위메뉴 code, 가격, multi 여부
> 
> 리뷰 백터디비 사용
> 
> 홈페이지에서 메뉴 추가하기 기능 UI 어떻게 할지 생각..

#### Structure
mealSelector/
- app.py Flask `메인 파일`
- config.py `설정 파일`
 - requirements.txt `패키지 목록`
- Profile `실행파일`
- static/ `CSS, JS 저장`
- templates/ `HTML 템플릿 저장`
 - base.html `#`
 - index.html `#`
 - notice/ `#`
  - list.html `#`
  - detail.html `#`
- views/ `Blueprint 기반 라우팅 관리`
 - __init__.py `#`
 - notice.py `#`
- models/ `데이터베이스 모델 관리`
 - __init__.py `#`
 - notice.py `#`
- database.py `# DB 연결 및 설정`
