from .models import BoardModel
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy




def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            login(request, user)
            return redirect('list')
            #return render(request,'signup.html',{'some':100})
        except IntegrityError:
            return render(request,'signup.html',{'error':'ユーザー名が重複しています'})
    return render(request,'signup.html',{'some':100})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
            # Redirect to a success page.
        else:
            return render(request,'login.html',{'context':'not logged in'})
            # Return an 'invalid login' error message.
            
    return render(request,'login.html',{})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')
    # Redirect to a success page.

@login_required
def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk = pk)
    return render(request,'detail.html',{'object':object})

def goodfunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.good += 1
        object.readtext = object.readtext + ' ' + username
        object.save()
    return redirect('list')

class CreatePost(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title','content','auther','snsimage')
    success_url = reverse_lazy('list')
    
# Create your views here.

