from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeListView, EmployeeViewSet, AddressViewSet, AddressTypeViewSet, EmployeeSelfEditView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'address-types', AddressTypeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my/profile/', EmployeeSelfEditView.as_view(), name='employee_self_edit'),
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('api/', include(router.urls)),
]
