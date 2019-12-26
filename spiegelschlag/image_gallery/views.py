from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Category, Image
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.
class IndexView(generic.ListView):
    template_name = "image_gallery/index.html"
    context_object_name = "all_categories"

    def get_queryset(self):
        """Return the last five published questions (not including
            those set in the future)"""
        return Category.objects.all()
