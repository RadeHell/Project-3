from django.views.generic import ListView
from ..models import Order

class BookListView(ListView):
    model = Order
    template_name = 'book_list.html'