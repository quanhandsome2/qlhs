from .models import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import pandas as pd


def add_nk(request):

    if request.method == "POST" and request.FILES['myfile3']:
        # Đọc file vào dataframe
        myfile = request.FILES['myfile3']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        empexceldata = pd.read_excel("." + excel_file)
        df = empexceldata
        print(df)

        for i in range(len(df)):

            nien_khoa = df.loc[i, 'nien_khoa']
            nien_khoa_tit = df.loc[i, 'nien_khoa_tit']

            nk = Nien_khoa.objects.create(
                nien_khoa = nien_khoa,
                nien_khoa_tit=nien_khoa_tit,
            )
            nk.save()
    return render(request, 'school/admin_import_nk.html')


def add_khoi(request):

    if request.method == "POST" and request.FILES['myfile3']:
        # Đọc file vào dataframe
        myfile = request.FILES['myfile3']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        empexceldata = pd.read_excel("." + excel_file)
        df = empexceldata
        print(df)

        for i in range(len(df)):

            ten_khoi = df.loc[i, 'ten_khoi']
            ma_khoi = df.loc[i, 'nien_khoa_tit']
            khoi_tit = df.loc[i, 'khoi_tit']

            nk = Khoi.objects.create(
                ten_khoi = ten_khoi,
                ma_khoi = ma_khoi,
                khoi_tit=khoi_tit,
            )
            nk.save()
    return render(request, 'school/admin_import_nk.html')

def add_gv(request):

    if request.method == "POST" and request.FILES['myfile3']:
        # Đọc file vào dataframe
        myfile = request.FILES['myfile3']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        empexceldata = pd.read_excel("." + excel_file)
        df = empexceldata
        print(df)

        for i in range(len(df)):

            salary = df.loc[i, 'salary']
            joindate = df.loc[i, 'joindate']
            mobile = df.loc[i, 'mobile']
            user = df.loc[i, 'user_id']
            gioi_tinh = df.loc[i, 'gioi_tinh']
            phone = df.loc[i, 'phone']
            ten_gv = df.loc[i, 'ten_gv']


            nk = TeacherExtra.objects.create(
                salary = salary,
                joindate = joindate,
                mobile=mobile,
                user_id = user,
                gioi_tinh = gioi_tinh,
                phone=phone,
                ten_gv=ten_gv,
            )
            nk.save()
    return render(request, 'school/admin_import_nk.html')

def add_mon_hoc(request):

    if request.method == "POST" and request.FILES['myfile3']:
        # Đọc file vào dataframe
        myfile = request.FILES['myfile3']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        empexceldata = pd.read_excel("." + excel_file)
        df = empexceldata
        print(df)

        for i in range(len(df)):

            ma_mon = df.loc[i, 'ma_mon']
            mon_tit = df.loc[i, 'mon_tit']
            ma_khoi_id = df.loc[i, 'ma_khoi_id']
            ten_mon = df.loc[i, 'ten_mon']


            nk = Mon_hoc.objects.create(
                ma_mon = ma_mon,
                mon_tit = mon_tit,
                ma_khoi_id=ma_khoi_id,
                ten_mon = ten_mon,
            )
            nk.save()
    return render(request, 'school/admin_import_nk.html')