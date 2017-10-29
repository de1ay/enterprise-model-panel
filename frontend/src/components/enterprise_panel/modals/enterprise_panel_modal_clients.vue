<template>
    <div id="enterprise_panel_modal_clients">
        <div class="form-field">
            <input 
            class="form-field__input"
            v-model.trim="client_name" 
            type="text" 
            placeholder="Имя/Название">
            <icon name="user" scale="1.2" class="form-field__icon--lock"></icon>
        </div>
        <div class="form-field__actions">
            <input class="form-field__submit" @click.prevent="addClient" type="submit" value="Создать"/>
        </div>
    </div>
</template>

<script>
  import 'vue-awesome/icons/user'
  export default {
    name: 'EnterprisePanelModalClients',
    props: ['requests', 'billings', 'clients', 'media', 'deals'],
    data () {
      return {
        client_name: ''
      }
    },
    methods: {
      addClient () {
        this.$emit('addClient', {
          client_name: this.client_name
        })
      }
    }
  }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>

    #enterprise_panel_modal_requests {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .form-field {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        margin: 15px 0;
        width: 300px;
        height: 38px;
        border-radius: 5px;
        background-color: #ffffff;
    }

    .form-field:first-child {
        margin: 30px 0 15px 0;
    }

    .form-field .fa-icon { color: #95a5a6; }

    .form-field .form-field__icon--lock {
        margin-top: 4px;
    }

    .form-field__input {
        width: 240px;
        height: 35px;
        font-size: 18px;
        color: #95a5a6;
        border: none;
        outline: none;
    }

    .form-field__input::-webkit-input-placeholder { color: #95a5a6; }
    .form-field__input:-moz-placeholder { color: #95a5a6; }
    .form-field__input::-moz-placeholder { color: #95a5a6; }
    .form-field__input:-ms-input-placeholder { color: #95a5a6; }

    .form-field__submit {
        width: 100%;
        height: 38px;
        border-radius: 5px;
        border: none;
        background-color: #3498db;
        text-transform: uppercase;
        color: #fff;
        font-size: 18px;
        outline: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }

    .form-field__submit:hover {  background: #2980b9; }

    .form-field__actions {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        margin: 15px 0 30px 0;
        width: 300px;
    }

    .form-field__input .multiselect__tags {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        padding: 0;
        margin: 2px 0;
        min-height: 35px;
        max-height: 35px;
        border: none;
    }

    .form-field__input .multiselect__tags input {
        margin: 0;
        padding: 0;
        height: 35px;
        font-size: 18px;
        color: #95a5a6;
    }

    .form-field__input .multiselect__tags input::-webkit-input-placeholder { color: #95a5a6; }
    .form-field__input .multiselect__tags input:-moz-placeholder { color: #95a5a6; }
    .form-field__input .multiselect__tags input::-moz-placeholder { color: #95a5a6; }
    .form-field__input .multiselect__tags input:-ms-input-placeholder { color: #95a5a6; }

</style>
