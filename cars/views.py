from django.http import request
from cars.forms import CarModelForm 
from cars.models import Car
from django.views.generic import ListView, CreateView, DetailView, UpdateView

# class based views (CBVs)
class CarsListView(ListView): 
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model') # super para quando quiser usar a classe 'pai'
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarsCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    sucess_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    sucess_url = '/cars/'