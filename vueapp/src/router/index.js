import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ImageSettings from '@/components/ImageSettings'
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
      path: '/settings/:id',
      name: 'ImageSettings',
      component: ImageSettings,
      props: true,
    }
  ],

  mode: "history",
})
