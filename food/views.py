from django.shortcuts import render
from .models import dishes

# Create your views here.
def home(request):
    dish = dishes.objects.all()
    return render(request,'index.html',{'dish':dish})