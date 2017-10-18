import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '@/components/sign_in'
import EnterprisePanelMain from '@/components/enterprise_panel/enterprise_panel_main'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'sign_in',
      component: SignIn
    },
    {
      path: '/panel',
      name: 'panel_main',
      component: EnterprisePanelMain
    }
  ]
})
