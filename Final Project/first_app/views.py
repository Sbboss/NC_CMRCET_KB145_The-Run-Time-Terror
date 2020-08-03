from django.shortcuts import render
from first_app import forms
from django.core.files.storage import FileSystemStorage
from first_app.cnvt_eng import text_to_eng
from first_app.OCR import pdf_ocr, img_ocr
from django.shortcuts import redirect
import sys
import os
from subprocess import run, PIPE


up_f = FileSystemStorage()
def index(request):
    text = ''
    crr_text = ''
    i = "../static/io.jpg"
    if request.method == 'POST':

        form = forms.fUpload(request.POST)

        f = request.FILES['doc']
        if form.is_valid():
            langss = form.cleaned_data['langs']
            choice = form.cleaned_data['file_type']
            # srch = request.POST.get('srch_box')
            langs = '-l ' + "+".join(langss)  #tel+urd
            print(langss)
            print(form.cleaned_data['file_type'])
            file = up_f.save(f.name, f)
            fp = str(up_f.open(file))
            print(fp)
            # try:
            if choice == '0':
                text, count = img_ocr(fp, langs)
            elif choice == '1':
                text, count = pdf_ocr(fp, langs)
            crr_text = text_to_eng(text)
            with open('a.txt', 'w') as fnw:
                s = str(count) + '\n' + langs
                print(s)
                fnw.write(s)
            # except:
            #     redirect('/')
            print(f.name)
            f.close()
    else:
        form = forms.fUpload()
    print(text)
    return render(request, 'main.html', {'form': form, 'text': text, 'crr_text': crr_text, 'i': i})



def search(request):
    img_arr=[]
    s = request.POST.get('srch_box')
    n_srch = 0
    if s:
        img_arr=[]
        count = 0
        with open('a.txt', 'r') as f:
            count = int(f.readline())
            langs = f.readline()
        print(count)
        print(langs)
        fp = ''

        for i in range(count):
            print(s)
            filename = "page" + str(i+1) + ".jpg"
            fp = up_f.open(filename)
            print('-----------')
            q = run([sys.executable, 'C:\\Users\\Shiv\\PycharmProjects\\Shiv\\Django_Prjct\\first_app\\sr.py', str(fp),\
                     str(fp.name), s, str(i+1), str(langs)], shell=False, stdout=PIPE)
            n_srch = int(q.stdout.decode("utf-8").split()[1])
            print("--------------",q.stdout.decode("utf-8").split()[1])
            # cv(fp, s, i+1, langs)
            img_arr.append(q.stdout.decode("utf-8").split()[0])
        print("--------------",img_arr)

    return render(request, 'search_cont.html', {'img_arr': img_arr, 'n_srch': n_srch})
