from django.shortcuts import redirect
from .models import Customer

def customer_check_session(func):
    def inner(request, *args, **kwargs):

        # If user is not logged in → redirect
        if "email" not in request.session:
            return redirect("signin")

        # Valid session → fetch customer
        try:
            request.customer = Customer.objects.get(email=request.session["email"])
        except Customer.DoesNotExist:
            return redirect("signin")

        # Continue the original view
        return func(request, *args, **kwargs)
    
    return inner
