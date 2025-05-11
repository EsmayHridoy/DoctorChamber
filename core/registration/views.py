from django.shortcuts import render, redirect
from .models import User, Role

def registration(request):
    context = {
        'roles': Role.objects.all(),
        'email_exists': False
    }

    if request.method == 'POST':
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            context['email_exists'] = True
            return render(request, 'registration/registration.html', context)

        user = User(
            first_name=request.POST['first_name'],
            middle_name=request.POST['middle_name'],
            last_name=request.POST['last_name'],
            email=email,
            role=Role.objects.get(id=request.POST['role']),
        )
        user.set_password(request.POST['password'])
        user.save()
        context['email_exists'] = False
        return render(request, 'registration/registration.html', context)

    return render(request, 'registration/registration.html', context)
