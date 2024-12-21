from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Leads , Agent ,User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadForm,LeadModelForm,CustomUserCreateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView


from agents.mixins import OrganizerLoginRequiredMixin

import logging
from django.conf import settings
logger = logging.getLogger(__name__)




class SignupView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreateForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been created successfully!"

    def form_invalid(self, form):
        """Override form_invalid to handle form errors."""
        # Add form errors to Django messages
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def form_invalid(self, form):
        """Override form_invalid to add custom behavior when the form is invalid."""
        response = super().form_invalid(form)
        return response


class LandingPageView(TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


class LeadListView(LoginRequiredMixin,ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user

        if user.is_organization:
            queryset = Leads.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Leads.objects.filter(organization=user.agent.organization, agent__isnull=False)


            queryset = queryset.filter(agent__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organization:
            queryset = Leads.objects.filter(
                organization=user.userprofile, 
                 agent__isnull=False
            )
            context.update({
                "unassigned_leads": queryset
            })
        return context

def lead_list(request):
    leads = Leads.objects.all()
    context = {
        'leads': leads,
        'age' : 20  
    } 
    return render(request, 'leads/lead_list.html', context)



class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'


    def get_queryset(self):
        user = self.request.user

        if user.is_organization:
            queryset = Leads.objects.filter(organization=user.userprofile)
        else:
            queryset = Leads.objects.filter(organization=user.agent.organization)


            queryset = queryset.filter(agent__user=user)
        return queryset


def lead_detail(request,pk):
    lead = Leads.objects.get(pk=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(OrganizerLoginRequiredMixin,CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        messages.success(self.request, "You have successfully created a lead")
        return super(LeadCreateView, self).form_valid(form)
    

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('/leads')
    
    context = {'form': form}
    return render(request, 'leads/lead_create.html', context)

class LeadUpdateView(OrganizerLoginRequiredMixin,UpdateView):
    form_class = LeadModelForm
    template_name = 'leads/lead_update.html'
    success_url = reverse_lazy('leads:lead-list')


    def get_queryset(self):
        user = self.request.user

        return Leads.objects.filter(organization=user.userprofile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead'] = self.object
        return context


def lead_update(request,pk):
    lead = Leads.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        'lead': lead,
        'form': form
    }
        
    return render(request, 'leads/lead_update.html',context)


class LeadDeleteView(OrganizerLoginRequiredMixin,DeleteView):
    model = Leads
    template_name = 'leads/lead_delete.html'
    success_url = reverse_lazy('leads:lead-list')


    def get_queryset(self):
        user = self.request.user

        return Leads.objects.filter(organization=user.userprofile)



def lead_delete(request, pk):
    lead = Leads.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')
























# def lead_update(request, pk):
#     lead = Leads.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('The form is valid')
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')
 
#     context = {
#         'lead': lead,
#         'form': form
#     }

#     return render(request, 'leads/lead_update.html', context)

# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('The form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             Leads.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print('Successfully created')
#             return redirect('/leads')
    
#     context = {'form': form}
#     return render(request, 'leads/lead_create.html', context)