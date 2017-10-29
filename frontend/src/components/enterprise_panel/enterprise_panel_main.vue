<template>
  <div id="enterprise_panel_main">
    <enterprise_panel_preloader v-if="!contentLoaded">
    </enterprise_panel_preloader>
    <enterprise_panel_modal 
      v-if="modal_active" 
      :modal_type="modal_types[selected_module]"
      :modal_active.sync="modal_active"
      :requests.sync="requests"
      :billings.sync="billings"
      :deals.sync="deals"
      :clients.sync="clients"
      :media.sync="media">
    </enterprise_panel_modal>
    <div class="menu">
      <div class="brand">
        <span class="brand-text">NullTeam</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_clients'}"
           @click="selected_module = 'enterprise_panel_clients'">
        <icon name="user" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">{{modules_headers_headlines['enterprise_panel_clients']}}</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_media'}"
           @click="selected_module = 'enterprise_panel_media'">
        <icon name="television" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">{{modules_headers_headlines['enterprise_panel_media']}}</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_requests'}"
           @click="selected_module = 'enterprise_panel_requests'">
        <icon name="pencil-square-o" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">{{modules_headers_headlines['enterprise_panel_requests']}}</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_billings'}"
           @click="selected_module = 'enterprise_panel_billings'">
        <icon name="credit-card" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">{{modules_headers_headlines['enterprise_panel_billings']}}</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_gantt'}"
           @click="selected_module = 'enterprise_panel_gantt'">
        <icon name="calendar" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">{{modules_headers_headlines['enterprise_panel_gantt']}}</span>
      </div>
    </div>
    <div class="container">
      <div class="header">
        <div class="header-page_name">
          <span class="page_name-text">{{modules_headers_headlines[selected_module]}}</span>
        </div>
        <div class="header-actions" v-if="selected_module !== 'enterprise_panel_gantt' || selected_module !== 'enterprise_panel_billings'">
          <button @click="modal_active = !modal_active" class="actions__button">{{modules_button_text[selected_module]}}</button>
        </div>
      </div>
      <component :is="selected_module" 
      :requests.sync="requests" 
      :billings.sync="billings"
      :media.sync="media"
      :deals.sync="deals"
      :clients.sync="clients"></component>
    </div>
  </div>
</template>

