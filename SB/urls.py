from django.contrib import admin
from django.urls import path, include
from tickets.views import Home_page, Pricing, Ticket, Ticket_list, New_Ticket
from users.views import Login, Logout, Registration, Profile
from django.conf import settings
from django.conf.urls.static import static
from feedback.views import FeedDesk

base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
app_name = 'SB'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home_page, name='Home_page'),
    path('pricing/', Pricing, name='Pricing'),
    path('ticket/', Ticket, name='Ticket'),
    path('login/', Login, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('registration/', Registration, name='Registration'),
    path('profile/', Profile, name='Profile'),
    path('ticket_table/', Ticket_list, name='Ticket_list'),
    path('feed_table/', FeedDesk, name='Feed_list'),
    path('new_ticket/', New_Ticket, name='New_Ticket'),
    path('', include('chat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
