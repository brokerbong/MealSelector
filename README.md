# 점심 메뉴 맨날 선택하기 귀찮아서 홈페이지 만들기


#### 라이브러리
 - python 3.13
 - Flask -> `web server`
 - Jinja2 -> `web component 구조 만들기 위한 라이브러리`


#### Data Storage
- Postgresql
- S3

#### CSS
 - Bulma ` https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css `
   - https://bulma.io/
   - https://github.com/app-generator/flask-bulma-css/tree/master

#### 생각나는 기능
- 메뉴선택 글 마다 수정, 삭제 비밀번호 db저장 -> password coulmm?
- Flask가 비동기작업에 취약함.. lambda로 백그라운드용 fastApi 구현..?

#### 메모
> 객체형 DB
> 
> auto number 가게 id and 주소지 정보 , 가게 메뉴 multi 선택
> 
>> 메뉴 code, 가게 code, 상위메뉴 code, 가격, multi 여부
> 
> 리뷰 백터디비 사용 -> `2차?`


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
  - \_\_init\_\_.py `#`
  - notice.py `#`
- models/ `데이터베이스 모델 관리`
  - \_\_init\_\_.py `#`
  - notice.py `#`
- database.py `# DB 연결 및 설정`

  ------------
  #### 참고
  1. `https://flask.palletsprojects.com/en/stable/`
  2. jinja `https://flask.palletsprojects.com/en/stable/templating/#jinja-setup`
  3. lifecycle `https://flask.palletsprojects.com/en/stable/lifecycle/`
  4. async `https://flask.palletsprojects.com/en/stable/async-await/`
