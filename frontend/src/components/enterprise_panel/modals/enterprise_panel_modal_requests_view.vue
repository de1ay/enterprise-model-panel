<template>
    <div id="enterprise_panel_modal_requests">
        <div class="form-field">
            <multiselect
                class="form-field__input"
                v-model="editable_data.deal_client"
                :options="clients"
                label="client_name"
                track-by="client_id"
                :allow-empty="false"
                :show-labels="false"
                placeholder="Клиент"></multiselect>
            <icon name="user" scale="1.2" class="form-field__icon--user"></icon>
        </div>
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim="editable_data.deal_brand"
            type="text"
            placeholder="Бренд">
            <icon name="newspaper-o" scale="1.2" class="form-field__icon--lock"></icon>
        </div>
        <div class="form-field">
            <multiselect
            class="form-field__input"
            v-model="editable_data.deal_media"
            :options="media"
            label="media_name"
            track-by="media_id"
            :show-labels="false"
            :allow-empty="false"
            placeholder="Медиа-носитель"></multiselect>
            <icon name="globe" scale="1.2" class="form-field__icon--globe"></icon>
        </div>
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim.number="editable_data.deal_sum"
            type="number"
            placeholder="Сумма">
            <icon name="money" scale="1.2" class="form-field__icon--money"></icon>
        </div>
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim.number="editable_data.deal_time"
            type="number"
            placeholder="Длительность">
            <icon name="clock-o" scale="1.2" class="form-field__icon--clock"></icon>
        </div>
        <div class="form-field">
            <flat-pickr
            v-model="editable_data.start_date"
            class="form-field__input"
            :config="date_config"
            placeholder="Начальная дата"></flat-pickr>
            <icon name="flag-o" scale="1.2" class="form-field__icon--flag"></icon>
        </div>
        <div class="form-field">
            <flat-pickr
            v-model="editable_data.end_date"
            class="form-field__input"
            :config="date_config"
            placeholder="Конечная дата"></flat-pickr>
            <icon name="flag-checkered" scale="1.2" class="form-field__icon--flag"></icon>
        </div>
        <div class="form-field__actions">
          <button class="form-field__edit" @click.prevent="editDealConfirm">Изменить</button>
          <button class="form-field__delete" @click.prevent="deleteDealConfirm">Удалить</button>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  import 'vue-awesome/icons/globe'
  import 'vue-awesome/icons/money'
  import 'vue-awesome/icons/newspaper-o'
  import 'vue-awesome/icons/flag-o'
  import 'vue-awesome/icons/flag-checkered'
  import 'vue-awesome/icons/clock-o'
  import flatPickr from 'vue-flatpickr-component'
  import 'flatpickr/dist/flatpickr.css'
  import {Russian} from 'flatpickr/dist/l10n/ru'
  export default {
    name: 'EnterprisePanelModalRequestsView',
    props: ['requests', 'billings', 'clients', 'media', 'deals', 'additional_data'],
    data () {
      return {
        editable_data: Object.assign({}, this.additional_data),
        date_config: {
          altFormat: 'd/m/Y',
          altInput: true,
          dateFormat: 'm/d/Y',
          locale: Russian
        },
        deal_statuses: [
          {
            id: '0',
            value: 'В обработке'
          },
          {
            id: '1',
            value: 'Ожидается оплата'
          },
          {
            id: '2',
            value: 'Оплачен'
          },
          {
            id: '3',
            value: 'Активен'
          },
          {
            id: '4',
            value: 'Завершён'
          }
        ]
      }
    },
    methods: {
      editDealConfirm () {
        this.$snotify.confirm('Изменить сделку?', 'Изменение', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.editDeal(); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      editDeal () {
        this.$emit('editRequest', this.editable_data, this.additional_data)
      },
      deleteDealConfirm () {
        this.$snotify.confirm('Удалить сделку?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.deleteDeal(this.additional_data); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      deleteDeal (rowObj) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.delete('https://beta.project.nullteam.info/api/deals/' + rowObj.deal_id).then(resp => {
              this.requests.splice(this.requests.indexOf(rowObj))
              this.$emit('update:requsets', this.requests)
              resolve({
                title: 'Успешно',
                body: 'Сделка удалена',
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
                body: 'Сделка не удалена',
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
      }
    },
    components: {
      flatPickr
    }
  }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>

    #enterprise_panel_modal_requests {
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
