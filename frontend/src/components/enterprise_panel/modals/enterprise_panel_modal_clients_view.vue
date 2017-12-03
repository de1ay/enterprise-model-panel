<template>
    <form id="enterprise_panel_modal_clients">
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim="editable_data.client_name"
            type="text"
            placeholder="Имя/Название">
            <icon name="user" scale="1.2" class="form-field__icon--lock"></icon>
        </div>
        <div class="form-field__actions">
          <button class="form-field__edit" @click.prevent="editClientConfirm">Изменить</button>
          <button class="form-field__delete" @click.prevent="deleteClientConfirm">Удалить</button>
        </div>
    </form>
</template>

<script>
  import 'vue-awesome/icons/user'
  export default {
    name: 'EnterprisePanelModalClientsView',
    props: ['billings', 'clients', 'media', 'deals', 'additional_data'],
    data () {
      return {
        editable_data: Object.assign({}, this.additional_data)
      }
    },
    methods: {
      editClientConfirm () {
        this.$snotify.confirm('Изменить клиента?', 'Изменение', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.editClient(); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      editClient () {
        this.$emit('editClient', this.editable_data, this.additional_data)
      },
      deleteClientConfirm () {
        this.$snotify.confirm('Удалить клиента?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.$emit('deleteClient', this.additional_data); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
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

    .form-field__delete {
        width: 45%;
        height: 38px;
        border-radius: 5px;
        border: none;
        background-color: #e74c3c;
        text-transform: uppercase;
        color: #fff;
        font-size: 18px;
        outline: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }

    .form-field__delete:hover {  background: #c0392b; }

    .form-field__edit {
        width: 45%;
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

    .form-field__edit:hover {  background: #2980b9; }

    .form-field__actions {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin: 15px 0 30px 0;
        width: 300px;
    }

</style>
