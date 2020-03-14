from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from user.forms import EventRegistrationForm
from django.urls import reverse, reverse_lazy
from user.models import EventRegistration
from django.http import HttpResponseRedirect

# Create your views here.

def index (request):
    return render (request, 'user/index.html')

def about (request):
    return render (request, 'user/about.html')

def contact (request):
    return HttpResponse ('Contact')

def help (request):
    return HttpResponse ('help')

def register (request):
    return render (request, 'user/register.html')

def report (request):
    return HttpResponse ('report')

def confirm (confirm):
    return HttpResponse ('report')

def Meeting1 (request):
    return HttpResponse ('meeting 1')

def Meeting2 (request):
    return HttpResponse ('meeting 2')

def goodluck (request):
    return HttpResponse ('goodluck')

def bill (request):
    return HttpResponse ('bill')

def Register (request):
    return render (request, 'user/register.html')

def track (request):
    return HttpResponse ('report')

def login_signUp (request):
    return HttpResponse ('login / sign Up')

class RegisterView(CreateView):
    form_class = EventRegistrationForm
    template_name = 'user/register.html'
    # must be lazy loading because urls are not loaded yet, otherwise crash!
    success_url = reverse_lazy('Login/Sign Up')

    def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))
        return super(RegisterView, self).form_valid(form)

# class ProjectCreateView(CreateView):
# 	# make a form based on this model
#     model = EventRegistration
#     # if we only want to edit these two fields
#     # fields = ('first_name', 'last_name')
#     fields = '__all__'

#     # render this html file, pass a form object to that file
#     template_name = 'user/register.html'

#     def form_valid(self, form):

#         model = form.save(commit=False)
#         # model.submitted_by = self.request.user
#         model.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse("Login/Sign Up")

