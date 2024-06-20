<template>
  <FuncionarioDialog >
    <template v-slot:activator="{ onClick }">
      <q-btn
        label="Cadastrar Funcionário"
        color="white"
        text-color="black"
        @click="onClick"
      />
    </template>
  </FuncionarioDialog>
  <div class="header-funcionarios row">
    <div class="col-2"></div>
    <div class="col-2">Nome</div>
    <div class="col-4">Setores</div>
    <div class="col-2"></div>
  </div>
  <div v-for="funcionario in funcionarios" :key="funcionario.id">
    <FuncionarioCard :data="funcionario" />
  </div>
</template>
<script setup lang="ts">
import FuncionarioService from 'src/service/funcionario.service'
import { FuncionarioCard } from './components'
import { FuncionarioDialog } from './components'
import { Funcionario } from '../../shared/types/funcionario.type'
import { ref } from 'vue';

const funcionarios = ref<Funcionario[]>([/*
  {
    id: 1,
    foto: 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQpXGKZgni7hwvYnFUen08LQP43RoFAhJc_p6XQ1yL3uDne6GjX',
    nome: 'Kendrick Lamar',
    setores: [1, 2]
  },*/
]);

FuncionarioService.getAll().then((response) => {
  funcionarios.value = response;
});
</script>
<style lang="sass">
.header-funcionarios
  color: white
  font-weight: bold
  margin: 1em 0
  padding: 0.5em
  border-bottom: 1px solid #ccc
  .col-2
    width: 20%
  .col-4
    width: 40%
  .col-2
    width: 20%
  .col-2
    width: 20%
</style>
