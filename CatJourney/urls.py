from home import views
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
# Use include() to add paths from the home application
from django.conf.urls import include
urlpatterns += [
    path('home/diarylist/', views.diary_list),
]


#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


