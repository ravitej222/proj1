from django.shortcuts import render,HttpResponseRedirect,redirect
from app1.models import course
from app1.forms import courseform,courseform2

# Create your views here. 

def index(request):
    context = {'msg':'This is home Page','title':'home'}
    return render(request,'app1/index.html',context)

def courses(request):
    coursedata = course.objects.all()
    context = {'msg': 'this is courses page','title':'course','coursedata':coursedata}
    return render(request,'app1/index.html',context)


def newcourse(request):
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save()
    form = courseform()
    context = {'msg':'this is new course','form':form}    
    return render(request,'app1/newcourse.html',context)

def newcourse2(request):
    if request.method == 'POST':
        form = courseform2(request.POST)
        if form.is_valid():
            cname = form.cleaned_data['cname']
            fee = form.cleaned_data['fee']
            dur = form.cleaned_data['dur']
            trainer = form.cleaned_data['trainer']
            Course = course(cname=cname,fee=fee,dur=dur,trainer=trainer)
            Course.save()
            form = courseform2()
        else:
            print("invalid data")
    else:
        form = courseform2()
        form.order_fields(field_order=['trainer','cname','dur','fee'])
        context = {'msg':'This is new course-2 page','form':form}
    return render(request,'app1/newcourse.html',context)

def newcourse3(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        fee = request.POST.get('fee')
        dur = request.POST.get('dur')
        trainer = request.POST.get('trainer')
        # course = course(cname=cname,fee=fee,dur=dur,trainer=trainer)
        course.objects.create(cname=cname,fee=fee,dur=dur,trainer=trainer)
        return redirect('app1:courses')
    else:
        return render(request,'app1/newcourse3.html')


def updatecourse(request,id):
    if request.method == 'POST':
        Course = course.objects.get(id=id)
        form = courseform(request.POST,instance=Course)
        if form.is_valid():
            form.save()
    else:
        Course = course.objects.get(id=id)
        form = courseform(instance=Course)
    context = {'msg':'update course data','form':form}
    return render(request,'app1/updatecourse.html',context)


def deletecourse(request,id):
    if request.method == 'POST':
        Course = course.objects.get(id=id)
        Course.delete()
    return HttpResponseRedirect('/app1/courses')