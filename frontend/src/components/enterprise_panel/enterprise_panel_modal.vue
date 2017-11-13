<template>
  <div id="enterprise_panel_modal" @click="hideModal">
    <div class="modal">
      <component
        :is="modal_name"
        :requests.sync="requests"
        :billings.sync="billings"
        :media.sync="media"
        :deals.sync="deals"
        :clients.sync="clients"
        :additional_data="additional_data"
        @hideModal="hideModal"
        @addRequest="addRequest"
        @addMedia="addMedia"
        @addClient="addClient"
        @addBilling="addBilling"
        @editRequest="editRequest"
        @editMedia="editMedia"
        @editClient="editClient"
        @editBilling="editBilling">
      </component>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import EnterprisePanelModalRequestsView from '@/components/enterprise_panel/modals/enterprise_panel_modal_requests_view'
  import EnterprisePanelModalRequestsAdd from '@/components/enterprise_panel/modals/enterprise_panel_modal_requests_add'
  import EnterprisePanelModalClientsView from '@/components/enterprise_panel/modals/enterprise_panel_modal_clients_view'
  import EnterprisePanelModalClientsAdd from '@/components/enterprise_panel/modals/enterprise_panel_modal_clients_add'
  import EnterprisePanelModalMediaAdd from '@/components/enterprise_panel/modals/enterprise_panel_modal_media_add'
  import EnterprisePanelModalMediaView from '@/components/enterprise_panel/modals/enterprise_panel_modal_media_view'
  import EnterprisePanelModalBillingsView from '@/components/enterprise_panel/modals/enterprise_panel_modal_billings_view'
  import EnterprisePanelModalBillingsAdd from '@/components/enterprise_panel/modals/enterprise_panel_modal_billings_add'
  export default {
    name: 'EnterprisePanelModal',
    props: ['requests', 'billings', 'modal_name', 'modal_active', 'media', 'clients', 'deals', 'additional_data'],
    components: {
      'enterprise_panel_requests_view': EnterprisePanelModalRequestsView,
      'enterprise_panel_requests_add': EnterprisePanelModalRequestsAdd,
      'enterprise_panel_clients_view': EnterprisePanelModalClientsView,
      'enterprise_panel_clients_add': EnterprisePanelModalClientsAdd,
      'enterprise_panel_media_view': EnterprisePanelModalMediaView,
      'enterprise_panel_media_add': EnterprisePanelModalMediaAdd,
      'enterprise_panel_billings_add': EnterprisePanelModalBillingsAdd,
      'enterprise_panel_billings_view': EnterprisePanelModalBillingsView
    },
    methods: {
      showModal (modalName) {
        this.$emit('showModal', modalName)
      },
      hideModal (e, flag = false) {
        if (flag || e.target.id === 'enterprise_panel_modal') {
          this.$emit('update:modal_active', false)
        }
      },
      addRequest (deal) {
        deal.deal_period = deal.start_date + '-' + deal.end_date + ';'
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.post('https://beta.project.nullteam.info/api/deals/', {
              deal_client: deal.deal_client.client_id,
              deal_brand: deal.deal_brand,
              deal_media: deal.deal_media.media_id,
              deal_period: deal.deal_period,
              deal_time: deal.deal_time,
              deal_status: deal.deal_status,
              deal_sum: deal.deal_sum,
              deal_paid: deal.deal_paid
            }).then(resp => {
              this.deals.push(resp.data)
              this.$emit('update:deals', this.deals)
              this.requests.push({
                deal_id: resp.data.deal_id,
                deal_client: deal.deal_client,
                deal_brand: deal.deal_brand,
                deal_media: deal.deal_media,
                deal_period: deal.deal_period,
                deal_time: deal.deal_time,
                deal_status: deal.deal_status,
                deal_sum: deal.deal_sum,
                deal_paid: deal.deal_paid,
                start_date: deal.start_date,
                end_date: deal.end_date
              })
              resolve({
                title: 'Успешно',
                body: 'Сделка добавлена',
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
                body: 'Сделка не добавлена',
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
        this.$emit('update:requests', this.requests)
        this.$emit('update:modal_active', false)
      },
      editRequest (newRequest, originalRequest) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.put('https://beta.project.nullteam.info/api/deals/' + newRequest.deal_id, {
              deal_client: newRequest.deal_client.client_id,
              deal_brand: newRequest.deal_brand,
              deal_media: newRequest.deal_media.media_id,
              deal_period: newRequest.start_date + '-' + newRequest.end_date + ';',
              deal_time: newRequest.deal_time,
              deal_status: newRequest.deal_status,
              deal_sum: newRequest.deal_sum,
              deal_paid: newRequest.deal_paid
            }).then(resp => {
              originalRequest = Object.assign(originalRequest, newRequest)
              resolve({
                title: 'Успешно',
                body: 'Сделка изменена',
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
                body: 'Сделка не изменена',
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
        this.$emit('update:modal_active', false)
      },
      addMedia (media) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.post('https://beta.project.nullteam.info/api/media/', {
              media_name: media.media_name,
              media_address: media.media_address,
              media_type: media.media_type
            }).then(resp => {
              this.media.push(resp.data)
              this.$emit('update:media', this.media)
              resolve({
                title: 'Успешно',
                body: 'Медиа-носитель добавлен',
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
                body: 'Медиа-носитель не добавлен',
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
        this.$emit('update:modal_active', false)
      },
      editMedia (newMedia, originalMedia) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.put('https://beta.project.nullteam.info/api/media/' + newMedia.media_id, {
              media_type: newMedia.media_type,
              media_name: newMedia.media_name
            }).then(resp => {
              originalMedia = Object.assign(originalMedia, newMedia)
              resolve({
                title: 'Успешно',
                body: 'Медиа-носитель изменён',
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
                body: 'Медиа-носитель не изменён',
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
        this.$emit('update:modal_active', false)
      },
      addBilling (billing) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.post('https://beta.project.nullteam.info/api/billings/', {
              billing_deal: billing.billing_deal,
              billing_sum: billing.billing_sum,
              billing_date: billing.billing_date
            }).then(resp => {
              this.billings.push({
                billing_id: resp.data.billing_id,
                billing_sum: resp.data.billing_sum,
                billing_date: resp.data.billing_date,
                billing_deal: resp.data.billing_deal,
                billing_deal_info: billing.billing_deal_info
              })
              this.$emit('update:billings', this.billings)
              resolve({
                title: 'Успешно',
                body: 'Оплата добавлена',
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
                body: 'Оплата не добавлена',
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
        this.$emit('update:modal_active', false)
      },
      editBilling (newBilling, originalBilling) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.put('https://beta.project.nullteam.info/api/billings/' + newBilling.billing_id, {
              billing_deal: newBilling.billing_deal,
              billing_date: newBilling.billing_date,
              billing_sum: newBilling.billing_sum
            }).then(resp => {
              originalBilling = Object.assign(originalBilling, newBilling)
              resolve({
                title: 'Успешно',
                body: 'Оплата изменена',
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
                body: 'Оплата не изменена',
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
        this.$emit('update:modal_active', false)
      },
      addClient (client) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.post('https://beta.project.nullteam.info/api/clients/', {
              client_name: client.client_name
            }).then(resp => {
              this.clients.push(resp.data)
              this.$emit('update:clients', this.clients)
              resolve({
                title: 'Успешно',
                body: 'Клиент добавлен',
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
                body: 'Клиент не добавлен',
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
        this.$emit('update:modal_active', false)
      },
      editClient (newClient, originalClient) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.put('https://beta.project.nullteam.info/api/clients/' + newClient.client_id, {
              client_name: newClient.client_name
            }).then(resp => {
              originalClient = Object.assign(originalClient, newClient)
              resolve({
                title: 'Успешно',
                body: 'Клиент изменён',
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
                body: 'Клиент не изменён',
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
        this.$emit('update:modal_active', false)
      }
    }
  }
</script>

<style>

    #enterprise_panel_modal {
        z-index: 1000;
        position: fixed;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
        background: rgba(0, 0, 0, 0.3);
    }

    .modal {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-width: 350px;
        min-height: 200px;
        border-radius: 5px;
        background: #ecf0f1;
    }

    #enterprise_panel_modal .form-field {
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

    #enterprise_panel_modal .form-field:first-child {
        margin: 30px 0 15px 0;
    }

    #enterprise_panel_modal .form-field .fa-icon { color: #95a5a6; }

    #enterprise_panel_modal .form-field .form-field__icon--lock {
        margin-top: 4px;
    }

    #enterprise_panel_modal .form-field .form-field__input {
        width: 240px;
        height: 35px;
        font-size: 18px;
        color: #95a5a6;
        border: none;
        outline: none;
    }

    #enterprise_panel_modal .form-field .form-field__input::-webkit-input-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field .form-field__input:-moz-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field .form-field__input::-moz-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field .form-field__input:-ms-input-placeholder { color: #95a5a6; }

    #enterprise_panel_modal .form-field__input .multiselect__tags {
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

    #enterprise_panel_modal .form-field__input .multiselect__tags input {
        margin: 0;
        padding: 0;
        height: 35px;
        font-size: 18px;
        color: #95a5a6;
    }

    #enterprise_panel_modal .form-field__input .multiselect__tags input::-webkit-input-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field__input .multiselect__tags input:-moz-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field__input .multiselect__tags input::-moz-placeholder { color: #95a5a6; }
    #enterprise_panel_modal .form-field__input .multiselect__tags input:-ms-input-placeholder { color: #95a5a6; }

</style>
