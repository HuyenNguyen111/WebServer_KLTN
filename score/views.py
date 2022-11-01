from django.shortcuts import render
from django.views import View

# Create your views here.


def score_view(request):
    return render(request, 'score.html')


def history_view(request):
    return render(request, 'history.html')


def historyItem_view(request, id):
    return render(request, 'historyItem.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass
