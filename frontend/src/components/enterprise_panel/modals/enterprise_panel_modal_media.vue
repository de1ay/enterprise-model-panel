<template>
    <div id="enterprise_panel_modal_requests">
        <div class="form-field">
            <input 
            class="form-field__input"
            v-model.trim="media_name" 
            type="text" 
            placeholder="Название">
            <icon name="television" scale="1.2" class="form-field__icon--tv"></icon>
        </div>
        <div class="form-field">
            <multiselect  
            class="form-field__input"
            v-model="media_type"
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
            v-model.trim.number="media_address" 
            type="text" 
            placeholder="Адрес">
            <icon name="globe" scale="1.2" class="form-field__icon--globe"></icon>
        </div>
        <div class="form-field__actions">
            <input class="form-field__submit" @click.prevent="addMedia" type="submit" value="Создать"/>
        </div>
    </div>
</template>

<script>
  import 'vue-awesome/icons/globe'
  import 'vue-awesome/icons/television'
  import 'vue-awesome/icons/bullhorn'
  export default {
    name: 'EnterprisePanelModalMedia',
    props: ['requests', 'billings', 'clients', 'media', 'deals'],
    data () {
      return {
        media_name: '',
        media_type: null,
        media_address: '',
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
      addMedia () {
        this.$emit('addMedia', {
          media_name: this.media_name,
          media_address: this.media_address,
          media_type: this.media_type.value
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
