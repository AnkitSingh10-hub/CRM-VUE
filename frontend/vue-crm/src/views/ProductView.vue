<template>
    <br>

    <div class="row">
        <div class="col-md">
            <div class="card card-body">
                <h5>Products</h5>
            </div>
            <div class="card card-body">
                <table class="table">
                    <tr>
                        <th>Product</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                    
               
                    <tr v-for="product in products" :key="product.id">
						<td>{{product.name}}</td>
						<td>{{product.category}}</td>
						<td>${{product.price}}</td>
                        <hr>
					</tr>
            

                </table>
            </div>
        </div>

    </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { type Product } from '../types/Product'
export default defineComponent({
    setup() {
        let products = ref<Product[]>([])
        onMounted(() => {
            fetch(' http://127.0.0.1:8000/products', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json', // Optional headers
                    // Add any other headers as needed
                },
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data); // Process the response data
                    products.value = data
                })
                .catch(error => {
                    console.error('Error:', error);
                });


        })


        return {products}
    }
})
</script>

<style scoped></style>