from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import HttpResponse
from .models import Comment

# Create your views here.

@login_required(login_url='login_user')
def home(request):
   if not request.user.is_authenticated:
      return redirect('user_login')   
   blogs=Article.objects.all()
   keyword = request.GET.get('keyword')
   
   if keyword:
      blogs = blog.filter(title__icontains=keyword)
   context = {
      'blogs':blogs,
      'choices':Article.genre_choices
   }
   return render(request,'index.html',context)

@login_required(login_url='login_user')
def create(request):
   if request.method == 'POST':
      tt=request.POST.get('t')
      cc=request.POST.get('c')
      genre=request.POST.get('genre')
      image = request.FILES.get('cover_image')
      Article.objects.create(
         title=tt,
         content=cc,
         cover_image=image,
         author=request.user,
         genre=genre
      )
      return redirect('index')
      
   return render (request,'create.html',{'choices':Article.genre_choices})

@login_required(login_url='login_user')
def details(request,id):
   article=Article.objects.get(id=id)
   comments = Comment.objects.filter(article=article)
   context = {
      'blog':article,
      'comments':comments

   }
   return render(request,'details.html',context)   


def edit(request, id):
    article = Article.objects.get(id=id)
    
    if article.author != request.user:
        return HttpResponse('You are not authorized to perform this action')
    
    if request.method == 'POST':
        title = request.POST.get('t')
        content = request.POST.get('c')
        article.title = title
        article.content = content
        article.save()
        return redirect('edit', article.id)
    
    context = {
        'article': article
    }
   
    return render(request, 'edit.html', context)


def delete(request,id):
   article=Article.objects.get(id=id)
   if request.method == 'POST':
      article.delete()
      return redirect('index')
   context = {
      'article':article
   }   
   return render(request,'delete.html',context)

def comment_post(request,article_id):
   article = Article.objects.get(id=article_id)
   if request.method == 'POST':
      comment = request.POST.get('comment')
      Comment.objects.create(
         text=comment,
         comment_author=request.user,
         article=article
      )
   return redirect('details',article_id)   

def comment_delete(request,id):
   comment = Comment.objects.get(id=id)
   article_id = comment.article.id
   comment.delete()
   return redirect('details',article_id)

def comment_edit(request,id):
   comment=Comment.objects.get(id=id)
   abc=comment.article
   if request.method == 'POST':
      text = request.POST.get('comment')
      comment.text = text
      comment.save()
      return redirect('details',abc.id)
   comments = Comment.objects.filter(article=abc)
   context = {
      'blog':abc,
      'comments':comments,
      'cmd':comment,
      'edit':True
   }
   return render(request,'details.html',context)
   