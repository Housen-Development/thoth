from django.views import generic, View
from django.db.models import F, Q, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Parts, PartsInOut
from .forms import PartsInOutForm


class PartsListView(generic.ListView):
    """在庫一覧。保管場所と部品でgroup byして在庫を集計。"""
    template_name = 'parts_manager/parts_list.html'
    context_object_name = 'parts_list'

    def get_queryset(self):
        return (PartsInOut.objects.values('location', 'parts')
                .annotate(stock=Sum(F('warehousing') - F('shipping')))
                .values('location__code', 'location__name', 'parts_id', 'parts__code', 'parts__name', 'stock')
                .order_by('parts__code'))


class PartsDetailView(generic.DetailView):
    model = Parts
    template_name = 'parts_manager/detail.html'


class PartsInOutHistoryView(generic.ListView):
    # https://noumenon-th.net/programming/2019/12/18/django-search/ 参考
    """入出庫履歴"""
    model = PartsInOut
    template_name = 'parts_manager/inout_history.html'
    context_object_name = 'parts_list'

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            parts_list = PartsInOut.objects.filter(
                Q(parts__code__icontains=q_word) | Q(parts__name__icontains=q_word))
        else:
            parts_list = PartsInOut.objects.all()
        return parts_list


class EditPartsInOutFormView(View):
    form_class = PartsInOutForm
    initial = {
        'key': 'value'
    }
    template_name = 'parts_manager/edit_inout_history.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
