from django.shortcuts import render

# Create your views here.


def get_landing(request):
    return render(request, 'tenant_types/public/pages/landing/_index.html')