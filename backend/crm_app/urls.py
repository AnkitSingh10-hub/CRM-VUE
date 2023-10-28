from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard", DashboardAPI.as_view(), name="dashboard-api"),
    path("register", Register.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    path("user", UserView.as_view(), name="user"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("products", ProductAPI.as_view(), name="products"),
    path("orders", OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>", OrderDetailView.as_view(), name="orders-detail"),

]
