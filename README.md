# jekyll_import_tistory
## 이 프로젝트의 정체
티스토리의 백업.xml을 정적 사이트 생성기 jekyll의 형식에 맞게 변환시켜주는 프로그램입니다.
사용법은 아래의 영상참고해주세요.

[![USAGE_VIDEO](http://img.youtube.com/vi/JCnGesYO-Co/0.jpg)](http://www.youtube.com/watch?v=JCnGesYO-Co)

### 설치법

```bash
pip install jekyll_import_tistory
````

##주의
- Python으로 작성되었습니다. Ruby가 아님!!
- 최소한만 만들었습니다. 만들다가 다른게 하고 싶어져서요.
- 티스토리에 업로드한 동영상은 가져올 수 없습니다.
- 발 영어 주의
- 발 영상 주의


## 왜 만들었나?
- 군대를 앞두고 내가 Python을 그래도 할줄은 안다는것을 남기고 싶었다.
  - 적당한 소재 (아무도 아직 시도하지 않은 적당한 난이도의 문제)
  - PyPi 업로드경험 삼아. (setup.py 사용 경험도 포함)
  - 정규표현식 연습
  - Click 사용이지만, CLI 사용 프로그램 연습.
  - Requests 사용이지만, 네트워크에서 원하는걸 요청해서 가져올 수 있다는 것을 연습.
  - BeautifulSoup 사용이지만, DOM 파싱, 크롤링 비슷한것을 연습.
