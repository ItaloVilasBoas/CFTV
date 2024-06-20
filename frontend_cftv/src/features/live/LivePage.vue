<template>
  <div class="row" v-if="setorAtual != null">
    <div class="white-text col-4">
      <h3>Dashboard</h3>
      <div class="row">
        <q-select standout="bg-teal text-white" v-model="setorAtual" :options="setores" option-label="nome"
          @update:model-value="() => trocarSetor()" />
      </div>
    </div>
    <div class="col-8 white-text" style="display: grid; justify-items: center;">
      <div style="
          display: flex;
          align-items: center;
          background: rgba(108, 122, 137, 0.2);
          height: 50px;
          position: absolute;">
        <q-icon :name="`img:icons/security-camera.svg`" class="filter-white" size="35px" />
        <q-select standout="bg-teal text-white" v-model="cameraAtual" :options="setorAtual.cameras"
          :option-label="opt => 'Camera ' + opt" />
      </div>
      <img :src="'http://localhost/video_feed/reconhecimento?camera_id=' + cameraAtual" />
      <div>
        <img
          v-for="camera in setorAtual.cameras.filter(f => f != cameraAtual)" :key="camera"
          :src="'http://localhost/video_feed/reconhecimento?camera_id=' + camera"
          width="25%"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SetorService from 'src/service/setor.service'
import { Setor } from 'src/shared/types/setor.type';
import { ref, reactive } from 'vue';

const setores = ref<Setor[]>([]);
const setorAtual = ref<Setor>();
const cameraAtual = ref();
const reactiveCameraAtual = reactive({ cameraAtual })

function trocarSetor() {
  if(setorAtual.value)
    reactiveCameraAtual.cameraAtual = setorAtual.value.cameras[0]
}

SetorService.getAll().then((response) => {
  setores.value.push(...response)
  setorAtual.value = response[0]
  cameraAtual.value = response[0].cameras[0]
});
</script>

<style lang="sass">
.q-field__native > span
  color: white
.q-field__append
  color: white
.white-text
  color: white
.filter-white
  filter: brightness(0) saturate(100%) invert(98%) sepia(1%) saturate(957%) hue-rotate(355deg) brightness(113%) contrast(100%)
</style>
