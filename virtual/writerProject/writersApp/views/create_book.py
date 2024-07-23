from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import Order
from ..forms import BookForm

class BookCreateView(CreateView):
    model = Order
    form_class BookForm
    template_name = "book_form.html"
    success_url = reverse_lazy('book_list')