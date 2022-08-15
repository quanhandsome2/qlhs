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