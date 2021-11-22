from django.urls import path
from feedback.views import NewFeedBack

urlpatterns = [
    path('', NewFeedBack, name='Feed'),
]
