from django.shortcuts import render
import random

from math import sqrt, atan

q1 = [
    'Математика — это ключ и дверь ко всем наукам.',
    '— Галилео Галилей'
        ]
q2 = [
    'Нельзя быть настоящим математиком, не будучи немного поэтом.', 
    '— Карл Теодор Вильгельм Вейерштрасс'
        ]
q3 = [
    'Если теорему так и не смогли доказать, она становится аксиомой.', 
    '— Евклид'
        ]
q4 = [
    'Математику уже затем учить надо, что она ум в порядок приводит.', 
    '— Михаил Васильевич Ломоносов'
        ]
q5 = [
    'Величие человека - в его способности мыслить.', 
    '— Блез Паскаль'
        ]

def main(request):
    template = 'calc/main.html'
    select = random.randint(1, 5)
    qlist = [q1, q2, q3, q4, q5]
    index = 0
    for i in qlist:
        index +=1
        if select == index:
            quote = i[0]
            author = i[1]
            index = 0

    return render(request, template, {'quote':quote, 'author':author})

def about(request):
    """Страница информации о сайте"""
    template = 'calc/about.html'
    return render(request, template)

def contacts(request):
    """Страница контактов"""
    template = 'calc/contacts.html'
    return render(request, template)

def algcalc(request):
    template = 'calc/algcalc/algcalc.html'
    return render(request, template)

def return_complex_number(num):
    """Преобразование входной строки в комп число"""

    num = num.split('+')
    z = complex(float(num[0].strip()), float((num[1].strip())[1:]))
    return z

def alganswer(request):
    z1 = str(request.GET.get('zn1'))
    z2 = str(request.GET.get('zn2'))
    z1c = return_complex_number(z1)
    z2c = return_complex_number(z2)

    if request.GET.get('sum') == "":
        ca = z1c+z2c 
        real = str(ca.real)
        imag = str(ca.imag)
        answer = 'z + w = '+'('+z1+')'+' + '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('diff') == "":
        ca = z1c-z2c 
        real = str(ca.real)
        imag = str(ca.imag)
        answer = 'z - w = '+'('+z1+')'+' - '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('mult') == "":
        ca = z1c*z2c 
        real = str(ca.real)
        imag = str(ca.imag)
        answer = 'z * w = '+'('+z1+')'+' * '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('div') == "":
        ca = z1c/z2c 
        real = str(ca.real)
        imag = str(ca.imag)
        answer = 'z / w = '+'('+z1+')'+' / '+'('+z2+')'+' = '+real+' + i'+imag

    template = 'calc/algcalc/alganswer.html'

    return render(request, template, {'answer': answer})

def algtotrig(request):
    return render(request, 'calc/algtotrig/algtotrig.html')

def convz(request):
    zin = str(request.GET.get('zin'))

    num = zin.split('+')

    x = float(num[0].strip())
    y = float((num[1].strip())[1:])

    r = round(sqrt(x**2+y**2), 2)
    fi = round(atan(y/x), 2)

    zconv = f'{r}(cos({fi}) + isin({fi}))'

    return render(request, 'calc/algtotrig/convz.html', {'zconv': zconv})

def trigcalc(request):
    return render(request, 'calc/trigcalc/trigcalc.html')

def return_trig_complex(num):
    num = num.split('+')
    r = float(num[0].strip().split('(')[0])
    cosfi = float(num[0].strip().split('(')[1][3:])
    sinfi = float(num[1].strip()[4:-1])
    clist = []
    clist.append(r)
    clist.append(cosfi)
    clist.append(sinfi)

    return clist

def triganswer(request):
    zt1 = str(request.GET.get('znt1'))
    zt2 = str(request.GET.get('znt2'))
    zr = str(request.GET.get('zr'))
    zfi = str(request.GET.get('zfi'))
    zn = str(request.GET.get('zn'))

    def zvalue(func):
        zt = []
        for i in func:
            zt.append(i)
        return zt

    if request.GET.get('mult') == "":
        zt1 = return_trig_complex(zt1)
        zt2 = return_trig_complex(zt2)
        mult = [] 
        mult.append(zt1[0] + zt2[0])
        mult.append(zt1[1] + zt2[1])
        mult.append(zt1[2] + zt2[2])
        answer = 'z = '+str(mult[0])+'(cos('+str(mult[1])+') + isin('+str(mult[2])+'))'

    elif request.GET.get('div') == "":
        zt1 = zvalue(return_trig_complex(zt1))
        zt2 = zvalue(return_trig_complex(zt2))
        div = [] 
        div.append(zt1[0]/zt2[0])
        div.append(zt1[1] - zt2[1])
        div.append(zt1[2] - zt2[2])
        answer = 'z = '+str(div[0])+'(cos('+str(div[1])+') + isin('+str(div[2])+'))'

    elif request.GET.get('exp') == "":
        exp = [] 
        exp.append(float(zr)**int(zn))
        exp.append(float(zfi)*int(zn))
        answer = 'z = '+str(exp[0])+'(cos('+str(exp[1])+') + ('+'sin('+str(exp[1])+'))'

    template = 'calc/trigcalc/triganswer.html'
    
    return render(request, template, {'answer': answer})
