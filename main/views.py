from email import message
from multiprocessing import context
import datetime
from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from main.models import Poll, Answers, Profile
from .forms import pollForm

# Create your views here.
@login_required(login_url='/login/')
def home(request):

    polls = Poll.objects.all()
    context = {'polls': polls}
    
    return render(request, "main/home.html", context)


@login_required(login_url='/login/')
def make_poll(request):
    form = pollForm()
    context = {'form':form}
    if request.method == 'POST':
        form = pollForm(request.POST)   
        user = request.user   
        if user.profile.q_counts < 5:    
            if form.is_valid():                         
                question= form.cleaned_data['question']
                option_1= form.cleaned_data['opt1']
                option_2= form.cleaned_data['opt2']
                option_3= form.cleaned_data['opt3']
                option_4= form.cleaned_data['opt4']  
                created  = datetime.datetime.now()         
                poll_obj = Poll.objects.create(question = question,  user=user, created=created )
                poll_obj.save()
                answers = Answers.objects.create(option_1=option_1, option_2=option_2, 
                option_3=option_3, option_4=option_4 , question= poll_obj)
                answers.save()
                
                messages.success(request, f'{user.profile.que_counts} - A Poll has been created')
                return redirect('profile')
        else:
            messages.warning(request, "You have reached maximum limit for Making New  Polls")
            return redirect('profile')
        
    return render(request, "main/make_poll.html", context)


@login_required(login_url='/login/')
def answer(request, pk):
    pol = Poll.objects.get(id = pk)
    if request.method == "POST":
        form = request.POST
        if form["poll"] == "1":
            pol.count_1 += 1
        elif form["poll"] == "2":
            pol.count_2 += 1
        elif form["poll"] == "3":
            pol.count_3 += 1
        elif form["poll"] == "4":
            pol.count_4 += 1
        pol.total += 1
        pol.save()

        messages.success(request, f' A Poll has been answered -{pol.question}')
    return redirect('home')



def log_out(request):
    logout(request)
    messages.info(request, 'You are logged out')  
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
    poll = Poll.objects.filter(user=request.user)
    
    return render(request, "main/profile.html", {"polls":poll})
