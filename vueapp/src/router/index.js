import Vue from 'vue'
import Router from 'vue-router'
import Preview from '@/components/Preview'
import Main from '@/components/Main'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/preview/:id',
      name: 'Preview',
      component: Preview,
      props: true,
    }
  ],

  mode: "history",
})
