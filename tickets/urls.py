from django.urls import path
from tickets.views import Home_page
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tickets'
urlpatterns = [
    path('', Home_page, name='First_page')
    # path('register/', register, name='register'),
    # path('profile/', profile, name='profile'),
    # path('logout/', logout, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
