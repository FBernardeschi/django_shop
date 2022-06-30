from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ItemForm
from .models import Item, Rubric


class ItemCreateView(CreateView):
    template_name = 'my_shop/create.html'
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def index(request):
    items = Item.objects.all()
    rubrics = Rubric.objects.all()
    context = {"items": items, 'rubrics': rubrics}
    return render(request, "my_shop/index.html", context)

def by_rubric(request, rubric_id):
    items = Item.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'items': items, 'rubrics': rubrics, "current_rubric": current_rubric}
    return render(request, 'my_shop/by_rubric.html', context)
