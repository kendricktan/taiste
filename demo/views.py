from django.shortcuts import render


# Create your views here.
def demo_view(request):
    return render(request, 'demo.html')
