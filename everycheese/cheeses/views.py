from django.db import models
from django.views.generic import ListView, DetailView

from .models import Cheese

# Create your views here.


class CheeseListView(ListView):
    model = Cheese
