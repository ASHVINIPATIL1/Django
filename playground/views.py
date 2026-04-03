# from django.shortcuts import render
# from django.db.models import Q, F, DecimalField, Value, Func, Count, ExpressionWrapper
# from django.db.models.aggregates import Count, Min, Max, Avg, Sum
# # from django.http import HttpResponse
# from store.models import Product, OrderItem, Customer


# # Create your views here.

# def say_hello(request):

#     # queryset = Product.objects.filter(unit_price__gt=20)

#     # queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__gt=20))

#     # queryset = Product.objects.order_by('unit_price', '-title').reverse()

#     # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct().order_by())

#     # queryset = Customer.objects.annotate(
#     #     full_name=Func(F('first_name'), Value(''), F('last_name'), function='CONCAT')
#     # )

#     # results = Product.objects.aggregate(Count('id'), min_price=Min('unit_price'))

#     # queryset = Customer.objects.annotate(is_new=Value(True))

#     discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field = DecimalField())
#     queryset = Product.objects.annotate(
#         discounted_price = discounted_price
#     )

#     return render(request, 'hello.html', {'name': 'Ashvini', 'results' : queryset})

from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from tags.models import Tag, TaggedItem
from store.models import Product


def say_hello(request):
    # TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'Ashvini'})   