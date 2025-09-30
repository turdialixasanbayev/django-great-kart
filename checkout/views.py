from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from .models import Cart, CartItem, Order, OrderItem
from store.models import Product


class CartPageView(View):
    template_name = 'cart.html'

    def get(self, request):
        cart = get_object_or_404(Cart, user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        cart_total_price = cart.cart_total_price
        cart_sub_total_price = cart.cart_sub_total_price

        context = {
            "cart": cart,
            "cart_items": cart_items,
            "cart_total_price": cart_total_price,
            "cart_sub_total_price": cart_sub_total_price,
        }

        return render(request=request, template_name=self.template_name, context=context)


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def get(self, request, pk):
        url = request.META.get("HTTP_REFERER")
        product = get_object_or_404(Product, pk=pk, is_active=True)
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if cart_created:
            messages.success(request, "Cart created")
        if item_created:
            messages.success(request, "Item added to cart")
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect(url)


@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def get(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user, is_active=True)
        cart = cart_item.cart
        cart_item.delete()
        messages.success(request, "Item removed from cart")
        other_items = CartItem.objects.filter(cart=cart, is_active=True).exists()
        if not other_items:
            cart.delete()
            messages.info(request, "Cart deleted because it was empty")
            return redirect('home')


@method_decorator(login_required, name='dispatch')
class OrderPageView(View):
    def get(self, request):
        cart = get_object_or_404(Cart, user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        sub_total = cart.cart_sub_total_price
        total = cart.cart_total_price

        context = {
            'cart': cart,
            'cart_items': cart_items,
            'sub_total': sub_total,
            'total': total,
        }

        return render(request, 'place-order.html', context)

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        notes = request.POST.get('notes', "")

        if first_name and last_name and email and phone_number and address:
            order = Order.objects.create(
                user=request.user,
                status='new',
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                notes=notes
            )
            messages.success(request, "Your order has been created.")
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.discount_price,
                )
            cart.delete()
            messages.success(request, "Your order has been placed successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please fill in all fields.")
            return redirect("order")
