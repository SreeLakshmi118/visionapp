from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Reads, ReadGenre, language
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

# @login_required(login_url='index')
 
def book(request):
    request.session['gen']=None
    request.session['lan']=None
    obj=Reads.objects.all()
    gen=ReadGenre.objects.all()
    lan=language.objects.all()
    context={
        'obj':obj,
        'gen':gen,
        'lan':lan,
    }
    return render(request, 'book.html', context)

def gencust(request, id):
    request.session['gen']=id
    if request.session['gen'] and request.session['lan']:
        obj=Reads.objects.filter(genre=id, language=request.session['lan'])
    else:
        obj=Reads.objects.filter(genre=id)
    gen=ReadGenre.objects.all()
    lan=language.objects.all()
    context={
        'obj':obj,
        'gen':gen,
        'lan':lan,
    }
    return render(request, 'book.html', context)

def langcust(request, id):
    request.session['lan']=id
    if request.session['gen'] and request.session['lan']:
        obj=Reads.objects.filter(genre=request.session['gen'], language=id)
    else:
        obj=Reads.objects.filter(language=id)
    gen=ReadGenre.objects.all()
    lan=language.objects.all()
    context={
        'obj':obj,
        'gen':gen,
        'lan':lan,
    }
    return render(request, 'book.html', context)









