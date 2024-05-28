<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="default-background-color">
      <ToolBar/>
    </q-header>
    <q-page-container class="page-container">
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script setup lang="ts">
import ToolBar from 'src/components/ToolBar.vue';
// import { ref } from 'vue';

defineOptions({
  name: 'MainLayout'
});
</script>
<style lang="sass">
.default-background-color
  background: linear-gradient(71deg, #0B121E 19.35%, #0D121C 90.12%)
.page-container
  background: linear-gradient(71deg, #0B121E 19.35%, #0D121C 90.12%)
  padding: 148px 40px !important
  min-height: -webkit-fill-avaible
</style>
