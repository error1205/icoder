
from turtle import title
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from blog.models import Post

# Create your views here.

def home(request):
    # latestPosts = Post.objects.all()
    # context = {'allPosts' : allPosts}
    return render(request, 'home/home.html')
    # return HttpResponse("This is Home")

def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse("This is about")

def contact(request):
    if request.method=='POST':
        name = request.POST['namee']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name) < 2 or len(email) < 2 or len(phone) < 10  or len(content) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "You Message Sent Sucessfully!")


    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = []
        allPostsByAuthor = []
        allPostsByContent = []
    
    else:
        allPosts = Post.objects.filter(title__icontains=query)
        allPostsByAuthor = Post.objects.filter(author__icontains=query)
        allPostsByContent = Post.objects.filter(content__icontains=query)

    if allPosts.count() == 0 and allPostsByAuthor.count() == 0 and allPostsByContent == 0:
        messages.error(request, "No Search result found. Kindly, refine your query")

    if allPosts == allPostsByContent:
        allPostsByAuthor = []
        allPostsByContent = []
        
        # params = {'allPosts':allPosts, 'query': query}

    print(allPostsByContent)
    params = {'allPosts':allPosts, 'query': query, 'allPostsByAuthor': allPostsByAuthor, 'allPostsByContent' : allPostsByContent}
    return render(request, 'home/search.html', params)
    
# Authentication APIS

def handleSignup(request):
    if request.method == 'POST':
        # Get the post method
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
       
        # check for errenous input  
        if not username.isalnum():
            messages.error(request, "username must be alphanumeric")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Password don't match")
            return redirect('/')
        # create user
        # 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.save()
        messages.success(request, "Your iCoder account has been created sucessfully.")
        return redirect('/')


    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # Get the post method
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Sucessfull")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')


    return HttpResponse('404 - Not Found')

def handleLogout(request):
        logout(request)
        messages.success(request, "Logout Sucessfull")
        return redirect('home')
    

