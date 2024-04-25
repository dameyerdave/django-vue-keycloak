<template>
  <q-page class="row items-center justify-evenly">
    <div col>
      <pre>{{ user }}</pre>
      <q-btn @click="$router.push('/login')">Login</q-btn>
      <q-btn @click="$router.push('/logout')">Logout</q-btn>
      <q-btn @click="$router.push('/admin')">Admin</q-btn>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue'
import {api} from 'src/boot/axios'
defineOptions({
  name: 'IndexPage',
})
const user = ref()

onMounted(async () => {
  try {
    const resp = await api.get('/api/users/me/')
    user.value = resp.data
  } catch (err) {}
})
</script>
