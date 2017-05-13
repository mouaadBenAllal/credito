from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import ContactForm, WerknemersForm, UpdateForm
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Werknemer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


# View die homepage laat zien.
def home(request):
    return render(request, 'home/home.html')


# Functie die alle werknemers uit de db haalt.
def werknemers_list(request):
    queryset_list = Werknemer.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(Q(voornaam__icontains=query) | Q(achternaam__icontains=query))

    paginator = Paginator(queryset_list, 4)  # Show 4 werknemers per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, "werknemer/werknemerlist.html", context)


# Class based view om werknemers aan te maken.
class WerknemerCreateView(CreateView):
    form_class = WerknemersForm
    template_name = 'werknemer/werknemercreate.html'
    success_url = reverse_lazy('werknemers_list')

    #
    # def form_valid(self, form_class):
    #     """
    #     If the form is valid, save the associated model.
    #     """
    #     if form_class.is_valid():
    #         subject = 'Welkom bij Credito!'
    #         message = form_class.cleaned_data['voornaam']
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = [Werknemer.email, settings.EMAIL_HOST_USER]
    #
    #         send_mail(subject, message, from_email, to_list, fail_silently=False)
    #     self.object = form_class.save()
    #     return super(ModelFormMixin, self).form_valid(form_class)
    #


# Class based view om werknemers te updaten.
class WerknemerUpdate(UpdateView):
    model = Werknemer
    form_class = UpdateForm
    template_name = 'werknemer/werknemerupdate.html'
    success_url = reverse_lazy('werknemers_list')


# Class based view om werknemer te verwijderen.
class WerknemerDelete(DeleteView):
    model = Werknemer
    template_name = 'werknemer/werknemerdelete.html'
    success_url = reverse_lazy('werknemers_list')


# Functie om contact pagina te laten zien samen met de aangegeven form.
def contact(request):
    form_class = ContactForm

    # if request.method == 'POST':
    #     form = form_class(data=request.POST)
    #     if form.is_valid():
    #         subject = 'Nieuwe gebruiker aangemaakt.'
    #         message = 'Welkom bij Credito!'
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = [Werknemer.email, settings.EMAIL_HOST_USER]
    #
    #         send_mail(subject, message, from_email, to_list, fail_silently=False)
    return render(request, 'home/contact.html', {
        'form': form_class,
    })





