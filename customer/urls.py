from django.urls import path
from .views import *

urlpatterns = [                          
    path("",index, name = "home"),
    path("contact/",contact, name = "contact"),
    path("customer_email_register/",customer_email_register, name = "customer_email_register"),
    path("customer_otp/",customer_otp, name = "customer_otp"),
    path("signup/",signup, name = "signup"),
    path("signin/",signin, name = "signin"),
    path("signout/",signout, name = "signout"),
    path("profile/",profile, name = "profile"),
    path("change_password/",change_password, name = "change_password"),
    path("add-to-wishlist/<int:pk>",add_to_wishlist, name = "add_to_wishlist"),
    path("wishlist-cart/",wishlist_cart, name = "wishlist_cart"),
    path("delete-wishlist-item/<int:pk>/", delete_wishlist_item, name="delete_wishlist_item"),
    path("delete-cart-item/<int:pk>/", delete_cart_item, name="delete_cart_item"),
    path("clear-wishlist/", clear_wishlist, name="clear_wishlist"),
    path("clear-cart/", clear_cart, name="clear_cart"),
    path("product-cart/",product_cart_display, name = "product_cart_display"),
    path("cart-product/<int:pk>/",add_to_cart, name = "add_to_cart"),
    path("blog/", blog_page, name = "blog"),
    path("blog/<int:pk>/", blog_detail, name="blog_detail"),
    path("create-checkout-session/", create_checkout_session, name="create_checkout_session"),
    path("payment-success/", payment_success, name="payment_success"),
    path("payment-cancel/", payment_cancel, name="payment_cancel"),


]