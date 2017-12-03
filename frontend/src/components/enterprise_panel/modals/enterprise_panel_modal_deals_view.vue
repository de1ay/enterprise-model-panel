<template>
    <div id="enterprise_panel_modal_deals">
      <div class="column-container">
        <div class="form-field">
            <multiselect
                class="form-field__input"
                v-model="editable_data.deal_client_info"
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
            v-model="editable_data.deal_media_info"
            :options="media"
            label="media_name"
            track-by="media_id"
            :show-labels="false"
            :allow-empty="false"
            placeholder="Медиа-носитель"></multiselect>
            <icon name="globe" scale="1.2" class="form-field__icon--globe"></icon>
        </div>
        <div class="form-field">
            <multiselect
                class="form-field__input"
                v-model="editable_data.deal_type_info"
                :options="deal_types"
                label="type_name"
                track-by="type_id"
                :allow-empty="false"
                :show-labels="false"
                placeholder="Тип сделки"></multiselect>
            <icon name="handshake-o" scale="1.2" class="form-field__icon--hadnshake"></icon>
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
        <div class="form-field__actions">
          <button class="form-field__edit" @click.prevent="editDealConfirm">Изменить</button>
          <button class="form-field__delete" @click.prevent="deleteDealConfirm">Удалить</button>
        </div>
      </div>
      <div class="column-container">
        <div class="form-field form-field--period"
             @click="editable_data.deal_periods.splice(editable_data.deal_periods.indexOf(period), 1)"
             v-for="period in editable_data.deal_periods">
          <span class="form-field__input">{{period.period_date}}</span>
          <icon name="calendar-o" scale="1.2" class="form-field__icon--close"></icon>
        </div>
        <div class="form-field">
            <flat-pickr
            v-model="start_date"
            class="form-field__input"
            :config="date_config"
            placeholder="Начальная дата"></flat-pickr>
            <icon name="flag-o" scale="1.2" class="form-field__icon--flag"></icon>
        </div>
        <div class="form-field">
            <flat-pickr
            v-model="end_date"
            class="form-field__input"
            :config="date_config"
            placeholder="Конечная дата"></flat-pickr>
            <icon name="flag-checkered" scale="1.2" class="form-field__icon--flag"></icon>
        </div>
        <div class="form-field__actions">
          <button class="form-field__add" @click.prevent="addPeriod">Добавить период</button>
        </div>
      </div>
    </div>
</template>

<script>
  import moment from 'moment'
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
    name: 'EnterprisePanelModalDealsView',
    props: ['billings', 'clients', 'media', 'deals', 'additional_data'],
    data () {
      return {
        editable_data: Object.assign({}, this.additional_data),
        date_config: {
          dateFormat: 'd/m/Y',
          locale: Russian
        },
        start_date: '',
        end_date: '',
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
        ],
        deal_types: [
          {
            type_id: '0',
            type_name: 'Размещение'
          },
          {
            type_id: '1',
            type_name: 'Сбыт'
          },
          {
            type_id: '2',
            type_name: 'Изготовление'
          },
          {
            type_id: '3',
            type_name: 'Реализация'
          },
          {
            type_id: '4',
            type_name: 'Бартер'
          }
        ]
      }
    },
    methods: {
      addPeriod () {
        if (this.start_date !== '' && this.end_date !== '') {
          this.editable_data.deal_periods.push({
            period_start: this.start_date,
            period_end: this.period_end,
            period_date: this.start_date + '-' + this.end_date
          })
          this.start_date = ''
          this.end_date = ''
        } else {
          this.$snotify.error('Дата не может быть пустой', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
        }
      },
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
        this.editable_data.deal_type = this.editable_data.deal_type_info.type_id
        this.editable_data.deal_client = this.editable_data.deal_client_info.client_id
        this.editable_data.deal_media = this.editable_data.deal_media_info.media_id
        let dealPeriod = ''
        let dates = []
        this.editable_data.deal_periods.forEach(period => {
          dealPeriod += period.period_date + ';'
          dates.push(period.period_start)
          dates.push(period.period_end)
        })
        dates = dates.sort((date1, date2) => {
          return moment(date1, 'DD/MM/YYYY').toDate() > moment(date2, 'DD/MM/YYYY').toDate()
        })
        this.editable_data.deal_period = dealPeriod
        this.editable_data.start_date = dates[0]
        this.editable_data.end_date = dates[dates.length - 1]
        if (this.editable_data.deal_status !== '4' && this.editable_data.deal_status !== '3') {
          if (this.editable_data.deal_paid >= this.editable_data.deal_sum) {
            this.editable_data.deal_status = '2'
          } else {
            this.editable_data.deal_status = '1'
          }
        }
        if (this.editable_data.deal_status === '2' && new Date() > moment(this.editable_data.start_date, 'DD/MM/YYYY').toDate() && new Date() < moment(this.editable_data.end_date, 'DD/MM/YYYY').toDate()) {
          this.editable_data.deal_status = '3'
        }
        if (this.editable_data.deal_status !== '4' && new Date() > moment(this.editable_data.end_date, 'DD/MM/YYYY').toDate()) {
          this.editable_data.deal_status = '4'
        }
        this.$emit('editDeal', this.editable_data, this.additional_data)
      },
      deleteDealConfirm () {
        this.$snotify.confirm('Удалить сделку?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.$emit('deleteDeal', this.additional_data); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      }
    },
    components: {
      flatPickr
    }
  }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>

    #enterprise_panel_modal_deals {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .column-container {
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: center;
      min-height: 506px;
      margin: 0 15px;
    }

    .form-field--period:hover { cursor: pointer }

    .form-field--period span {
      margin-top: 11px;
    }

    .form-field__add {
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
