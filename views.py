from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from docx import *


def fun(request):
    arr = []
    emp = ""
    if request.method == 'POST':
        fil = str(request.FILES['myfile']).split(".")
        print(fil[1])
        if fil[1] != "docx":
            return render(request, 'upload.html', {'alert_flag': True})
        file1 = request.FILES['myfile']
        doc = Document(file1)
        for para in doc.paragraphs:
            line = para.text.split()
            for i in line:
                emp = " "
                if i != ":":
                    emp += i
            arr.append(emp)

        setoflist = {'fname': arr[0],
                     'lname': arr[1],
                     'regno': arr[2],
                     'college': arr[3],
                     'mailid': arr[4],
                     'dept': arr[5],
                     'skills': arr[6],
                     'pincode': arr[7],
                     'state': arr[8],
                     'country': arr[9]
                     }
        if arr[0] == " " or arr[1] == " " or arr[2] == " " or arr[3] == " " or arr[5] == " " or arr[6] == " " or arr[
            7] == " " or arr[8] == " " or arr[9] == " ":
            return render(request, 'upload.html', {'alert_flag1': True})
        else:
            return render(request,'display.html',setoflist)

    return render(request, "upload.html")
