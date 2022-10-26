from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Rim
from .forms import TireForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', {
    'cars': cars
    })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  id_list = car.rims.all().values_list('id')
  rims_car_doesnt_have = Rim.objects.exclude(id__in=id_list)
  tire_form = TireForm()
  return render(
    request,
    'cars/detail.html',
    {
      'car': car, 
      'tire_form': tire_form,
      'rims': rims_car_doesnt_have
    }
  )

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'
  

class CarUpdate(UpdateView):
  model = Car
  fields = ['model','description', 'age']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_tire(request, car_id):
  # create a FeedingForm instance using
  # the data that was submitted via the form
  form = TireForm(request.POST)
  # validate the form
  if form.is_valid():
    # can't save the form/object to the db
    # until we've assigned a cat_id
    new_tire= form.save(commit=False)
    new_tire.car_id = car_id
    new_tire.save()
  return redirect('detail', car_id=car_id)

def assoc_rim(request, car_id, rim_id):
  Car.objects.get(id=car_id).rims.add(rim_id)
  return redirect('detail', car_id=car_id)

class RimList(ListView):
  model = Rim

class RimDetail(DetailView):
  model = Rim

class RimCreate(CreateView):
  model = Rim
  fields = '__all__'

class RimUpdate(UpdateView):
  model = Rim
  fields = ['name', 'color']

class RimDelete(DeleteView):
  model = Rim
  success_url = '/rims/'