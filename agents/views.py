from django.shortcuts import render
from .forms import AgentModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent,UserProfile
from django.views import generic
from django.urls import reverse_lazy
from .mixins import OrganizerLoginRequiredMixin
from django.core.mail import send_mail
import random



class AgentListView(OrganizerLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentCreateView(OrganizerLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.organization = False
        user.set_password(f'{random.randint(0,100000)}')
        user.save()
        Agent.objects.create(user=user, organization=self.request.user.userprofile)
        send_mail(
            subject="You are invited to be an agent",
            message='You were added as an agent on MDEV CRM. Please come login to start working',
            from_email="admin@test.com",
            recipient_list=[user.email]

        )
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganizerLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentUpdateView(OrganizerLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return Agent.objects.filter(organization=user_profile)
    

class AgentDeleteView(OrganizerLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'
    success_url = reverse_lazy('agents:agent-list')

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
