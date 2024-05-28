<template>
  <div class="card-dashboard"
       :style="{ height: cardHeight + 'px', width: cardWidth + 'px', background: corCard }">
    <div class="card-dashboard-header">
      <q-icon :name="`img:icons/${iconCard}.svg`" size="45px"/>
      <span>{{ label }}</span>
    </div>
    <div class="card-dashboard-footer">
      {{ quantidade }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

withDefaults(defineProps<{
  label: string,
  iconCard: string,
  corCard: string,
  corIconCard: string,
  cardHeight: number,
  cardWidth: number,
  quantidade: string
}>(), {
  label: '',
  iconCard: 'disabled_by_default',
  corCard: '#000',
  corIconCard: '#000',
  cardHeight: 197,
  cardWidth: 285
});
</script>

<style lang="sass">
.card-dashboard
  border-radius: 8px
  padding: 20px
  position: relative

.card-dashboard-header
  display: flex
  flex-direction: column
  span
    color: #6C6C6C
    font-family: Montserrat
    font-size: 14px
    font-style: normal
    font-weight: 400
    line-height: normal
    margin-top: 5px

.card-dashboard-footer
  position: absolute
  bottom: 20px
  right: 20px
  color: gray
  font-family: Montserrat
  font-size: 30px
  font-style: normal
  font-weight: 700
  line-height: normal
  text-transform: uppercase
</style>
