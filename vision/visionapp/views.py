from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from . models import Reads, ReadGenre, language, Question, Answer
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.
import speech_recognition as sr
import pyautogui





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

def quiz(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'quiz.html', context)

def quiz_results(request):
    if request.method == 'POST':
        score = 0
        questions = Question.objects.all()
        for question in questions:
            selected_choice = request.POST.get('question'+str(question.id))
            correct_answer = Answer.objects.get(question=question)
            print(selected_choice)
            print(correct_answer)
            if selected_choice == correct_answer.answer_text:
                score += 1
        total_questions = questions.count()
        percentage = (score/total_questions)*100

        data=Answer.objects.all()

        context = {
            'score': score,
            'total_questions': total_questions,
            'percentage': percentage,
            'data':data
        }
        return render(request, 'quiz_results.html', context)
    else:
        return redirect('quiz')
    
def quiz_view(request):
    questions = Question.objects.all()
    for question in questions:
        answers = Answer.objects.filter(question=question, is_correct=True)
        if answers.exists():
            question.correct_answer = answers.first().answer_text
    context = {'questions': questions}
    return render(request, 'quiz.html', context)


