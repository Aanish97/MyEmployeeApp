from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('employee_list')  # or any page after login

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # auto-login after registration
        return response
