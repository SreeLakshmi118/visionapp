from django.contrib import messages, auth
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Reads, ReadGenre, language, QuizQuestion
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.
import speech_recognition as sr
import pyautogui
from datetime import datetime, timedelta





def index(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        uname=uname.lower()
        password=password.lower()
        user=auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('index')
    return render(request, "index.html")

def register(request):
    if request.method=='POST':
        print(request.POST)
        uname=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        uname=uname.lower()
        password=password.lower()
        cpassword=cpassword.lower()
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
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print('You said:', command)
            if 'show books' in command:
                obj = Reads.objects.all()
            elif 'show genre' in command:
                gen = ReadGenre.objects.all()
                return HttpResponse(gen)
            elif 'show language' in command:
                lan = language.objects.all()
                return HttpResponse(lan)
            else:
                return HttpResponse('Sorry, I did not understand that.')
            context = {
                'obj': obj,
                'gen': gen,
                'lan': lan,
            }
            return render(request, 'book.html', context)
        except sr.UnknownValueError:
            print('Speech Recognition could not understand audio')
        except sr.RequestError as e:
            print('Could not request results from Speech Recognition service; {0}'.format(e))
    else:
        request.session['gen'] = None
        request.session['lan'] = None
        obj = Reads.objects.all()
        gen = ReadGenre.objects.all()
        lan = language.objects.all()
        context = {
            'obj': obj,
            'gen': gen,
            'lan': lan,
        }
        return render(request, 'book.html', context)


def gencust(request, id1):
    request.session['gen']=id1
    print(request.session['gen'])
    if request.session['gen'] and request.session['lan']:
        obj=Reads.objects.filter(genre=id1, language=request.session['lan'])
    else:
        obj=Reads.objects.filter(genre=id1)
    gen=ReadGenre.objects.all()
    lan=language.objects.all()
    context={
        'obj':obj,
        'gen':gen,
        'lan':lan,
    }
    return render(request, 'book.html', context)

def langcust(request, id2):
    request.session['lan']=id2
    if request.session['gen'] and request.session['lan']:
        obj=Reads.objects.filter(genre=request.session['gen'], language=id2)
    else:
        obj=Reads.objects.filter(language=id2)

    print(obj)
    gen=ReadGenre.objects.all()
    lan=language.objects.all()
    context={
        'obj':obj,
        'gen':gen,
        'lan':lan,
    }
    return render(request, 'book.html', context)


def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')
def quizview(request):
    questions_list = QuizQuestion.objects.all()
    paginator = Paginator(questions_list, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'quiz.html', {'page_obj': page_obj})


# def quiz_results(request):
#     if request.method == 'POST':
#         score = 0
#         questions = QuizQuestion.objects.all()
#         for question in questions:
#             selected_choice = request.POST.get('question'+str(question.id))
#             correct_answer = question.correct_answer
#             if selected_choice == correct_answer:
#                 score += 1
#         total_questions = questions.count()
#         percentage = (score/total_questions)*100

#         context = {
#             'score': score,
#             'total_questions': total_questions,
#             'percentage': percentage,
#         }
#         return render(request, 'quiz_results.html', context)
#     else:
#         return redirect('quiz')

def quiz_results(request):
    if request.method == 'POST':
        score=0
        cookie_dict = request.COOKIES
        questions = QuizQuestion.objects.all()
        for question in questions:
            key = str(question.id)
            value = cookie_dict.get(key)
            print(key, value)
            if value=='a':
                if question.choice1==str(question.correct_answer):
                    score+=1
            elif value == 'b':
                if question.choice2==str(question.correct_answer):
                    score+=1
            elif value =='c':
                if question.choice3==str(question.correct_answer):
                    score+=1
            else:
                pass
            
        total_questions = questions.count()
        percentage = (score/total_questions)*100

        response = HttpResponse("Cookies reset")
        cookie_dict = request.COOKIES
        for key, value in cookie_dict.items():
            response.set_cookie(key, '',expires=(datetime.utcnow() - timedelta(days=1)))
        context = {
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage,
        }
        return render(request, 'quiz_results.html', context)
    else:
        return redirect('quiz')
            





def quiz_view(request):
    questions = QuizQuestion.objects.all()
    context = {'questions': questions}
    return render(request, 'start_quiz.html', context)

