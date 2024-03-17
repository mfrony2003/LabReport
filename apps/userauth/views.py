from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:            
            login(request, user)           
            return redirect(redirectonUsertypes(user.role_id))
            
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'auth/login.html')

def redirectonUsertypes(role_id):
    role_types = {
            1: "admin",
            2: "staff",
            3: "doctor",
            4: "pathologist",
            5: "patient"
        }
    print(role_types[role_id])

    pagename=role_types[role_id]+'dashboard'

    return pagename


def logout_user(request):
    logout(request)
    return  redirect('login')

def home(request):
    return render(request, 'home.html')