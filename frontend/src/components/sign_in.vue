<template>
  <div class="SignIn">
    <form class="signIn__form">
      <div class="form-field">
        <input class="form-field__input" id="signIn__form-login" v-model.trim="login" type="text" placeholder="Логин">
        <icon name="user" scale="2" class="form-field__icon--user"></icon>
      </div>
      <div class="form-field">
        <input class="form-field__input" id="signIn__form-password" v-model.trim="password" type="password" placeholder="Пароль">
        <icon name="lock" scale="2" class="form-field__icon--lock"></icon>
      </div>
      <div class="form-field__actions">
        <input @click.prevent="authorize" class="form-field__submit" type="submit" value="Войти"/>
      </div>
    </form>
  </div>
</template>

<script>
  import 'vue-awesome/icons/user'
  import 'vue-awesome/icons/lock'
  export default {
    name: 'SignIn',
    data () {
      return {
        login: '',
        password: ''
      }
    },
    methods: {
      authorize () {
        if (this.login === 'test' && this.password === 'qazwsx123') {
          this.$router.push({name: 'panel_main'})
        } else {
          this.$snotify.error('Неверный логин/пароль', 'Ошибка!', {
            timeout: 2000,
            showProgressBar: true,
            closeOnClick: true,
            pauseOnHover: true
          })
        }
      }
    }
  }
</script>

<style scoped>

  .SignIn {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-color: #3498db
  }

  .signIn__form {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    height: 304px;
    width: 598px;
    background-color: #ecf0f1;
    border-radius: 5px;
  }

  .SignIn .signIn__form .form-field {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 534px;
    height: 55px;
    border-radius: 5px;
    background-color: #ffffff;
  }

  .form-field .fa-icon { color: #95a5a6; }

  .SignIn .signIn__form .form-field .form-field__icon--user {
    width: 21px;
    height: 26px;
  }

  .SignIn .signIn__form .form-field .form-field__icon--lock {
    margin-top: 4px;
    width: 21px;
    height: 26px;
  }

  .SignIn .signIn__form .form-field__input {
    width: 474px;
    height: 52px;
    font-size: 24px;
    color: #95a5a6;
    background-color: #fff;
    border: none;
    outline: none;
  }

  .form-field__input::-webkit-input-placeholder { color: #95a5a6; }
  .form-field__input:-moz-placeholder { color: #95a5a6; }
  .form-field__input::-moz-placeholder { color: #95a5a6; }
  .form-field__input:-ms-input-placeholder { color: #95a5a6; }

  .SignIn .signIn__form .form-field__submit {
    width: 100%;
    height: 55px;
    border-radius: 5px;
    border: none;
    background-color: #3498db;
    text-transform: uppercase;
    color: #fff;
    font-size: 30px;
    outline: none;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
  }

  .SignIn .signIn__form .form-field__submit:hover {  background: #2980b9; }

  .SignIn .signIn__form .form-field__actions {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 534px;
  }

</style>
