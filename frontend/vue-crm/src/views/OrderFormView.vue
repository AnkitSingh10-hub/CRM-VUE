<template>
	<div class="row">
		<div class="col-md-6">
			<div class="card card-body">
				<h3>Create Order</h3>

				<div v-if="successMsG" class="alert alert-info" role="alert">
					{{ successMsG }}
				</div>


			</div>
		</div>
	</div>

	<div class="row">
		<div class="col-md-6">
			<div class="card card-body">
				<form @submit.prevent="submit">
					<label for="options">Customer</label>

					<select id="options" v-model="dataToSend.customer_name" class="form-select" aria-label="Default select example">
					    <option value="" disabled selected>Choose a customer</option>

						<option v-for="customer in customers" :key="customer.id">{{ customer.name }}</option>

					</select>
					<hr>
					<label for="options1">Product</label>

					<select id="options1" v-model="dataToSend.product_name" class="form-select" aria-label="Default select example">
						<option value="" disabled selected>Choose a Product</option>

						<option v-for="product in products" :key="product.id">{{ product.name }}</option>

					</select>
					<hr>
					<label for="options2">Status</label>

					<select id="options2" v-model="dataToSend.status" class="form-select" aria-label="Default select example">
						<option value="" disabled selected>Choose a Status</option>

						<option v-for="st in statuses" :key="st.status">{{ st.status }}</option>

					</select>
					<hr>
					<button type="submit" class="btn btn-info"> Submit Form </button>
				</form>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, reactive, ref } from 'vue'
import { type Customer } from '@/types/Customer'
import { type Product } from '@/types/Product'
import { type Status } from '@/types/Status'

export default defineComponent({
	setup() {
		let customers = ref<Customer[]>([])
		let products = ref<Product[]>([])
		let statuses = ref<Status[]>([])
		var successMsG = ref<string>('')
		const dataToSend = reactive({
			status: '',
			customer_name: '',
			product_name: ''
		})
		const x = ref<string>('Select a Customer')
		const y = ref<string>('Select a Product')
		const z = ref<string>('Select a Status')
		onMounted(() => {
			fetch('http://127.0.0.1:8000/orders', {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json', // Optional headers
					// Add any other headers as needed
				},
			})
				.then(response => response.json())
				.then(data => {
					console.log(data);

					customers.value = data.customers
					products.value = data.products
					statuses.value = data.status

				})
				.catch(error => {
					console.error('Error:', error);
				});

		})

		const submit = () => {
			fetch('http://127.0.0.1:8000/orders', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json', // Specify the content type
					// Add any other headers as needed
				},
				body: JSON.stringify(dataToSend), // Convert data to JSON
			})
				.then(response => response.json())
				.then(data => {
					console.log(data);
					console.log(data, "data is received")
					console.log(successMsG)
					successMsG.value = "The order has been submitted !!!"
					setTimeout(() => {
						successMsG.value = '';
					}, 3000);
				})
				.catch(error => {
					console.error('Error:', error);
				});


		}

		return { customers, products, statuses, submit, dataToSend, successMsG, x, y, z }
	}
})
</script>

<style scoped></style>