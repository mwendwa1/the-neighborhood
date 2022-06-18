import re
from django.shortcuts import render

from hood.models import Neighborhood


# Create your views here.
def index(request):
    return render(request, 'index.html')


def hoods(request):
    all_hoods = Neighborhood.objects.all()
    all_hoods = all_hoods[::-1]
    context = {'all_hoods':all_hoods}
    return render(request, context, 'all_hoods.html')
    
