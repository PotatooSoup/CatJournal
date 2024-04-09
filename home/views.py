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




