<template>
  <div id="enterprise_panel_modal" @click="hideModal">
    <div class="modal">
      <component 
        :is="modal_type"
        :requests.sync="requests"
        :billings.sync="billings"
        :media.sync="media"
        :deals.sync="deals"
        :clients.sync="clients"
        @addRequest="addRequest"
        @addMedia="addMedia"
        @addClient="addClient">
      </component>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import EnterprisePanelModalRequests from '@/components/enterprise_panel/modals/enterprise_panel_modal_requests'
  import EnterprisePanelModalClients from '@/components/enterprise_panel/modals/enterprise_panel_modal_clients'
  import EnterprisePanelModalMedia from '@/components/enterprise_panel/modals/enterprise_panel_modal_media'
  export default {
    name: 'EnterprisePanelModal',
    props: ['requests', 'billings', 'modal_type', 'modal_active', 'media', 'clients', 'deals'],
    components: {
      'enterprise_panel_modal_requests': EnterprisePanelModalRequests,
      'enterprise_panel_modal_clients': EnterprisePanelModalClients,
      'enterprise_panel_modal_media': EnterprisePanelModalMedia
    },
    methods: {
      hideModal (e) {
        if (e.target.id === 'enterprise_panel_modal') {
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
      }
    }
  }
</script>

<style scoped>

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

</style>
