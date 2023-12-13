from django import template

register = template.Library()

@register.filter(name='total_price')
def total_price(products):
    total = sum(product.Price + product.Quantity for product in products)
    return f'{total:,.2f}'
