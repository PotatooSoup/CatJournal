from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('diarys/', views.DiaryListView.as_view(), name='diarys'),
    path('diary/<int:pk>', views.DiaryDetailView.as_view(), name='diary-detail'),
    path('post/',views.post, name='post'),
]

