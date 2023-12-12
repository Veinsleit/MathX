from django.shortcuts import render

from math import sqrt, atan

def main(request):
    template = 'calc/main.html'
    return render(request, template)

def about(request):
    template = 'calc/about.html'
    return render(request, template)

def contacts(request):
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

    x = float(num[0])
    y = float((num[1])[:-1])

    r = sqrt(x**2+y**2)
    fi = atan(y/x)

    zconv = f'{r}(cos{fi} + isin{fi})'

    return render(request, 'calc/algtotrig/convz.html', {'zconv': zconv})

def trigcalc(request):
    return render(request, 'calc/trigcalc/trigcalc.html')

def return_trig_complex(num):
    """Преобразование входного КЧ в тригонометрическую форму""" 
    num = num.split('+')
    print(num)
    r = float(num[0].split('(')[0])
    print(r)
    cosfi = float(num[0].split('(')[1][3:])
    print(cosfi)
    sinfi = float(num[1][4:-1])
    print(sinfi)

    return r, cosfi, sinfi

def triganswer(request):
    zt1 = str(request.GET.get('znt1'))
    zt2 = str(request.GET.get('znt2'))
    zt = str(request.GET.get('znt'))
    zn = str(request.Get.get('n'))

    def zvalue(func):
        zt = []
        for i in func:
            zt.append(i)
        return zt
    
    zt1 = zvalue(return_trig_complex(zt1))
    zt2 = zvalue(return_trig_complex(zt2))
    zt = zvalue(return_trig_complex(zt))

    if request.GET.get('mult') == "":
        mult = [] 
        mult.append(zt1[0] + zt2[0])
        mult.append(zt1[1] + zt2[1])
        mult.append(zt1[2] + zt2[2])
        answer = mult

    elif request.GET.get('div') == "":
        div = [] 
        div.append(zt1[0]/zt2[0])
        div.append(zt1[1] - zt2[1])
        div.append(zt1[2] - zt2[2])
        answer = div

    elif request.GET.get('exp') == "":
        exp = [] 
        exp.append(zt[0]**int(zn))
        exp.append(zt[1]*int(zn))
        exp.append(zt[2]*int(zn))
        answer = exp

    # elif request.GET.get('sqrt') == "":
    #     zsqrt = []

    #     answer = zsqrt

    return answer