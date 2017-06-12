from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# Create your views here.


def login(request):
    return render(request, 'user/login.html')


def validate_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if models.validate(username, password):
        return HttpResponseRedirect('/user/list_name/')

    else:
        context = {'username': username, 'password': password,
                   'error': 'user and name not rightttttt'}
        return render(request, 'user/login.html', context)


def list_name(request):
    users = {'users': models.list_user()}
    return render(request, 'user/list_user.html', users)


def create_user(request):
    return render(request, 'user/create_user.html')


def save_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age')
    tel = request.POST.get('tel')
    rt, error = models.validate_save_user(username, password, age, tel)
    if rt:

        return HttpResponseRedirect('/user/list_name')
    else:
        context = {}
        context['username'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel
        context['error'] = error
        return render(request, 'user/create_user.html', context)


def update_user(request):
    username = request.GET.get('name')
    password, age, tel = models.update_user(username)
    context = {}
    context['username'] = username
    context['password'] = password
    context['age'] = age
    context['tel'] = tel
    return render(request, 'user/update_user.html', context)


def modify_update_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')
    tel = request.POST.get('tel')
    models.modify_update_user(username, password, age, tel)
    return HttpResponseRedirect('/user/list_name')


def delete_user(request):
    username = request.GET.get('name')
    models.delete_user(username)
    return HttpResponseRedirect('/user/list_name')
