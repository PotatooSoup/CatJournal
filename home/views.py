from django.shortcuts import render

# Create your views here.
from .models import Diary, Author, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_diarys=Diary.objects.all().count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    #获得最新的三篇日记
    latest_diaries = Diary.objects.order_by('-date')[:3]
    context={
        'num_diarys':num_diarys,
        'num_authors':num_authors,
        'latest_diaries': latest_diaries
        }

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context
    )


from django.views import generic
from .models import Diary
class DiaryListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Diary
    paginate_by = 10


from django import forms
from . import models
from django.shortcuts import redirect

class PostModelForm(forms.ModelForm):
    class Meta: 
        model = models.Diary
        fields = ["title","author","genre","summary","date","image"]
        widgets ={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "summary":forms.Textarea(attrs={"class":"form-control","rows":"5"}),
            
        }


def model_form_add(request):
    """添加帖子 model form"""
    if request.method == "GET":
        form = PostModelForm()
        return render(request,'post_mf_add.html',{"form":form})

    form = PostModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/home/diarys/')
    else:
        print(form.errors)



class DiaryDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Diary

class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


class GenreDetailView(generic.DetailView):
    """Generic class-based detail view for a genre."""
    model = Genre

class GenreListView(generic.ListView):
    """Generic class-based list view for a list of genres."""
    model = Genre
    paginate_by = 10


def diary_list(request):
    return 

from django.contrib.auth.decorators import login_required

from django.db.models import Q



# def Register(request):
#     if request.method=="POST":   
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 != password2:
#             messages.error(request, "密码不匹配.")
#             return redirect('/register')
 
#         user = User.objects.create_user(username, email, password1)
#         user.save()
#         return render(request, 'login.html')  
#     return render(request, "register.html")


# def Login(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Credentials")
#         return render(request, 'blog.html')   
#     return render(request, "login.html")