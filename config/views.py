from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")


def burger_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse("pyburger의 햄버거 목록입니다")
