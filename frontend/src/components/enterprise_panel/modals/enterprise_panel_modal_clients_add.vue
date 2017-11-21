<template>
    <form id="enterprise_panel_modal_clients">
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
    </form>
</template>

<script>
  import 'vue-awesome/icons/user'
  export default {
    name: 'EnterprisePanelModalClientsAdd',
    props: ['billings', 'clients', 'media', 'deals'],
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

<style scoped>

    #enterprise_panel_modal_clients {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

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

</style>
