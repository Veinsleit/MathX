from django.shortcuts import render, redirect
from math import sqrt, atan

import random

from . import quotes


def main(request):
    """Главная страница"""

    template = 'calc/main.html'
    select = random.randint(1, 5)
    qlist = [
        quotes.q1, 
        quotes.q2, 
        quotes.q3, 
        quotes.q4, 
        quotes.q5,
            ]
    index = 0
    for i in qlist:
        index +=1
        if select == index:
            quote = i[0]
            author = i[1]
            index = 0
            break

    return render(request, template, {'quote':quote, 'author':author})


def about(request):
    """Страница информации о сайте"""

    template = 'calc/about.html'
    return render(request, template)


def contacts(request):
    """Страница контактов"""

    template = 'calc/contacts.html'
    return render(request, template)


def algcalc(request, excpt = ''):
    """Страница калькулятора алгебраической формы КЧ"""

    template = 'calc/algcalc/algcalc.html'
    return render(request, template, {'excpt': excpt})


def return_complex_number(num):
    """Преобразование входной строки в КЧ"""

    num = num.split('+')
    z = complex(float(num[0].strip()), float((num[1].strip())[1:]))

    return z


def alganswer(request):
    """Страница с ответом калькулятора алгебраической формы КЧ"""

    z1 = str(request.GET.get('zn1'))
    z2 = str(request.GET.get('zn2'))

    try:
        z1c = return_complex_number(z1)
        z2c = return_complex_number(z2)
    except:
        return redirect('algexcept')

    if request.GET.get('sum') == "":
        ca = z1c+z2c 
        real = str(round(ca.real, 2))
        imag = str(round(ca.imag, 2))
        if len(real.split('.')[1]) == 1 and real.split('.')[1] == '0':
            real = real.split('.')[0]
        if len(imag.split('.')[1]) == 1 and imag.split('.')[1] == '0':
            imag = imag.split('.')[0]
        if ca.real == 0 and ca.imag == 0:
            answer = 'z + w = '+'('+z1+')'+' + '+'('+z2+')'+' =  0'
        else:
            answer = 'z + w = '+'('+z1+')'+' + '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('diff') == "":
        ca = z1c-z2c 
        real = str(round(ca.real, 2))
        imag = str(round(ca.imag, 2))
        if len(real.split('.')[1]) == 1 and real.split('.')[1] == '0':
            real = real.split('.')[0]
        if len(imag.split('.')[1]) == 1 and imag.split('.')[1] == '0':
            imag = imag.split('.')[0]
        if ca.real == 0 and ca.imag == 0:
            answer = 'z - w = '+'('+z1+')'+' - '+'('+z2+')'+' = 0'
        else:
            answer = 'z - w = '+'('+z1+')'+' - '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('mult') == "":
        ca = z1c*z2c 
        real = str(round(ca.real, 2))
        imag = str(round(ca.imag, 2))
        if len(real.split('.')[1]) == 1 and real.split('.')[1] == '0':
            real = real.split('.')[0]
        if len(imag.split('.')[1]) == 1 and imag.split('.')[1] == '0':
            imag = imag.split('.')[0]
        if ca.real == 0 and ca.imag == 0:
             answer = 'z * w = '+'('+z1+')'+' * '+'('+z2+')'+' = 0'
        else:
            answer = 'z * w = '+'('+z1+')'+' * '+'('+z2+')'+' = '+real+' + i'+imag

    elif request.GET.get('div') == "":
        ca = z1c/z2c 
        real = str(round(ca.real, 2))
        imag = str(round(ca.imag, 2))
        if len(real.split('.')[1]) == 1 and real.split('.')[1] == '0':
            real = real.split('.')[0]
        if len(imag.split('.')[1]) == 1 and imag.split('.')[1] == '0':
            imag = imag.split('.')[0]
        if ca.real == 0 and ca.imag == 0:
            answer = 'z / w = '+'('+z1+')'+' / '+'('+z2+')'+' = 0'
        else:
            answer = 'z / w = '+'('+z1+')'+' / '+'('+z2+')'+' = '+real+' + i'+imag

    template = 'calc/algcalc/alganswer.html'

    return render(request, template, {'answer': answer})


def algexcept(request):

    template = 'calc/algcalc/algex.html'
    return render(request, template)


def algtotrig(request):

    template = 'calc/algtotrig/algtotrig.html'
    return render(request, template)


def convz(request):

    zin = str(request.GET.get('zin'))
    num = zin.split('+')

    try:
        x = float(num[0].strip())
        y = float((num[1].strip())[1:])
    except:
        return redirect(convzex)

    r = round(sqrt(x**2+y**2), 2)
    if x == 0:
        fi = 0
    else:
        fi = round(atan(y/x), 2)

    zconv = f'{r}(cos({fi}) + isin({fi}))'

    template = 'calc/algtotrig/convz.html'

    return render(request, template, {'zconv': zconv})

def convzex(request):

    template = 'calc/algtotrig/algtotrigex.html'
    return render(request, template)

def trigcalc(request):

    template = 'calc/trigcalc/trigcalc.html'
    return render(request, template)

def return_trig_complex(num):

    num = num.split('+')


    r = float(num[0].strip().split('(')[0])
    cosfi = float(num[0].strip().split('(')[2][0:-1])
    sinfi = float(num[1].strip().split('(')[1][0:-2])

    
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

    if request.GET.get('mult') == "":
        try:
            zt1 = return_trig_complex(zt1)
            zt2 = return_trig_complex(zt2)
        except:
            return redirect(trigex)
        mult = [] 
        mult.append(zt1[0] + zt2[0])
        mult.append(zt1[1] + zt2[1])
        mult.append(zt1[2] + zt2[2])
        answer = 'z = '+str(mult[0])+'(cos('+str(mult[1])+') + isin('+str(mult[2])+'))'

    elif request.GET.get('div') == "":
        try:
            zt1 = return_trig_complex(zt1)
            zt2 = return_trig_complex(zt2)
        except:
            return redirect(trigex)
        div = [] 
        if zt2[0] == 0:
            div.append(0)
        else:
            div.append(zt1[0]/zt2[0])
        div.append(zt1[1] - zt2[1])
        div.append(zt1[2] - zt2[2])
        answer = 'z = '+str(div[0])+'(cos('+str(div[1])+') + isin('+str(div[2])+'))'

    elif request.GET.get('exp') == "":
        exp = []

        try: 
            exp.append(float(zr)**int(zn))
            exp.append(float(zfi)*int(zn))
        except:
            return redirect(trigex)

        answer = 'z = '+str(exp[0])+'(cos('+str(exp[1])+') + '+'sin('+str(exp[1])+'))'

    template = 'calc/trigcalc/triganswer.html'
    
    return render(request, template, {'answer': answer})

def trigex(request):

    template = 'calc/trigcalc/trigex.html'
    return render(request, template)