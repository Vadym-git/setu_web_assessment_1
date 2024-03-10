from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html")


def about_me(request):
    return render(request, "about-me.html")


def contact_us(request):
    return render(request, "contact-us.html")


def project(request, project_id):
    data = [["img/simple_coin_info.png", "Crypto Coin Info",
             "https://play.google.com/store/apps/details?id=ie.mvo.simplecryptocoininfo"],
            ["img/mvo.png", "MVO Website", "https://mvo.ie/"]]
    context = {"img": data[project_id][0], "title": data[project_id][1], "link": data[project_id][2]}
    return render(request, "project.html", context)
