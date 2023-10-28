<template>
	<div class="row">
		<div class="col-md-6">
			<div class="card card-body">
				<h3>Update Order</h3>
				<h2>{{ $route.params.id }}</h2>
			</div>
		</div>
	</div>

	<div class="row">
		<div class="col-md-6">
			<div class="card card-body">
				<form>


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
import { useRoute } from 'vue-router';


export default defineComponent({
	setup() {
		const route = useRoute();
		const num = ref<number>(5)
		
		fetch('http://127.0.0.1:8000/orders/'+ route.params.id, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json', // Optional headers
				// Add any other headers as needed
			},
		})
			.then(response => response.json())
			.then(data => {
				console.log(data); // Process the response data
			})
			.catch(error => {
				console.error('Error:', error);
			});


	}
})
</script>

<style scoped></style>