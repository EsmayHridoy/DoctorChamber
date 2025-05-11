from django.shortcuts import render, redirect
from registration.models import User

def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                if user.is_approved:
                    request.session['user_id'] = user.id

                    # Role-based redirection
                    role_name = user.role.role.lower()
                    if role_name == 'admin':
                        return redirect('admin_dashboard')
                    elif role_name == 'doctor':
                        return redirect('doctor_dashboard')
                    elif role_name == 'general':
                        return redirect('general_dashboard')
                    else:
                        return redirect('default_dashboard')
                else:
                    error_message = "Your account is not approved yet."
            else:
                error_message = "Incorrect password."
        except User.DoesNotExist:
            error_message = "User does not exist."

    return render(request, 'login/login.html', {'error_message': error_message})
