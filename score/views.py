from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DataBottle, Department, Score, HistoryEvaluate

# Create your views here.


@api_view(['POST'])
def post_data(request):
    data = request.data
    department = Department.objects.get(pk=data.get('department'))
    data_bottle = DataBottle.objects.filter(
        studentID=data.get("studentID"), status=0)
    score = Score.objects.all().values()[0]
    if data_bottle:
        DataBottle.objects.filter(pk=data_bottle[0].id).update(
            quantity=data.get('quantity')+data_bottle[0].quantity,
            score=(data.get('quantity') +
                   data_bottle[0].quantity)/score['numItem']*score['score']
        )
    else:
        DataBottle.objects.create(
            name=data.get('name'),
            studentID=data.get('studentID'),
            quantity=data.get('quantity'),
            department=department,
            note=data.get('note'),
            status=0,
            score=data.get('quantity')/score['numItem']*score['score']
        )
    return Response(status=status.HTTP_200_OK)


def score_view(request):
    departments = Department.objects.all()
    department = Department.objects.get(id=1)
    not_evaluate = DataBottle.objects.filter(status=0, department=department)
    return render(request, 'score.html', context={'departments': departments, 'not_evaluate': not_evaluate})


def history_view(request):
    departments = Department.objects.all()
    histories = HistoryEvaluate.objects.all()
    print(histories)
    return render(request, 'history.html', context={"departments": departments, "histories": histories})


def historyItem_view(request, id):
    departments = Department.objects.all()
    history = HistoryEvaluate.objects.get(pk=id)
    dataBottles = DataBottle.objects.filter(pk__in=history.dataBottle)
    return render(request, 'historyItem.html', context={"departments": departments, "dataBottles": dataBottles})


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass
