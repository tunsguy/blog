from django.shortcuts import render,redirect
from . models import Post,Comment,Topic,User,Contact
from django.db.models import Q
from django.core.paginator import Paginator
from . forms import CommentForm,ContactForm
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse

def index(request):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    posts = Post.objects.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )[0:5]
    topics = Topic.objects.all()
    context = {"posts":posts,"topics":topics}
    return render(request,"index.html",context)

def post(request,pk):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    post = Post.objects.get(id=pk)
    posts = Post.objects.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )
    topics = Topic.objects.all()
    comments = post.comment_set.all()
    newform=None
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newform =form.save(commit=False)
            newform.post = post
            newform.save()
            return redirect("post", pk=post.id)
    else:
        form = CommentForm()

    context = {"posts":posts,"topics":topics,"post":post,"comments":comments,"form":form}
    return render(request,"posts.html",context)

def category(request):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    posts = Post.objects.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )
    topics = Topic.objects.filter(name__icontains=s)
    p = Paginator(posts,2)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context = {"posts":posts,"topics":topics,"page_obj":page_obj}
    return render(request,"category.html",context)

def author(request,pk):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    user = User.objects.get(id=pk)
    posts = user.post_set.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )
    # comments = user.comment_set.all()
    topics = Topic.objects.all()
    p = Paginator(posts,2)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context = {"posts":posts,"topics":topics,"user":user,"page_obj":page_obj}
    return render(request,"author.html",context)



def blog(request):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    posts = Post.objects.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )
    topics = Topic.objects.all()
    p = Paginator(posts,2)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context = {"posts":posts,"topics":topics,"page_obj":page_obj}
    return render(request,"blog.html",context)


def about(request,pk):
    s= request.GET.get("s") if request.GET.get("s") != None else ""
    user = User.objects.get(id=pk)
    posts = user.post_set.filter(
        Q(topic__name__icontains=s)|
        Q(name__icontains=s)|
        Q(description__icontains=s)
    )
    # comments = user.comment_set.all()
    topics = Topic.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        subject = "Welcome To TunsBlog"
        message = "Our team will contact you in the next 24hrs.."
        from_email = settings.FROM_EMAIL
        email = form.cleaned_data["email"]
        email_to = email
        try:
            send_mail(subject,message,from_email,[email_to])
        except BadHeaderError:
            return HttpResponse("Invalid header found")
        return redirect("success")
    else:
        form = ContactForm()
    context = {"posts":posts,"topics":topics,"user":user,"form":form}
    return render(request,"about.html",context)

def success(request):
    return HttpResponse("message sent successfully!!!!")