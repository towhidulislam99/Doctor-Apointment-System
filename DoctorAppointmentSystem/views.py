from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(requset):
    return render(requset, 'admin/role.html')