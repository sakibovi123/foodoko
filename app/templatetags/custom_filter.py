from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name="cart_quantity")
def cart_quantity(product_id, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product_id.id:
            return cart.get(id)
    return 0


@register.filter(name="get_total_cart_quantity")
def get_total_cart_quantity(items, cart):
    total_quantity = 0
    for i in items:
        total_quantity += cart_quantity(i, cart)
    return total_quantity
    


@register.filter(name="cart_total")
def cart_total(product_id, cart):
    if not product_id.sale_price:
        return product_id.regular_price * cart_quantity(product_id, cart)
    else:
        return product_id.sale_price * cart_quantity(product_id, cart)



@register.filter(name="get_grand_total")
def get_grand_total(items, cart):
    total = 0
    for i in items:
        total += cart_total(i, cart)
    return total


@register.filter(name="get_sub_total")
def get_sub_total(items, cart):
    total = 0
    for i in items:
        total += cart_total(i, cart)
    return total