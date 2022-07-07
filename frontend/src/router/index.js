import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const constantRoutes = [{
    path: '/login',
    component: () => import('@/views/login/login'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },
  {
    path: '/',
    redirect: '/index',
    component: () => import('@/views/home/home'),
    children: [{
      path: '/index',
      component: () => import('@/views/index/index'),
    }, {
      path: '/create',
      component: () => import('@/views/create/create'),
    }, {
      path: '/my',
      component: () => import('@/views/my/my'),
    }, {
      path: '/vip',
      component: () => import('@/views/vip/vip'),
    },{
      path: '/detail',
      component: () => import('@/views/detail/detail'),
    }, {
      path: '/com',
      component: () => import('@/views/com/com'),
    }]
  },
  // 404 page must be placed at the end !!!
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({
    y: 0
  }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
