<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>Keycloak test</q-toolbar-title>

        <div v-if="user">Hi {{ user.first_name }} {{ user.last_name }}!</div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue'
import {api} from 'src/boot/axios'
defineOptions({
  name: 'MainLayout',
})
const user = ref()

onMounted(async () => {
  try {
    const resp = await api.get('/api/users/me/')
    user.value = resp.data
  } catch (err) {}
})
</script>
