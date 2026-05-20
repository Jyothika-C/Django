from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    context = {
        'user_name': request.user.username,
        'is_student': request.user.is_student,
    }

    return render(request, 'dashboard.html', context)