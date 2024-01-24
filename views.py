from django.shortcuts import render,redirect
from . models import DashboardData
from . forms import DashboardDataForm
# Create your views here.
def index(request):
    data = DashboardData.objects.all()
    
    
    if request.method == 'POST':
        form = DashboardDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DashboardDataForm()        

    context = {
        "data": data,
        "form": form
    }
    
    return render(request, 'app/index.html',context)


