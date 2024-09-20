from django.shortcuts import render

from .models import *
# Create your views here.
def home(req):
    return render(req,'user/index.html')

def about(req):
    return render(req,'user/about.html')

def imagegallery(req):
    gdata=gallery.objects.all().order_by('-pdes')
    #gdata=gallery.objects.filter(pdes="Sapna",)
    print(gdata)
    mydict={"d":gdata}

    return render(req,'user/gallery.html',mydict)


def ourrecruiters(req):
    rdata=recruiters.objects.all()
    print(rdata)
    mydict={"d":rdata}
    return render(req,'user/recruiters.html',mydict)

def course(req):
        cdata=courses.objects.all()
        print(cdata)
        mydict={"d":cdata}
        return render(req,'user/courses.html',mydict)

def contactus(request):
    status=False
    if request.method=='POST':
        a=request.POST.get("name","")
        b=request.POST.get("contact","")
        c=request.POST.get("address","")
        d=request.POST.get("email","")
        e=request.POST.get("message", "")
        x=contact(name=a,contact=b,email=c,address=d,message=e)
        x.save()
        status=True


    return render(request,'user/contactus.html',{'S':status})

def services(req):
    return render(req,'user/services.html')

def adminlogin(req):
    return render(req,'user/adminlogin.html')

def ourplacement(req):
    cdata=courses.objects.all().order_by('-id')
    a=req.GET.get('msg')
    pdata=""
    if a is None:
        pdata=placements.objects.all()
    else:
        pdata=placements.objects.filter(pcourse=a)
    return render(req,'user/ourplacement.html',{"course":cdata,"ourplacement":pdata})

def faculty(req):
    cname=fact.objects.all()
    return render(req,'user/faculty.html',{"d":cname})
