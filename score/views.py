from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DataBottle, Department, Score, HistoryEvaluate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout as lout
from typing import Union
import xlwt
from django.core.paginator import Paginator
# Create your views here.


@api_view(['POST'])
def post_data(request) -> Response:
    data: dict = request.data
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

@login_required
def index(request):
    return redirect('/score/?page=1')

@login_required
def score_view(request) -> HttpResponse:
    page = request.GET['page']
    departments = Department.objects.all()
    not_evaluate = DataBottle.objects.filter(
        status=0
    )
    paginator = Paginator(not_evaluate, per_page=2)
    page_object = paginator.get_page(page)
    return render(request, 'score.html', context={'departments': departments, 'page_object': page_object})


@login_required
def history_view(request) -> HttpResponse:
    departments = Department.objects.all()
    histories = HistoryEvaluate.objects.all()
    return render(request, 'history.html', context={"departments": departments, "histories": histories})


@login_required
def historyItem_view(request, id) -> HttpResponse:
    departments = Department.objects.all()
    history = HistoryEvaluate.objects.get(pk=id)
    dataBottles = DataBottle.objects.filter(pk__in=history.dataBottle)
    return render(request, 'historyItem.html', context={"departments": departments, "dataBottles": dataBottles})


class Login(View):
    def get(self, request) -> HttpResponse:
        return render(request, 'login.html')

    def post(self, request) -> Union[HttpResponse, HttpResponseRedirect]:
        data = request.POST
        user = authenticate(username=data.get('username'),
                            password=data.get('password'))
        if user is not None:
            login(request=request, user=user)
            return redirect('/')
        else:
            return render(request, 'login.html', context={"error": "Username or password incorrect"})


@login_required
def logout(request) -> HttpResponseRedirect:
    lout(request)
    return redirect('login')


@api_view(['POST'])
def update_score(request) -> Response:
    data: dict = request.data
    dpm = Department.objects.get(id=int(data.get('dpm')))
    score = Score.objects.all().values()[0]
    DataBottle.objects.filter(id=int(data.get('id'))).update(
        name=data.get('name'),
        quantity=int(data.get('quantity')),
        department=dpm,
        score=int(data.get('quantity'))/score['numItem']*score['score']

    )
    return Response(status=status.HTTP_200_OK)


@login_required
def export_report(request):

    dpm = Department.objects.get(id=int(request.GET['dpm'][0]))
    data = DataBottle.objects.filter(department=dpm)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['STT', 'Họ và Tên', 'Mã Sinh viên',
               'Khoa/viện', 'Số lượng', 'Điểm']

    for col_num in range(len(columns)):
        # at 0 row 0 column
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
