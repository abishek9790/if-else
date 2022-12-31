from django.shortcuts import render

# Create your views here.
def applicationc(request):
    d={'a':1000,'b':200}
    return render(request, 'applicationc.html',context=d)