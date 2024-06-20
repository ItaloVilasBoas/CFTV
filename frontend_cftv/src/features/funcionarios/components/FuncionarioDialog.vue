<template>
  <slot name="activator" :onClick="onClick" />
  <q-dialog v-model="mostrarDialog">
    <q-card>
      <q-card-section>
        <q-inner-loading :showing="gravando" label="Capturando fotos do funcionario..." label-class="text-teal"
          label-style="font-size: 1.1em" />
        <q-inner-loading :showing="treinando" label="Retreinando Modelo..." label-class="text-teal"
          label-style="font-size: 1.1em" />
        <div v-if="funcionario.foto != ''">
          <img width="400" height="300" :src="getFoto(funcionario.foto)" alt="foto do funcionário">
        </div>
        <div v-if="funcionario.foto === ''">
          <q-select standout="bg-teal text-white" v-model="camera" :options="cameras"
            @update:model-value="() => trocarCamera()" :option-label="opt => 'Camera ' + opt" />
          <img width="400" height="300" :src="reactiveSourceGravacao.sourceGravacao" alt="gravar foto do funcionário">
        </div>
        <q-input outlined v-model="nomeFuncionario" label="Nome" />
        <q-select v-model="setoresFuncionario" :options="setores" label="Setores" multiple />
      </q-card-section>
      <q-card-actions align="right">
        <q-btn label="Cancelar" @click="mostrarDialog = false" />
        <q-btn label="Salvar" @click="salvarFuncionario" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import SetoresService from 'src/service/setor.service';
import FuncionarioService from 'src/service/funcionario.service';
import TreinaModeloService from 'src/service/modelo.service'
import { Funcionario } from 'src/shared/types/funcionario.type'

const props = defineProps({
  funcionario: {
    type: Object,
    default: () => ({
      id: 0,
      foto: '',
      nome: '',
      setores: [],
    }),
  },
});
const gravando = ref<boolean>(false);
const treinando = ref<boolean>(false);
const mostrarDialog = ref<boolean>(false);
const camera = ref<number>(0);
const sourceGravacao = ref<string>('http://localhost/video_feed/funcionario/1');
const reactiveSourceGravacao = reactive({ sourceGravacao })

const setores = ref<number[]>([]);
const cameras = ref<number[]>([0, 1, 2, 3]);
const nomeFuncionario = ref<string>(props.funcionario.nome);
const setoresFuncionario = ref<number[]>(props.funcionario.setores);

const onClick = () => mostrarDialog.value = true;
const trocarCamera = () => sourceGravacao.value = `http://localhost/video_feed/funcionario/1?camera_id=${camera.value}`;
const getFoto = (foto: string) => 'data:image/jpeg;base64,' + foto;

const salvarFuncionario = () => {
  if (props.funcionario.id !== 0) {
    const updatedFuncionario: Funcionario = {
      id: props.funcionario.id,
      nome: nomeFuncionario.value,
      setores: setoresFuncionario.value,
      foto: props.funcionario.foto,
    }
    FuncionarioService.update(updatedFuncionario)
    mostrarDialog.value = false;
    return;
  }

  FuncionarioService.create({
    id: 0,
    foto: '',
    nome: nomeFuncionario.value,
    setores: setoresFuncionario.value,
  }).then((funcionario) => {
    gravando.value = true;
    sourceGravacao.value =
      `http://localhost/video_feed/funcionario/${funcionario.id}?camera_id=${camera.value}&capturar=1`;
    setTimeout(() => {
      treinando.value = true;
      TreinaModeloService.treinarModelo().then(() => {
        treinando.value = false;
      })
      FuncionarioService.updateFoto(funcionario.id).then(() => {
        gravando.value = false;
        mostrarDialog.value = false;
        sourceGravacao.value = 'http://localhost/video_feed/funcionario/1'
      })
    }, 5000)
  });
};

SetoresService.getAll().then((response) => {
  setores.value.push(...response.map((setor) => setor.id))
});
</script>
