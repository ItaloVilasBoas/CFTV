import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('src/features/home/HomePage.vue')
      },
      {
        path: 'live',
        component: () => import('src/features/live/LivePage.vue')
      },
      {
        path: 'funcionarios',
        component: () => import('src/features/funcionarios/FuncionariosPage.vue')
      },
      {
        path: 'ajustes',
        component: () => import('src/features/ajustes/AjustesPage.vue')
      },
    ],
  },
  {
    path: '/login',
    component: () => import('src/features/login/LoginPage.vue'),
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
