<template>
	<br>

	<div class="row">
		<div class="col">
			<div class="col-md">
				<div class="card text-center text-white  mb-3" id="total-orders">
					<div class="card-header">
						<h5 class="card-title">Total Orders</h5>
					</div>
					<div class="card-body">
						<h3 class="card-title">{{ totalOrders }}</h3>
					</div>
				</div>
			</div>
		</div>

		<div class="col">
			<div class="col-md">
				<div class="card text-center text-white  mb-3" id="orders-delivered">
					<div class="card-header">
						<h5 class="card-title">Orders Delivered</h5>
					</div>
					<div class="card-body">
						<h3 class="card-title">{{ delivered }}</h3>
					</div>
				</div>
			</div>
		</div>

		<div class="col">
			<div class="col-md">
				<div class="card text-center text-white  mb-3" id="orders-pending">
					<div class="card-header">
						<h5 class="card-title">Orders Pending</h5>
					</div>
					<div class="card-body">
						<h3 class="card-title">{{ pending }}</h3>
					</div>
				</div>
			</div>
		</div>
	</div>

	<br>

	<div class="row">
		<div class="col-md-5">
			<h5>CUSTOMERS:</h5>
			<hr>
			<div class="card card-body">
				<a class="btn btn-primary  btn-sm btn-block" href="">Create Customer</a>
				<br>
				<table class="table table-sm">
					<tr>
						<th></th>
						<th>Customer</th>
						<th>Orders</th>
					</tr>
					<tr v-for="customer in customers" :key="customer.id">
						<td></td>
						<td>{{ customer.name }}</td>
						<td>&nbsp;&nbsp;&nbsp;{{ customer.order_count }}</td>
					</tr>

				</table>
			</div>
		</div>

		<div class="col-md-7">
			<h5>LAST 5 ORDERS</h5>
			<hr>
			<div class="card card-body">
				<a class="btn btn-primary  btn-sm btn-block" href="">Create Order</a>
				<br>
				<table class="table table-sm">
					<tr>
						<th>Product</th>
						<th>Date Ordered</th>
						<th>Status</th>
						<th>Update</th>
						<th>Remove</th>
					</tr>

					<tr v-for="order in orders" :key="order.id">
						<td>{{ order.product_name }}</td>
						<td>{{ order.date_created }}</td>
						<td>{{ order.status }}</td>
						<td><a class="btn btn-warning btn-sm">Update</a></td>
						<td><a class="btn btn-danger btn-sm">Delete</a></td>
					</tr>


				</table>
			</div>
		</div>

	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { type Orders } from '../types/Orders'
import { type Customer } from '../types/Customer'
export default defineComponent({
	name: 'DashboardView',
	setup() {
		const customers = ref<Customer[]>([]);
		const orders = ref<Orders[]>([]);
		const totalCustomers = ref<number>(0);
		const totalOrders = ref<number>(0);
		const delivered = ref<number>(0);
		const pending = ref<number>(0);

		onMounted(async () => {
			try {
				const response = await fetch('http://127.0.0.1:8000/dashboard', {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json', // Optional headers
						// Add any other headers as needed
					},
				});

				if (!response.ok) {
					throw new Error('Network response was not ok');
				}

				const data = await response.json();

				console.log(data);

				customers.value = data.customers;
				orders.value = data.orders;
				totalCustomers.value = data.total_customers;
				totalOrders.value = data.total_orders;
				delivered.value = data.delivered;
				pending.value = data.pending;
			} catch (error) {
				console.error('Error:', error);
			}
		});

		return {
			customers,
			orders,
			totalCustomers,
			totalOrders,
			delivered,
			pending,
		};

	}
})
</script>

<style scoped></style>