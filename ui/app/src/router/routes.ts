import {RouteRecordRaw} from 'vue-router'

const post = (path: string, params: {[key: string]: string | null}, method = 'post') => {
  // The rest of this code assumes you are not using a library.
  // It can be made less verbose if you use one.
  const form = document.createElement('form')
  form.method = method
  form.action = path

  for (const key in params) {
    if (params.hasOwnProperty(key)) {
      const hiddenField = document.createElement('input')
      hiddenField.type = 'hidden'
      hiddenField.name = key
      hiddenField.value = params[key] || ''

      form.appendChild(hiddenField)
    }
  }

  document.body.appendChild(form)
  form.submit()
}

const cookie = (key: string) =>
  (new RegExp((key || '=') + '=(.*?); ', 'gm').exec(document.cookie + '; ') || ['', null])[1]

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '/',
        component: () => import('pages/IndexPage.vue'),
      },
    ],
  },
  {
    path: '/login',
    component: () => import('layouts/MainLayout.vue'),
    beforeEnter() {
      // Must be posted including the csfr token to redirect to the keycloak login page
      post('/api/auth/oidc/keycloak/login/?process=login', {
        csrfmiddlewaretoken: cookie('csrftoken'),
      })
    },
  },
  {
    path: '/logout',
    component: () => import('layouts/MainLayout.vue'),
    beforeEnter() {
      // Must be posted including the csfr token to redirect to the keycloak login page
      post('/api/auth/logout/', {csrfmiddlewaretoken: cookie('csrftoken')})
    },
  },
  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    beforeEnter() {
      window.location.href = '/admin'
    },
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
