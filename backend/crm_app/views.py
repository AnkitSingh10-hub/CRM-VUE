from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import Order, Customer
from .serializers import (
    OrderSerializer,
    CustomerSerializer,
    CustomUserSerializer,
    ProductSerializer,
)
import jwt, datetime
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404


# from .filters import OrderFilter
class DashboardAPI(APIView):
    def get(self, request):
        orders = Order.objects.all().order_by("-status")[:5]
        customers = Customer.objects.all()
        total_customers = customers.count()
        total_orders = Order.objects.all().count()
        delivered = Order.objects.filter(status="Delivered").count()
        pending = Order.objects.filter(status="Pending").count()
        order_serializer = OrderSerializer(orders, many=True)
        customer_serializer = CustomerSerializer(customers, many=True)

        data = {
            "customers": customer_serializer.data,
            "orders": order_serializer.data,
            "total_customers": total_customers,
            "total_orders": total_orders,
            "delivered": delivered,
            "pending": pending,
        }

        return Response(data)


class ProductAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data)

class OrderListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        # Get the data from the request
        data = request.data

        # Look up the customer and product based on the provided names
        customer_name = data.get('customer_name')
        product_name = data.get('product_name')

        customer = get_object_or_404(Customer, name=customer_name)
        product = get_object_or_404(Product, name=product_name)

        # Add the customer and product to the data before creating the order
        data['customer'] = customer.id
        data['product'] = product.id

        return self.create(request)






        
        
       

class Register(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        username = request.data["username"]

        try:
            user = CustomUser.objects.get(email=email, username=username)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

        user = CustomUser.objects.get(id=payload["id"])
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response


# #-------------------(DETAIL/LIST VIEWS) -------------------

# def dashBoard(request):
# 	orders = Order.objects.all().order_by('-status')[0:5]
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = Order.objects.all().count()
# 	delivered = Order.objects.filter(status='Delivered').count()
# 	pending = Order.objects.filter(status='Pending').count()


# 	context = {'customers':customers, 'orders':orders,
# 	'total_customers':total_customers,'total_orders':total_orders,
# 	'delivered':delivered, 'pending':pending}
# 	return render(request, 'accounts/dashBoard.html', context)

# def products(request):
# 	products = Product.objects.all()
# 	context = {'products':products}
# 	return render(request, 'accounts/products.html', context)

# def customer(request, pk):
# 	customer = Customer.objects.get(id=pk)
# 	orders = customer.order_set.all()
# 	total_orders = orders.count()


# 	orderFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = orderFilter.qs

# 	context = {'customer':customer, 'orders':orders, 'total_orders':total_orders,
# 	'filter':orderFilter}
# 	return render(request, 'accounts/customer.html', context)


# #-------------------(CREATE VIEWS) -------------------

# def createOrder(request):
# 	action = 'create'
# 	form = OrderForm()
# 	if request.method == 'POST':
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context =  {'action':action, 'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# #-------------------(UPDATE VIEWS) -------------------

# def updateOrder(request, pk):
# 	action = 'update'
# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/customer/' + str(order.customer.id))

# 	context =  {'action':action, 'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# #-------------------(DELETE VIEWS) -------------------

# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == 'POST':
# 		customer_id = order.customer.id
# 		customer_url = '/customer/' + str(customer_id)
# 		order.delete()
# 		return redirect(customer_url)

# 	return render(request, 'accounts/delete_item.html', {'item':order})
