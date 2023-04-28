from django.shortcuts import render, redirect
from .models import Client

# Create your views here.
def home(request):
    if request.method=='POST':
        date1=request.POST.get('date1')
        date2=request.POST.get('date2')
        adult=request.POST.get('adult')
        children=request.POST.get('children')
        rooms=request.POST.get('rooms')
        print(date1,date2,adult,children,rooms)

        client=Client.objects.create(
            from_date=date1,
            to_date=date2,
            kattalar=adult,
            bolalar=children,
            xonalar=rooms
        )



    return render(request,'index.html')



