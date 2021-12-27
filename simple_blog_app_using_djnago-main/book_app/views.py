from django.shortcuts import render 
from django.http.response import HttpResponse ,HttpResponseRedirect
from.models import post ,Category ,Comment
from django.urls import reverse
# Create your views here.
def index(request):
    data= post.objects.order_by('-id')
    print(">>>>>",data)
    return render(request, 'app/home.html',{"posts":data})

def post_one(request,id):
    data= post.objects.get(id=id)
    if request.method == 'POST':
        comment_body = request.POST.get('msg')
        comment_obj = Comment(post=data , author=request.user , body = comment_body)
        comment_obj.save()
    comments=Comment.objects.filter(post=data).select_related('author')
    return render(request, 'app/first_post.html',{"post":data ,"comments":comments})
   

def search(request):
    query=request.GET.get('q')
    data=post.objects.filter(title__icontains=query)
    return render(request, 'app/search.html',{"posts":data})

def new_comment(request,id):
    comment_body = request.POST.get('msg')
    comment_obj = Comment(post= Post.objects.get(id=id) , author=request.user , body = comment_body)
    comment_obj.save()
    return HttpResponseRedirect( reverse('book_app:post_one', args=(id)) )
