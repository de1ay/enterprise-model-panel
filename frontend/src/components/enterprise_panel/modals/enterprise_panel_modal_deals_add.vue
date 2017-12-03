<template>
    <form id="enterprise_panel_modal_deals">
      <div class="column-container">
        <div class="form-field">
            <multiselect
                class="form-field__input"
                v-model="deal_client"
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
            v-model.trim="deal_brand"
            type="text"
            placeholder="Бренд">
            <icon name="newspaper-o" scale="1.2" class="form-field__icon--lock"></icon>
        </div>
        <div class="form-field">
            <multiselect
            class="form-field__input"
            v-model="deal_media"
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
                v-model="deal_type"
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
            v-model.trim.number="deal_sum"
            type="number"
            placeholder="Сумма">
            <icon name="money" scale="1.2" class="form-field__icon--money"></icon>
        </div>
        <div class="form-field">
            <input
            class="form-field__input"
            v-model.trim.number="deal_time"
            type="number"
            placeholder="Длительность">
            <icon name="clock-o" scale="1.2" class="form-field__icon--clock"></icon>
        </div>
        <div class="form-field__actions">
            <input class="form-field__submit" @click.prevent="addDeal" type="submit" value="Создать"/>
        </div>
      </div>
      <div class="column-container">
        <div class="form-field form-field--period" @click="deal_periods.splice(deal_periods.indexOf(period), 1)" v-for="period in deal_periods">
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
    </form>
</template>

<script>
  import 'vue-awesome/icons/handshake-o'
  import 'vue-awesome/icons/calendar-o'
  import 'vue-awesome/icons/globe'
  import 'vue-awesome/icons/money'
  import 'vue-awesome/icons/newspaper-o'
  import 'vue-awesome/icons/flag-o'
  import 'vue-awesome/icons/flag-checkered'
  import 'vue-awesome/icons/clock-o'
  import moment from 'moment'
  import flatPickr from 'vue-flatpickr-component'
  import 'flatpickr/dist/flatpickr.css'
  import {Russian} from 'flatpickr/dist/l10n/ru'
  export default {
    name: 'EnterprisePanelModalDealsAdd',
    props: ['billings', 'clients', 'media', 'deals'],
    data () {
      return {
        deal_client: null,
        deal_brand: '',
        deal_media: null,
        deal_sum: '',
        deal_type: '',
        deal_periods: [],
        deal_time: '',
        start_date: '',
        end_date: '',
        date_config: {
          dateFormat: 'd/m/Y',
          locale: Russian
        },
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
      addDeal () {
        if (this.deal_client === null) {
          this.$snotify.error('Поле "Клиент" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_brand === '') {
          this.$snotify.error('Поле "Бренд" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_media === null) {
          this.$snotify.error('Поле "Медиа" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_sum === '') {
          this.$snotify.error('Поле "Сумма" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_periods === []) {
          this.$snotify.error('Периоды отсутствуют', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_type === '') {
          this.$snotify.error('Поле "Тип сделки" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        if (this.deal_time === '') {
          this.$snotify.error('Поле "Длительность" не может быть пустым', 'Ошибка', {
            closeOnClick: true,
            timeout: 2000,
            showProgressBar: true,
            pauseOnHover: true})
          return
        }
        let dealPeriod = ''
        let dates = []
        this.deal_periods.forEach(period => {
          dealPeriod += period.period_date + ';'
          dates.push(period.period_start)
          dates.push(period.period_end)
        })
        dates = dates.sort((date1, date2) => {
          return moment(date1, 'DD/MM/YYYY').toDate() > moment(date2, 'DD/MM/YYYY').toDate()
        })
        this.$emit('addDeal', {
          deal_client: this.deal_client.client_id,
          deal_client_info: this.deal_client,
          deal_brand: this.deal_brand,
          deal_media: this.deal_media.media_id,
          deal_media_info: this.deal_media,
          deal_sum: this.deal_sum,
          deal_time: this.deal_time,
          deal_type: this.deal_type.type_id,
          deal_type_info: this.deal_type,
          deal_paid: 0,
          deal_period: dealPeriod,
          deal_periods: this.deal_periods,
          deal_status: '0',
          start_date: dates[0],
          end_date: dates[dates.length - 1]
        })
      },
      addPeriod () {
        if (this.start_date !== '' && this.end_date !== '') {
          this.deal_periods.push({
            period_start: this.start_date,
            period_end: this.end_date,
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
      width: 700px;
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
