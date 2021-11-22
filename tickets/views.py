from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from tickets.forms import PriorityForm, LanguageForm, TicketCreate, StatusForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from tickets.models import Ticket as tickets
from django.contrib import messages
from users.views import Profile
from feedback.views import TicketMail


def Home_page(request):
    context = {"current_url": reverse('Home_page')}
    return render(request, 'tickets/Home_page.html', context)


def Pricing(request):
    context = {"current_url": reverse('Pricing')}
    return render(request, 'tickets/Pricing.html', context)


def Ticket(request):
    context = {"current_url": reverse('Ticket'), "task_priority": PriorityForm(), "language_choices": LanguageForm(), "form": TicketCreate(), "ticket_status": StatusForm()}
    return render(request, 'tickets/Ticket.html', context)


def New_Ticket(request):

    def form_valid():
        try:
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return True
        except:
            return False

    if request.method == 'POST' and request.user.is_authenticated:
        form = TicketCreate(request.POST)
        priority = PriorityForm(request.POST)
        language = LanguageForm(request.POST)
        status = StatusForm(request.POST)
        form.base_fields = {**form.base_fields, **priority.base_fields, **language.base_fields, **status.base_fields}
        form.changed_data.append(language.changed_data[0])
        if form_valid():
            # TicketMail()
            messages.success(request, 'We received your letter, check your mail')
            return Profile(request)
        else:
            messages.error(request, "Error! Ticket didn't added in base!")
    else:
        return HttpResponseRedirect(reverse('Login'))
    context = {"current_url": reverse('Ticket'), "task_priority": PriorityForm(), "language_choices": LanguageForm(), "form": TicketCreate(), "ticket_status": StatusForm()}
    return render(request, 'tickets/Ticket.html', context)


@login_required
def Ticket_list(request):
    if request.user.is_staff:
        context = {
            "current_url": reverse('Profile'),
            'tickets': tickets.objects.all()
        }
        return render(request, 'tickets/Ticket_desk.html', context)
    else:
        return Profile(request)

