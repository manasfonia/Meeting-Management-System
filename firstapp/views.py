from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm1, RegistrationForm2, VisitorForm
from .models import EmployeeInfo, VisitorInfo


# Create your views here.
def DisplayView(request):
    return render(request, "base.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url="/")
def ProfileView(request):
    return render(request, "profile.html")


@login_required(login_url="/")
def EmView(request):
    all_emp_details = EmployeeInfo.objects.all()
    context = {
        'all_emp_details': all_emp_details
    }
    return render(request, "employeedata.html", context=context)


@login_required(login_url="/")
def ScheduleView(request):
    all_sch_details = VisitorInfo.objects.all()
    context = {
        'all_sch_details': all_sch_details
    }
    return render(request, "meetingSchedule.html", context=context)

@login_required(login_url="/")
def DeleteVisitor(request, pk):
    vis = VisitorInfo.objects.filter(id=pk).first()
    if vis:
        vis.delete()
    return redirect('meetings')

@login_required(login_url="/")
def UpdateVisitor(request, pk):
    vis_update = VisitorInfo.objects.get(id=pk)
    if request.method== 'GET':
        form = VisitorForm(instance=vis_update)
    else:
        form = VisitorForm(request.POST,  instance=vis_update)
        if form.is_valid():
            form.save()
            return redirect('meetings')

    context = {
        'form': form,
    }
    return render(request, "fixmeet.html", context=context)

@login_required(login_url="/")
def UserMeeting(request):
    emp_user = EmployeeInfo.objects.filter(user=request.user).first()
    sch_details = VisitorInfo.objects.filter(host=emp_user)
    context = {
        'sch_details': sch_details
    }
    return render(request, "user_meeting.html", context=context)

@login_required(login_url="/")
def FixView(request):
    form = VisitorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        'form': form
    }
    return render(request, "fixmeet.html", context=context)


@login_required(login_url="/")
def AddEmployer(request):
    registration1_form = RegistrationForm1(request.POST or None)
    if registration1_form.is_valid():
        registration1 = registration1_form.save()

        return redirect('register', username=registration1.username)

    context = {
        'registration1_form': registration1_form
    }

    return render(request, "addempolyer.html", context=context)


@login_required(login_url="/")
def RegisterEmployer(request, username):
    user = User.objects.get(username=username)
    registration2_form = RegistrationForm2(request.POST or None)
    if registration2_form.is_valid():
        registration2 = registration2_form.save(commit=False)
        registration2.user = user
        registration2.save()
        return redirect('profile')

    context = {
        'registration2_form': registration2_form,
    }
    return render(request, "empregister.html", context=context)

@login_required(login_url="/")
def DeleteEmployee(request, username):
    emp = EmployeeInfo.objects.filter(user__username=username).first()
    if emp:
        emp.delete()
    return redirect('emdata')

@login_required(login_url="/")
def UpdateEmployee(request, username):
    emp_update = EmployeeInfo.objects.get(user__username=username)
    emp_user = User.objects.get(username=username)
    if request.method== 'GET':
        registration1_form = RegistrationForm1(instance=emp_user)
        registration2_form = RegistrationForm2(instance=emp_update)
    else:
        registration1_form = RegistrationForm1(request.POST,  instance=emp_user)
        registration2_form = RegistrationForm2(request.POST,  instance=emp_update)
        if registration1_form.is_valid() and registration2_form.is_valid():
            registration1_form.save()
            registration2_form.save()
            return redirect('profile')

    context = {
        'registration1_form': registration1_form,
        'registration2_form': registration2_form,
    }
    return render(request, "updateEmployee.html", context=context)

@login_required(login_url="/")
def UserUpdate(request):
    emp_info = EmployeeInfo.objects.get(user=request.user)
    emp_user = User.objects.get(username =request.user)
    if request.method== 'GET':
        registration1_form = RegistrationForm1(instance=emp_user)
        registration2_form = RegistrationForm2(instance=emp_info)
    else:
        registration1_form = RegistrationForm1(request.POST,  instance=emp_user)
        registration2_form = RegistrationForm2(request.POST,  instance=emp_info)
        if registration1_form.is_valid() and registration2_form.is_valid():
            registration1_form.save()
            registration2_form.save()
            return redirect('profile')

    context = {
        'registration1_form': registration1_form,
        'registration2_form': registration2_form,
    }
    return render(request, "updateEmployee.html", context=context,)




