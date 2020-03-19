from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Parts, PartsInOut


class PartsListView(generic.ListView):
    template_name = 'parts_manager/parts_list.html'
    context_object_name = 'partslist'

    def get_queryset(self):
        """クエリセットを用意"""
        return PartsInOut.objects.all()


class PartsDetailView(generic.DetailView):
    model = Parts
    template_name = 'parts_manager/parts_detail.html'
