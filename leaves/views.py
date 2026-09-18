from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Leave

# Create your views here.
@login_required
def apply_leave(request):
    if request.method == 'POST':
        Leave.objects.create(
            user=request.user,
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start'],
            end_date=request.POST['end'],
            reason=request.POST['reason'],
            status='pending')
        return redirect('staff_dashboard')

    return render(request,'apply_leave.html')



@login_required
def my_leaves(request):
    leave = Leave.objects.filter(user=request.user)
    return render(request, 'my_leaves.html',{'leaves':leave})


@login_required
def view_leaves(request):
    if request.user.profile.role != 'admin':
        return redirect('staff_dashboard')

    leave = Leave.objects.all()
    return render(request,'view_leaves.html',{'leaves':leave})


@login_required
def  approve_leave(request,id):
    if request.user.profile.role !='admin':
        return redirect('staff_dashboard')

    leave = get_object_or_404(Leave, id=id)
    leave.status='Approve'
    leave.save()
    return redirect('view_leaves')

@login_required
def reject_leave(request, id):
    if request.user.profile.role !='admin':
        return redirect('staff_dashboard')

    leave = get_object_or_404(Leave, id=id)
    leave.status = 'Reject'
    leave.save()
    return redirect('view_leaves')