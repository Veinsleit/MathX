from django.shortcuts import render



# Create your views here.
def return_complex_number(num):
    """Преобразование входной строки в комп число"""

    num = num.split('+')
    z = complex(float(num[0]), float((num[1])[:-1]))
    return z


def home(request):
    return render(request, 'calc/home.html')

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


    