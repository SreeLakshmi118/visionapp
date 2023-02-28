from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Read, ReadGenre
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
       if request.method=='POST':
           uname=request.POST['uname']
           password=request.POST['password']
           user=auth.authenticate(username=uname, password=password)

           if user is not None:
                auth.login(request, user)
                return redirect('book')
           else:
                messages.info(request, 'Invalid Credentials')
                return redirect('index')
       return render(request, "index.html")

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            user=User.objects.create_user(username=uname, password=password)
            user.save()
            return redirect('index')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='index')
def book(request):
    obj=Read.objects.all()
    context={'obj':obj}
    for i in obj:
        print(i.name)
    return render(request, 'book.html', context)

def book (request):
    obj=Read.objects.all()
    cat=ReadGenre.objects.all()
    context={'obj':obj,'cat':cat}
    for i in obj:
        print(i.name)
    return render(request, 'book.html', context)



def showcategory(request):
    categories = Read.objects.all()
    cat=ReadGenre.objects.all()
    cats= Read.onjects.filter(genre_id=id)
    context={'cat':categories,
              'cat':cat,
              'cats':cats}
    return render(request, 'book.html', context)




