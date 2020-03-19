from django.shortcuts import get_object_or_404, render

from .models import Parts, PartsInOut


def parts_list(request):
    partslist = PartsInOut.objects.order_by('parts__name')
    context = {'partslist': partslist}
    return render(request, 'parts_manager/parts_list.html', context)


def parts_detail(request, parts_id):
    parts = get_object_or_404(Parts, pk=parts_id)
    return render(request, 'parts_manager/parts_detail.html', {'parts': parts})
