from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'likki','age':22}
    return render(request,'jinja_print.html',context=d)

def test1(request):
    d1={'name':'likki','age':21}
    return render(request,'test1.html',context=d1)


def ope(request):
    dict={'name':'mohii','age':22}
    return render(request,'ope.html',context=dict)


def loop(request):
    di={'name':'saha','age':21}
    return render(request,'loop.html',context=di)

