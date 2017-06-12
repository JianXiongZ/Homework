from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from . import models


def index(request):
    context = {'messages': models.get_messages()}
    return render(request, 'online/index.html', context)


def create(request):
    return render(request, 'online/create.html')


def save(request):
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    print(username, title, content)
    models.save_message(username, title, content)
    return HttpResponseRedirect('/online/')


def edit(request):
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    context = {'username': username, 'title': title, 'content': content}
    return render(request, 'online/edit.html', context)


def update(request):
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    print(username, title, content)
    models.update_message(username, title, content)
    return HttpResponseRedirect('/online/')


def delete(request):
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    print(username, title, content)
    models.delete_message(username, title, content)
    return HttpResponseRedirect('/online/')
