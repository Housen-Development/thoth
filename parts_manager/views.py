from django.views import generic
from django.db.models import F, Sum

from .models import Parts, PartsInOut


class PartsListView(generic.ListView):
    template_name = 'parts_manager/parts_list.html'
    context_object_name = 'parts_list'

    def get_queryset(self):
        """保管場所と部品でgroup byして在庫を集計"""
        return (PartsInOut.objects.values('location', 'parts')
                .annotate(stock=Sum(F('warehousing') - F('shipping')))
                .values('location__code', 'location__name', 'parts_id', 'parts__code', 'parts__name', 'stock')
                .order_by('parts__code'))


class PartsDetailView(generic.DetailView):
    model = Parts
    template_name = 'parts_manager/parts_detail.html'
