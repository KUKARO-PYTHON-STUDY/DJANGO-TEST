from django.http import HttpRequest, HttpResponse


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")
