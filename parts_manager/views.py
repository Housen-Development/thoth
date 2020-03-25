from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.db.models import F, Q, Sum
from django.shortcuts import redirect

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
    template_name = 'parts_manager/detail.html'
    model = Parts


class PartsInOutHistoryView(generic.ListView, FormMixin):
    """入出庫履歴と抽出フォーム"""
    template_name = 'parts_manager/inout_history.html'
    model = PartsInOut
    form_class = ExtractionForm
    success_url = '/parts/inout_history'
    context_object_name = 'parts_list'

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     self.object_list = self.get_queryset()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # FormView inherits TemplateResponseMixin so template_name can be used here.
        # The default implementation for form_valid() simply redirects to the success_url.
        return super().form_valid(form)

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            parts_list = PartsInOut.objects.filter(
                Q(parts__code__icontains=q_word) | Q(parts__name__icontains=q_word))
        else:
            parts_list = PartsInOut.objects.all()
        return parts_list


class PartsInOutCreateView(generic.CreateView):
    """入出庫履歴 新規作成"""
    model = PartsInOut
    fields = ['created', 'location', 'parts', 'warehousing', 'shipping']


class PartsInOutUpdateView(generic.UpdateView):
    """入出庫履歴 編集"""
    template_name = 'parts_manager/edit_inout_history.html'
    model = PartsInOut
    fields = ['created', 'location', 'parts', 'warehousing', 'shipping']

    # pk_url_kwarg = 'parts_inout_pk'  # URLConfでpk以外を指定したとき？
    # context_object_name = 'parts_inout'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        updates = form.save(commit=False)
        updates.updated = timezone.now()
        updates.save()
        return redirect('/parts/inout_history/')


class PartsInOutDeleteView(generic.DeleteView):
    """入出庫履歴 削除"""
    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/
    model = PartsInOut
    success_url = reverse_lazy('inout_history')
