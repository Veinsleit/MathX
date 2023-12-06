from django.shortcuts import render

from math import sqrt, atan


# Create your views here.
def return_complex_number(num):
    """Преобразование входной строки в комп число"""

    num = num.split('+')
    z = complex(float(num[0]), float((num[1])[:-1]))
    return z


def home(request):
    return render(request, 'calc/home.html')

def conv(request):
    return render(request, 'calc/zconv.html')

def trig(request):
    return render(request, 'calc/trig.html')

def calc(request):
    z1 = str(request.GET.get('zn1'))
    z2 = str(request.GET.get('zn2'))
    z1c = return_complex_number(z1)
    z2c = return_complex_number(z2)

    if request.GET.get('sum') == "":
        answer = z1c + z2c

    elif request.GET.get('diff') == "":
        answer = z1c-z2c

    elif request.GET.get('mult') == "":
        answer = z1c*z2c

    elif request.GET.get('div') == "":
        answer = z1c/z2c

    return render(request, 'calc/answer.html', {'answer': answer})

def convz(request):
    zin = str(request.GET.get('zin'))

    num = zin.split('+')

    x = float(num[0])
    y = float((num[1])[:-1])

    r = sqrt(x**2+y**2)
    fi = atan(y/x)

    zconv = f'{r}(cos{fi} + jsin{fi})'

    return render(request, 'calc/zconvanswer.html', {'zconv': zconv})


# def trig_calc(request):
#     zt1 = str(request.GET.get('znt1'))
#     zt2 = str(request.GET.get('znt2'))
#     zt = str(request.GET.get('znt'))

#     if request.GET.get('mult') == "":
#         answer = 

#     elif request.GET.get('div') == "":
#         answer = 

#     elif request.GET.get('^') == "":
#         answer = 

#     elif request.GET.get('sqrt') == "":
#         answer = 