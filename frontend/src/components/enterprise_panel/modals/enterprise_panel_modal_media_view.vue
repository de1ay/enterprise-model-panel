<template>
    <form id="enterprise_panel_modal_media">
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim="editable_data.media_name"
            type="text"
            placeholder="Название">
            <icon name="television" scale="1.2" class="form-field__icon--tv"></icon>
        </div>
        <div class="form-field">
            <multiselect
            class="form-field__input"
            v-model="editable_data.media_type_info"
            :options="media_types"
            label="label"
            track-by="value"
            :show-labels="false"
            :allow-empty="false"
            placeholder="Тип"></multiselect>
            <icon name="bullhorn" scale="1.2" class="form-field__icon--bullhorn"></icon>
        </div>
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim.number="editable_data.media_address"
            type="text"
            placeholder="Адрес">
            <icon name="globe" scale="1.2" class="form-field__icon--globe"></icon>
        </div>
        <div class="form-field__actions">
          <button class="form-field__edit" @click.prevent="editMediaConfirm">Изменить</button>
          <button class="form-field__delete" @click.prevent="deleteMediaConfirm">Удалить</button>
        </div>
    </form>
</template>

<script>
  import axios from 'axios'
  import 'vue-awesome/icons/globe'
  import 'vue-awesome/icons/television'
  import 'vue-awesome/icons/bullhorn'
  export default {
    name: 'EnterprisePanelModalMediaView',
    props: ['billings', 'clients', 'media', 'deals', 'additional_data'],
    data () {
      return {
        editable_data: Object.assign({}, this.additional_data),
        media_types: [
          {
            label: 'Баннер',
            value: '1'
          },
          {
            label: 'Радиостанция',
            value: '2'
          }
        ]
      }
    },
    methods: {
      editMediaConfirm () {
        this.$snotify.confirm('Изменить медиа-носитель?', 'Изменение', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.editMedia(); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      editMedia () {
        this.editable_data.media_type = this.editable_data.media_type_info.value
        this.$emit('editMedia', this.editable_data, this.additional_data)
      },
      deleteMediaConfirm () {
        this.$snotify.confirm('Удалить медиа-носитель?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.deleteMedia(this.additional_data); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      deleteMedia (rowObj) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.delete('https://beta.project.nullteam.info/api/media/' + rowObj.media_id).then(resp => {
              this.media.splice(this.media.indexOf(rowObj))
              this.$emit('update:media', this.media)
              resolve({
                title: 'Успешно',
                body: 'Медиа-носитель удален',
                config: {
                  closeOnClick: true,
                  timeout: 2000,
                  showProgressBar: true,
                  pauseOnHover: true
                }
              })
            }).catch(resp => {
              /*eslint-disable */
              reject({
                title: 'Ошибка!',
                body: 'Медиа-носитель не удален',
                config: {
                  closeOnClick: true,
                  timeout: 2000,
                  showProgressBar: true,
                  pauseOnHover: true
                }
              })
              /*eslint-enable */
            })
          }
        ))
        this.$emit('hideModal', {}, true)
      }
    }
  }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>

    #enterprise_panel_modal_media {
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
