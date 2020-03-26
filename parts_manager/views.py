from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.db.models import F, Q, Sum
from django.shortcuts import redirect, render

from .models import Parts, PartsInOut
from .forms import ExtractionForm


class PartsListView(generic.ListView):
    """在庫一覧。保管場所と部品でgroup byして在庫を集計。"""
    template_name = 'parts_manager/parts_list.html'
    context_object_name = 'parts_list'  # テンプレート側で参照するオブジェクト名

    def get_queryset(self):
        return (PartsInOut.objects.values('location', 'parts')
                .annotate(stock=Sum(F('warehousing') - F('shipping')))
                .values('location__code', 'location__name', 'parts_id', 'parts__code', 'parts__name', 'stock')
                .order_by('parts__code'))


class PartsDetailView(generic.DetailView):
    model = Parts
    template_name = 'parts_manager/detail.html'


class PartsInOutHistoryView(generic.ListView, FormMixin):
    """入出庫履歴と抽出フォーム"""
    model = PartsInOut
    template_name = 'parts_manager/inout_history.html'
    context_object_name = 'parts_list'
    form_class = ExtractionForm
    success_url = '/parts/inout-history'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    # def get_queryset(self):
    #     parts_list = PartsInOut.objects.filter(pk=1)
    #     return parts_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ExtractionForm'] = self.form_class
        return context


class PartsInOutCreateView(generic.CreateView):
    """入出庫履歴 新規作成"""
    model = PartsInOut
    fields = ['created', 'location', 'parts', 'warehousing', 'shipping']


class PartsInOutUpdateView(generic.UpdateView):
    """入出庫履歴 編集"""
    model = PartsInOut
    fields = ['created', 'location', 'parts', 'warehousing', 'shipping']
    template_name = 'parts_manager/edit_inout_history.html'

    # pk_url_kwarg = 'parts_inout_pk'  # URLConfでpk以外を指定したとき？
    # context_object_name = 'parts_inout'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        updates = form.save(commit=False)
        updates.updated = timezone.now()
        updates.save()
        return redirect('/parts/inout-history/')


class PartsInOutDeleteView(generic.DeleteView):
    """入出庫履歴 削除"""
    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/
    model = PartsInOut
    success_url = reverse_lazy('inout-history')
