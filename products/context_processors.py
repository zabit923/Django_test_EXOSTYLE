from products.models import Basket


def baskets(request):
    user = request.user
    baskets = Basket.objects.filter(user=user) if user.is_authenticated else []
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum += basket.sum()
        total_quantity += basket.quantity
    return {'baskets': baskets,
            'total_sum': total_sum,
            'total_quantity': total_quantity
            }
