<template>
  <div class="card row">
    <div class="col-2" style="display: flex">
      <img class="foto-funcionario" :src="getFoto(data.foto)" alt="" />
    </div>
    <div class="col-2">
      {{ data.nome }}
    </div>
    <div class="col-4">
      {{ data.setores }}
    </div>
    <div class="col-2">
      <FuncionarioDialog :funcionario="data">
        <template v-slot:activator="{ onClick }">
          <q-btn icon="edit" @click="onClick" />
        </template>
      </FuncionarioDialog>
      <q-btn icon="delete" @click="deletar" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { Funcionario } from '../../../shared/types/funcionario.type'
import FuncionarioService from 'src/service/funcionario.service';
import { FuncionarioDialog } from '.'

const props = defineProps<{ data: Funcionario; }>();

const getFoto = (foto: string) => {
  if (foto.includes('http'))
    return foto;
  return 'data:image/jpeg;base64,' + foto;
}

const deletar = () => {
  FuncionarioService.delete(props.data.id)
}

</script>

<style lang="sass">
.card
  color: white
  background-color: rgba(255, 255, 255, .1)
  align-items: center
  height: 70px
  justify-content: space-between

.foto-funcionario
  border-radius: 8px
  width: 60px
</style>
