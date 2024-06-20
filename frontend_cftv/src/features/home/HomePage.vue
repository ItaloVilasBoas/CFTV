<template>
  <div class="dashBoard">
    <div v-for="card in cardsDashboard" :key="card.label">
      <DashBoardCard
        :label="card.label"
        :iconCard="card.icon"
        :corIcon="card.corIcon"
        :corCard="card.background"
        :quantidade="card.quantidade"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { DashBoardCard } from './components';
  import FuncionarioService from 'src/service/funcionario.service'
  import SetorService from 'src/service/setor.service'
  import { ref } from 'vue'

  const cardsDashboard = ref([
    {
      label: 'Funcionários',
      quantidade: '0',
      background: 'linear-gradient(110deg, #000 18.27%, #2E2E2E 91.84%)',
      icon: 'profile',
      corIcon: '#EE95C5'
    },
  ])

  FuncionarioService.getAll().then((response) => {
    cardsDashboard.value[0].quantidade = response.length.toString()
  });

  SetorService.getAll().then((response) => {
    response.forEach((setor) => {
      cardsDashboard.value.push({
        label: setor.nome,
        quantidade: setor.cameras.length.toString(),
        background: 'linear-gradient(180deg, #e0f4fe 0%, #9ac0f7 100%)',
        icon: 'security-camera',
        corIcon: '#74c1ed'
      })
    });
  });
</script>
<style lang="sass">
.dashBoard
  display: grid
  grid-template-columns: repeat(auto-fill, 285px)
  justify-content: center
  gap: 80px

</style>
