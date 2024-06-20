<template>
  <div id="body">
    <div class="card-login">
      <div class="card-logo">
        <svg width="6" height="39" viewBox="0 0 6 39" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 0L3 39" stroke="#050330" stroke-width="6"/>
        </svg>
        <div class="card-logo-text">
          <div style="font-size: 32px; font-weight: 700;">CFTV</div>
          <q-icon size="49px" name="img:icons/security-camera-colored.svg"/>
        </div>
      </div>
      <div class="card-content">
        <div class="sign-in-text">SIGN IN</div>
        <div class="sign-in-subtitle">Entre suas credenciais para acessar sua conta</div>
        <div class="card-form">
          <div>Email</div>
          <q-input square outlined label="Insira seu email" type="text" v-model="email" style="margin-bottom: 20px;"/>
          <div>Senha</div>
          <q-input square outlined label="Insira sua senha" type="password" v-model="senha"/>
        </div>
      </div>
      <div class="card-actions">
        <q-btn class="btn-sign-in" color="black" label="SIGN IN"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const senha = ref('')
</script>

<style lang="sass">
@import url(https://fonts.googleapis.com/css2?family=Montserrat)

#body
  background: linear-gradient(71deg, #0B121E 19.35%, #0D121C 90.12%)
  display: grid
  justify-items: center
  align-items: center
  height: 100vh

.card-login
  align-items: center
  background: #FFF
  border-radius: 20px
  box-shadow: 2px 5px 10px 0px rgba(0, 0, 0, 0.10)
  height: 550px
  width: 475px
  padding: 44px 30px

.card-logo
  display: flex
  margin-bottom: 40px
  .card-logo-text
    display: flex
    position: relative
    left: 155px

.card-content
  display: grid
  justify-items: center

.card-form
  margin: 50px 0
  .q-input
    border-radius: 4px
    height: 44px
    width: 415px

.sign-in-text
  font-family: Montserrat
  font-size: 22px
  font-weight: 600

.sign-in-subtitle
  color: #6C6C6C
  font-family: Montserrat
  font-size: 14px
  font-weight: 400

.btn-sign-in
  font-family: Montserrat
  font-weight: 400
  height: 44px
  width: 415px
</style>
