
from django.shortcuts import redirect, render
from.models import Member



def index(request):
    member=Member.objects.all()
    return render(request,'index.html',{'member':member})

def add(request):
      return render(request, 'add.html')

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=Member(firstname=x,lastname=y)
    member.save()
    return redirect('index')

def delete(request,id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect('index')
    
def update(request,id):
    member=Member.objects.get(id=id)
    return render(request,'Update.html',{'member':member})
     

def uprecord(request, id):
    x = request.POST.get('first', '')
    y = request.POST.get('last', '')
    member = Member.objects.get(id=id)
    member.firstname = x
    member.lastname = y
    member.save()
    return redirect('index')

