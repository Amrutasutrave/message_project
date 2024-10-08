from django.shortcuts import render,HttpResponse,redirect
from msgapp.models import Msg

# Create your views here.
def create (request):
    if request.method=="GET":
    #print("Request is:", request.method)
        return render(request,'create.html')
    else:
        name=request.POST['username']
        mail=request.POST['mail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        print("Username is:",name)
        print("Email Id is:",mail)
        print("Mobile num is:",mob)
        print("Message is:",msg)
        m=Msg.objects.create(name=name,mail=mail,mob=mob,msg=msg)
        m.save()
        #return HttpResponse("Data inserted")
        return redirect('/dashboard')
    
def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    #print("Id to be deleted",rid)
    #return HttpResponse("ID to be deleted"+rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=="GET":
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        name=request.POST['username']
        mail=request.POST['mail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        m=Msg.objects.create(name=name,mail=mail,mob=mob,msg=msg)
        m.save()
        m = Msg.objects.filter(id=rid)
        m.delete()
        #return HttpResponse("Data inserted")
        return redirect('/dashboard')