import CustomerView from '@/views/CustomerView.vue'
import DashboardView from '@/views/DashboardView.vue'
import ProductView from '@/views/ProductView.vue'
import OrderFormView from '@/views/OrderFormView.vue'
import DeleteFormView from '@/views/DeleteFormView.vue'
import OrderFormUpdateView from '@/views/OrderFormUpdateView.vue'
import LoginView from '@/views/LoginView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import RegisterView from '@/views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/customer',
      name: 'customer',
      component: CustomerView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/orderform',
      name: 'orderform',
      component: OrderFormView
    },
    {
      path: '/orderupdate/:id',
      name: 'orderupdate',
      component: OrderFormUpdateView
    },
    {
      path: '/deleteform',
      name: 'deleteform',
      component: DeleteFormView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },




  ]
})

export default router
