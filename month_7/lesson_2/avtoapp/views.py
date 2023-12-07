from django.shortcuts import render, redirect, get_object_or_404
from .models import Avto
from .forms import AvtoForm

def avtoList(request):  
    avtos = Avto.objects.all()  
    return render(request,"avto-list.html",{'avtos':avtos})  

def avtoCreate(request):  
    if request.method == "POST":  
        form = AvtoForm(request.POST)  
        if form.is_valid():   
            form.save() 
            model = form.instance
            return redirect('avto-list')  
    else:  
        form = AvtoForm()  
    return render(request,'avto-create.html',{'form':form})  

def avtoUpdate(request, id):  
    avto = get_object_or_404(Avto, pk=id)
    form = AvtoForm(initial={'egasi': avto.egasi, 'model': avto.model, 'narxi': avto.narxi, 'rasmi': avto.rasmi})
    if request.method == "POST":  
        form = AvtoForm(request.POST, instance=avto)  
        if form.is_valid():  
            form.save() 
            model = form.instance
            return redirect('/avto-list')   
    return render(request,'avto-update.html',{'form':form})  

def avtoDelete(request, id):
    avto = get_object_or_404(Avto, pk=id)
    avto.delete()
    return redirect('avto-list')
