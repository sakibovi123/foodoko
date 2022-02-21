from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name="cart_quantity")
def cart_quantity(item_id, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == item_id.id:
            return cart.get(id)
    return False


@register.filter(name="cart_total")
def cart_total(item_id, cart):
    return item_id.item_price * cart_quantity(item_id, cart)



@register.filter(name="get_grand_total")
def get_grand_total(items, cart):
    total = 0
    for i in items:
        total += cart_total(i, cart)
    return total