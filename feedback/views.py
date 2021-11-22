from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.contrib import messages
from feedback.forms import NewFeedBack
from django.core.mail import send_mail, BadHeaderError
from SB.settings import DEFAULT_FROM_EMAIL
from feedback.models import FeedBack as feed
from django.contrib.auth.decorators import login_required
from users.views import Profile


def FeedBack(request):
    if request.method == 'POST':
        form = NewFeedBack(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            message = 'Hello! We received your letter: "\n"'+form.cleaned_data['message']
            try:
                send_mail(f'{username} от {email}', message, DEFAULT_FROM_EMAIL, email)
                messages.success(request, "We received your letter, check your mail")
            except BadHeaderError:
                messages.error(request, "Error!")
    context = {"current_url": reverse('Home_page')}
    return render(request, 'tickets/Home_page.html', context)


def TicketMail(request, form):
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    message = 'Hello! We received your letter: "\n"' + form.cleaned_data['message']
    try:
        send_mail(f'{username} от {email}', message, DEFAULT_FROM_EMAIL, email)
        return True
    except BadHeaderError:
        messages.error(request, "Error!")
        return False


@login_required
def FeedDesk(request):
    if request.user.is_staff:
        context = {
            "current_url": reverse('Profile'),
            'feed': feed.objects.all()
        }
        return render(request, 'feed.html', context)
    else:
        return Profile(request)

