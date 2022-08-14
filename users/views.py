from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.utils import timezone
from django.db.models import F
from datetime import datetime, timedelta
from .models import Profile
from .models import Post
from django.http import request

user = User.objects


def register(request):
    if(request.method == 'POST'):
        if(request.POST['password1'] == request.POST['password2']):
            try:
                global user
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'users/Register_Page.html', {'error':'UserName is already exist'})
            except:
                user = User.objects.create_user(username = request.POST['username'],
                 email = request.POST['email'],
                 password = request.POST['password1'])
                user_profile = Profile()
                user_profile.user = user
                user_profile.gender = request.POST['gender']
                user_profile.rollno = request.POST['rollno']
                user_profile.bloodgroup = request.POST['bloodgroup']
                user_profile.lastblooddonationdate = request.POST['lastblooddonationdate']
                user_profile.phonenumber = request.POST['phonenumber']
                user_profile.currentlocation = request.POST['currentlocation']
                user_profile.save()
                return redirect('http://127.0.0.1:8000/login/')
        else:
            return render(request, 'users/Register_Page.html', {'error':'Password should be matched'})
    else:
        return render(request, 'users/Register_Page.html')




def login(request):
    if(request.method=='POST'):
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if(user is not None):
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000')
        else:
            return render(request, 'users/Login_Page.html',{'error': 'UserName and Password didn\'t match'})
    else:
        return render(request, 'users/Login_Page.html')






@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'blog/Welcome_Page.html')





@login_required
def blood_request(request):

    context = {
        'posts' : Post.objects.order_by('-posteddatetime'),
        'profiles' : Profile.objects.all()
    }
    
    if(request.method == 'POST'):
        user_post = Post()
        user_post.user = request.user
        user_post.posttitle = request.POST['posttitle']
        user_post.bloodgroup = request.POST['bloodgroup']
        user_post.howmanybagsofblood = request.POST['howmanybagsofblood']
        user_post.patientdisease = request.POST['patientdisease']
        user_post.admittedhospitalname = request.POST['admittedhospitalname']
        user_post.deadlinedate = request.POST['deadlinedate']
        user_post.deadlinetime = request.POST['deadlinetime']
        user_post.currentlocation = request.POST['currentlocation']
        user_post.phonenumber = request.POST['phonenumber']
        user_post.relationwithruetians = request.POST['relationwithruetians']
        user_post.posteddatetime = timezone.now()+timedelta(hours=6)
        user_post.save()
        return redirect('http://127.0.0.1:8000/blood_request',context)
    else:
        return render(request, 'users/Blood_Request_Page.html',context)





@login_required
def profile(request):
    context = {
        'posts' : Post.objects.order_by('-posteddatetime')
    }
    return render(request, 'users/Profile_Page.html',context)





@login_required
def post_update(request, post_id):
    context = {
        'posts' : Post.objects.order_by('-posteddatetime')
    }

    post = get_object_or_404(Post, pk = post_id)

    if(request.method == 'POST'):
        Post.objects.filter(pk = post_id).update(user = request.user)
        Post.objects.filter(pk = post_id).update(posttitle = request.POST['posttitle'])
        Post.objects.filter(pk = post_id).update(bloodgroup = request.POST['bloodgroup'])
        Post.objects.filter(pk = post_id).update(howmanybagsofblood = request.POST['howmanybagsofblood'])
        Post.objects.filter(pk = post_id).update(patientdisease = request.POST['patientdisease'])
        Post.objects.filter(pk = post_id).update(admittedhospitalname = request.POST['admittedhospitalname'])
        Post.objects.filter(pk = post_id).update(deadlinedate = request.POST['deadlinedate'])
        Post.objects.filter(pk = post_id).update(deadlinetime = request.POST['deadlinetime'])
        Post.objects.filter(pk = post_id).update(currentlocation = request.POST['currentlocation'])
        Post.objects.filter(pk = post_id).update(phonenumber = request.POST['phonenumber'])
        Post.objects.filter(pk = post_id).update(relationwithruetians = request.POST['relationwithruetians'])
        Post.objects.filter(pk = post_id).update(posteddatetime = timezone.now()+timedelta(hours=6))
        return redirect("/blood_request",context)
    else:
        return render(request, 'users/Post_Update.html', {'post' : post})





@login_required
def post_delete(request, post_id): 
    post = get_object_or_404(Post, pk = post_id)
    if(request.method == "POST"):
        post.delete()
        return redirect('user-blood_request')
    else:
        return render(request, 'users/Post_Delete_Page.html', {'post' : post})


