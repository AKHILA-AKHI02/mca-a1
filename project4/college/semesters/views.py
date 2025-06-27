from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        User.objects.create(username=uname, email=email, password=pwd)
        messages.success(request, 'Registration successful.')
        return redirect('login')
    
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect('login')

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def mca101(request):
    return render(request,'MCA101.html')
def mca102(request):
    return render(request,'MCA102.html')
def mca103(request):
    return render(request,'MCA103.html')
def mca104(request):
    return render(request,'MCA104.html')
def mca105(request):
    return render(request,'MCA105.html')
def mca106(request):
    return render(request,'MCA106.html')
def mca107(request):
    return render(request,'MCA107.html')
def mca108(request):
    return render(request,'MCA108.html')
def mca201(request):
    return render(request,'MCA201.html')
def mca202(request):
    return render(request,'MCA202.html')
def mca203(request):
    return render(request,'MCA203.html')
def mca204(request):
    return render(request,'MCA204.html')
def mca205(request):
    return render(request,'MCA205.html')
def mca206(request):
    return render(request,'MCA206.html')
def mca207(request):
    return render(request,'MCA207.html')
def mca208(request):
    return render(request,'MCA208.html')
def mca209(request):
    return render(request,'MCA209.html')
def mca301(request):
    return render(request,'MCA301.html')
def mca302(request):
    return render(request,'MCA302.html')
def mca303(request):
    return render(request,'MCA303.html')
def mca304(request):
    return render(request,'MCA304.html')
def mca305(request):
    return render(request,'MCA305.html')
def mca307(request):
    return render(request,'MCA307.html')
def mca308(request):
    return render(request,'MCA308.html')
def mca309(request):
    return render(request,'MCA309.html')
def mca310(request):
    return render(request,'MCA310.html')
def mca401(request):
    return render(request,'MCA401.html')
def mca402(request):
    return render(request,'MCA402.html')
def mca403(request):
    return render(request,'MCA403.html')
def m(request):
    return render(request,'1.html')
def n(request):
    return render(request,'2.html')
def o(request):
    return render(request,'3.html')
def p(request):
    return render(request,'4.html')
# Create your views here.
