<template>
  <q-toolbar class="bar gt-sm">
    <div class="nav-buttons">
      <div class="nav-button"
        v-for="button in navButtons"
        :key="button.path"
        @click="navigateTo(button.path)"
      >
        <Transition name="fade">
          <q-icon class="icon-nav-button" size="26px"
            :name="'img:icons/active.svg'"
            v-if="button.active"
          />
        </Transition>
        <q-icon class="icon-filter" size="47px"
          :name="`img:icons/${button.icon}.svg`"
        />
        <span>{{ button.titulo }}</span>
      </div>
    </div>
  </q-toolbar>
  <div class="lt-md" style="display: grid">
    <q-btn icon="menu" size="26px"
      @click="drawer = !drawer"
      flat dense
    />
    <q-drawer class="bar-drawer" :width="190" v-model="drawer">
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item v-for="button in navButtons" :key="button.path"
            @click="navigateTo(button.path)"
            clickable v-ripple
          >
            <q-item-section avatar>
              <q-icon class="icon-filter" :name="`img:icons/${button.icon}.svg`"/>
            </q-item-section>
            <q-item-section>
              {{ button.titulo }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const drawer = ref(false);
const router = useRouter();
const route = useRoute();
const navButtons = ref([
  { path: '/', active: false, icon: 'home', titulo: 'Home' },
  { path: '/live', active: false, icon: 'security-camera', titulo: 'Live' },
  { path: '/funcionarios', active: false, icon: 'employee-card', titulo: 'Funcionários' },
  { path: '/ajustes', active: false, icon: 'settings', titulo: 'Ajustes' },
]);
navButtons.value.find((botao) => botao.path == route.path)!.active = true;

function navigateTo(path: string) {
  navButtons.value.find((botao) => botao.active)!.active = false;
  navButtons.value.find((botao) => botao.path == path)!.active = true;
  router.push(path);
}
</script>
<style lang="sass">
.bar
  border-radius: 30px
  background: #101F2C
  font-family: Montserrat
  height: 108px
  justify-content: center

.bar-drawer
  background: #101F2C
  font-family: Montserrat

.nav-buttons
  display: flex
  position: relative
  left: 50px

.nav-button
  margin-right: 160px
  position: relative
  &:hover
    cursor: pointer
    filter: brightness(0) saturate(100%) invert(87%) sepia(26%) saturate(411%) hue-rotate(183deg) brightness(103%) contrast(105%) !important
  span
    position: relative
    top: 10px
    left: 12px
    font-size: 14px
    font-weight: 700
.icon-nav-button
  margin-right: 14px
  position: absolute
  right: 100%
  top: 15px

.icon-filter
  filter: invert(77%) sepia(17%) saturate(6944%) hue-rotate(190deg) brightness(113%) contrast(94%)

.fade-enter-active,
.fade-leave-active
  transition: opacity 0.5s ease
.fade-enter-from,
.fade-leave-to
  opacity: 0
</style>
