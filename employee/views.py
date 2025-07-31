from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from rest_framework import viewsets, permissions

from .forms import EmployeeForm
from .models import Employee, Address, AddressType
from .serializers import EmployeeSerializer, AddressSerializer, AddressTypeSerializer
from user.permissions import IsAdminOrSelf
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from .models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrSelf]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminOrSelf]


class AddressTypeViewSet(viewsets.ModelViewSet):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
    permission_classes = [permissions.IsAdminUser]



class EmployeeListView(LoginRequiredMixin, TemplateView):
    template_name = 'employees/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sort_by = self.request.GET.get('sort', 'user__first_name')
        employees = Employee.objects.select_related('user').order_by(sort_by)
        paginator = Paginator(employees, 10)
        page = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page)
        context['employees'] = context['page_obj']
        context['is_paginated'] = paginator.count > 10
        return context


class EmployeeSelfEditView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/self_edit.html'

    def get_object(self, queryset=None):
        try:
            return self.request.user.employee
        except Employee.DoesNotExist:
            return redirect('employee_list')  # or raise Http404

    def get_success_url(self):
        return self.object.get_absolute_url()  # or use reverse_lazy('employee_detail', kwargs={'pk': self.object.pk})