<script>
  import 'vue-awesome/icons/pencil-square-o'
  import 'vue-awesome/icons/credit-card'
  import 'vue-awesome/icons/plus'
  import 'vue-awesome/icons/calendar'
  import 'vue-awesome/icons/television'
  import 'vue-awesome/icons/user'
  import axios from 'axios'
  import EnterprisePanelPreloader from '@/components/preloader'
  import EnterprisePanelRequests from '@/components/enterprise_panel/modules/enterprise_panel_requests'
  import EnterprisePanelBillings from '@/components/enterprise_panel/modules/enterprise_panel_billings'
  import EnterprisePanelGantt from '@/components/enterprise_panel/modules/enterprise_panel_gantt'
  import EnterprisePanelClients from '@/components/enterprise_panel/modules/enterprise_panel_clients'
  import EnterprisePanelMedia from '@/components/enterprise_panel/modules/enterprise_panel_media'
  import EnterprisePanelModal from '@/components/enterprise_panel/enterprise_panel_modal'
  export default {
    name: 'EnterprisePanelMain',
    data () {
      return {
        modal_active: false,
        modal_types: {
          'enterprise_panel_clients': 'enterprise_panel_modal_clients',
          'enterprise_panel_media': 'enterprise_panel_modal_media',
          'enterprise_panel_requests': 'enterprise_panel_modal_requests',
          'enterprise_panel_billings': 'enterprise_panel_modal_billings',
          'enterprise_panel_gantt': 'enterprise_panel_modal_gantt'
        },
        modules_headers_headlines: {
          'enterprise_panel_clients': 'Клиенты',
          'enterprise_panel_media': 'Медиа',
          'enterprise_panel_requests': 'Сделки',
          'enterprise_panel_billings': 'Оплата',
          'enterprise_panel_gantt': 'График'
        },
        modules_button_text: {
          'enterprise_panel_clients': 'Новый клиент',
          'enterprise_panel_media': 'Новый медиа-носитель',
          'enterprise_panel_requests': 'Новая сделка'
        },
        selected_module: 'enterprise_panel_requests',
        requests: [],
        billings: [],
        deals: [],
        media: [],
        clients: [],
        contentLoaded: false
      }
    },
    created () {
      axios.get('https://beta.project.nullteam.info/api/media/').then(resp => { this.media = resp.data })
      axios.get('https://beta.project.nullteam.info/api/clients/').then(resp => {
        this.clients = resp.data
        axios.get('https://beta.project.nullteam.info/api/deals/').then(resp => {
          this.deals = resp.data
          this.parseDeals()
          this.contentLoaded = true
        })
      })
    },
    components: {
      'enterprise_panel_clients': EnterprisePanelClients,
      'enterprise_panel_media': EnterprisePanelMedia,
      'enterprise_panel_requests': EnterprisePanelRequests,
      'enterprise_panel_billings': EnterprisePanelBillings,
      'enterprise_panel_gantt': EnterprisePanelGantt,
      'enterprise_panel_modal': EnterprisePanelModal,
      'enterprise_panel_preloader': EnterprisePanelPreloader
    },
    methods: {
      parseDeals () {
        this.deals.forEach(deal => {
          deal.deal_client = this.findClientByID(deal.deal_client)
          deal.deal_media = this.findMediaByID(deal.deal_media)
          deal.deal_period = deal.deal_period.split(';')
          let dealPeriods = deal.deal_period
          delete (deal.deal_period)
          dealPeriods.forEach((dealPeriod, index) => {
            if (dealPeriod.length > 1) {
              dealPeriod = dealPeriod.split('-')
              deal.start_date = dealPeriod[0]
              deal.end_date = dealPeriod[1]
              this.requests.push(deal)
            }
          })
        })
      },
      findClientByID (clientId) {
        try {
          return this.clients.filter((client, index) => {
            return client.client_id === clientId
          })[0]
        } catch (e) {
          return {
            client_id: 0,
            client_name: 'Клиент не найден'
          }
        }
      },
      findMediaByID (mediaId) {
        try {
          return this.media.filter((media, index) => {
            return media.media_id === mediaId
          })[0]
        } catch (e) {
          return {
            media_id: 0,
            media_name: 'Медиа-носитель не найден',
            media_type: 0,
            media_address: ''
          }
        }
      }
    }
  }
</script>

<style scoped="true">

  #enterprise_panel_main {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: stretch;
    width: 100%;
    height: 100vh;
    max-height: 100vh;
    overflow: hidden;
  }

  .menu {
    z-index: 999;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    height: 100%;
    min-width: 200px;
    background: #fff;
    box-shadow: 0.5px 0 1px 0 rgba(50, 50, 50, 0.3);
  }

  .container {
    z-index: 10;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: stretch;
    flex-grow: 1;
    overflow-y: scroll;
  }

  .header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 50px;
    width: 100%;
    background: #fff;
    box-shadow: 0 0.5px 1px 0 rgba(50, 50, 50, 0.3);
  }

  .header-page_name { margin-left: 50px; }

  .page_name-text {
    font-size: 24px;
    color: #3498db;
  }

  .header-actions {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-right: 50px;
  }

  .actions__button {
    padding: 5px 10px;
    color: #fff;
    background: #3498db;
    font-size: 18px;
    border-radius: 10px;
    border: none;
    outline: none;
    transition: all 0.3s ease-in-out;
  }

  .actions__button:hover {
    cursor: pointer;
    background: #2980b9;
  }

  .brand {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 50px;
    width: 100%;
    box-shadow: 0 0.5px 1px 0 rgba(50, 50, 50, 0.3);
  }

  .brand-text {
    font-size: 28px;
    font-weight: 800;
    color: #3498db;
  }

  .menu__item:nth-child(2) { margin-top: 50px; }

  .menu__item {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 50px;
    width: 90%;
    margin-left: 10%;
    color: #3498db;
    font-size: 24px;
    transition: all 0.3s ease-in-out;
  }

  .menu__item:hover { cursor: pointer; }

  .menu__item:not(.menu__item--active):hover {
    color: #fff;
    background: #3498db;
  }

  .menu__item--active {
    color: #fff;
    background: #3498db;
  }

  .menu__item--active:after {
    content: '';
    position: absolute;
    left: 190px;
    width: 10px;
    height: 50px;
    background: #2980b9;
  }

  .menu__item-icon {
    margin-top: 4px;
    margin-right: 10px;
  }

  .menu__item-text { text-transform: capitalize; }

</style>
