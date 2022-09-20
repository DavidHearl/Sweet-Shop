from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item_data in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        shopping_bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    grand_total = total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
