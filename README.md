"# DJANGO-TEST" 
```shell
poetry new django-test
```
* 프로젝트 시작

```shell
python manage.py runserver  
```
* 테스트 용으로 서버 시작할 때는 위 처럼 명령어를 입력한다

```shell
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000
```
* gunicorn(wsgi)로 서버 동작시킬때는 위 처럼 한다

```shell
poetry shell
```
* 실행전에 가상환경 실행하려면 이 명령어 해야한다

```shell
poetry run python manage.py collectstatic --noinput
```
* 정적파일 없는 경우 이거 해주면된다