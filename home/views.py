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
class DiaryListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Diary
    paginate_by = 10




def post(request):
    # 如果是 POST 请求，则处理提交的表单数据
    if request.method == 'POST':
        # 处理表单提交逻辑，保存日记等
        # 你可以在这里使用表单数据创建新的 Diary 对象

        # 重定向到其他页面，比如发布成功页面或者详情页
        # 这里假设你有一个名为 'diary-detail' 的 URL 名称，用于显示日记详情
        return redirect('diary-detail', pk=new_diary.pk)  # 假设 new_diary 是你新创建的 Diary 对象

    # 如果是 GET 请求，则渲染发布日记页面的模板
    return render(request, 'post.html')

def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})


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