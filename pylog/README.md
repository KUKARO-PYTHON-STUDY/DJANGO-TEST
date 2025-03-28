```shell
poetry new pylog
```

- 프로젝트 시작

```shell
poetry add django
```

- django 프로젝트 추가

```shell
django-admin startproject config .
```

- 프로젝트 시작

```shell
python manage.py startapp blog
```

- blog 앱 성성

```shell
python manage.py makemigrations
```

- 마이그레이션을 하면 model이 생성된다, 이걸로 실제 db에 테이블이 생기진 않음

```shell
python manage.py migrate
```

- 실제 db에 변경사항을 적용함

```shell
python manage.py createsuperuser
```

- 슈퍼 유저를 만든다

```shell
python manage.py runserver
```

- 서버를 시작
