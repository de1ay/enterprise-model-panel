<template>
    <form id="enterprise_panel_modal_requests">
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
            <input class="form-field__submit" @click.prevent="addRequest" type="submit" value="Создать"/>
        </div>
    </form>
</template>

<script>
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
    name: 'EnterprisePanelModalRequests',
    props: ['requests', 'billings', 'clients', 'media', 'deals'],
    data () {
      return {
        deal_client: null,
        deal_brand: '',
        deal_media: null,
        deal_sum: '',
        deal_time: '',
        start_date: '',
        end_date: '',
        date_config: {
          altFormat: 'd/m/Y',
          altInput: true,
          dateFormat: 'm/d/Y',
          locale: Russian
        }
      }
    },
    methods: {
      addRequest () {
        this.$emit('addRequest', {
          deal_client: this.deal_client,
          deal_brand: this.deal_brand,
          deal_media: this.deal_media,
          deal_sum: this.deal_sum,
          deal_time: this.deal_time,
          deal_paid: 0,
          start_date: this.start_date,
          end_date: this.end_date,
          deal_status: '0'
        })
      }
    },
    components: {
      flatPickr
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
