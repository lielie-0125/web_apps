import socket

from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index/index.html")


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


def site(request):
    # 获取本地ip地址
    ip = get_ip()

    return HttpResponse("http://" + ip + ":8000/permit")
