from django.shortcuts import render
from django.http import HttpResponse
from models import Article
from django.shortcuts import render


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
