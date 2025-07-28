from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Product
from django.urls import reverse_lazy

# Top
class TopView(TemplateView):
    template_name = "top.html"
    
#ListView
class ProductListView(ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3

# 商品の新規作成
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

# 商品の編集
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

# 商品の削除
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

# 商品詳細画面
class ProductDetailView(DetailView):
    model = Product