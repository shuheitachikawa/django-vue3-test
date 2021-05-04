import { createRouter, createWebHistory } from 'vue-router'
const routerHistory = createWebHistory()


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/home.vue'),
    children: [
      {
        path: '',
        redirect: 'tweet'
      },
      {
        path: 'tweet',
        name: 'tweet',
        component:  () => import('../views/home/tweet.vue'),
      }
    ]
  },
]

const router = createRouter({
  history: routerHistory,
  routes,
})

export default router