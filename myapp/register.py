from django.shortcuts import render
from django.views.decorators import csrf


def register(request):
    infomation = {}
    student = request.POST
    if student:
        infomation['rtl'] = student['stu_name']
    return render(request, "home.html", infomation)
