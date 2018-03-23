from django.shortcuts import render,redirect,  get_object_or_404
from . models import Board, Topic, Post
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})


# def board_topics(request, pk):
#     board = Board.objects.get(pk =pk)
#     return render(request, 'topics.html', {'board':board})


# def board_topics(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         raise Http404
#     return render(request, 'topics.html', {'board': board})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
