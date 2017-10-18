<template>
  <div id="enterprise_panel_main">
    <div class="menu">
      <div class="brand">
        <span class="brand-text">NullTeam</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_requests'}"
           @click="selected_module = 'enterprise_panel_requests'">
        <icon name="pencil-square-o" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">заявки</span>
      </div>
      <div class="menu__item"
           :class="{'menu__item--active': selected_module === 'enterprise_panel_billings'}"
           @click="selected_module = 'enterprise_panel_billings'">
        <icon name="credit-card" scale="1" class="menu__item-icon"></icon>
        <span class="menu__item-text">оплата</span>
      </div>
    </div>
    <div class="container">
      <div class="header">
        <div class="header-page_name">
          <span class="page_name-text">{{modules_headers_headlines[selected_module]}}</span>
        </div>
        <div class="header-actions" v-if="selected_module === 'enterprise_panel_requests'">
          <button class="actions__button">Создать заявку</button>
        </div>
      </div>
      <component :is="selected_module" :requests.sync="requests" :billings.sync="billings"></component>
    </div>
  </div>
</template>

<script>
  import 'vue-awesome/icons/pencil-square-o'
  import 'vue-awesome/icons/credit-card'
  import 'vue-awesome/icons/plus'
  import EnterprisePanelRequests from '@/components/enterprise_panel/modules/enterprise_panel_requests'
  import EnterprisePanelBillings from '@/components/enterprise_panel/modules/enterprise_panel_billings'
  export default {
    name: 'EnterprisePanelMain',
    data () {
      return {
        modules_headers_headlines: {
          'enterprise_panel_requests': 'Заявки',
          'enterprise_panel_billings': 'Оплата'
        },
        selected_module: 'enterprise_panel_requests',
        requests: [
          {
            id: 1,
            customer: 'Таттелеком',
            place: 'Проспект победы',
            brand: 'Летай',
            sum: 100,
            duration: 10,
            status: 'Оплачен',
            billing_date: '12/10/2017',
            start_date: '22/10/2017',
            end_date: '24/10/2017'
          },
          {
            id: 2,
            customer: 'Ак-Барс Банк',
            place: 'Ул. Мавлютова',
            brand: 'Ак-Барс Банк',
            sum: 80,
            duration: 6,
            status: 'В обработке',
            billing_date: '12/11/2017',
            start_date: '22/11/2017',
            end_date: '24/11/2017'
          }
        ],
        billings: [
          {
            id: 1,
            customer: 'Таттелеком',
            brand: 'Летай',
            sum: 100,
            date: '12/10/2017'
          }
        ]
      }
    },
    methods: {

    },
    components: {
      'enterprise_panel_requests': EnterprisePanelRequests,
      'enterprise_panel_billings': EnterprisePanelBillings
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
    color: #2ecc71;
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
    background: #2ecc71;
    font-size: 18px;
    border-radius: 10px;
    border: none;
    outline: none;
    transition: all 0.3s ease-in-out;
  }

  .actions__button:hover {
    cursor: pointer;
    background: #27ae60;
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
    color: #2ecc71;
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
    color: #2ecc71;
    font-size: 24px;
    transition: all 0.3s ease-in-out;
  }

  .menu__item:hover { cursor: pointer; }

  .menu__item:not(.menu__item--active):hover {
    color: #fff;
    background: #2ecc71;
  }

  .menu__item--active {
    color: #fff;
    background: #2ecc71;
  }

  .menu__item--active:after {
    content: '';
    position: absolute;
    left: 190px;
    width: 10px;
    height: 50px;
    background: #27ae60;
  }

  .menu__item-icon {
    margin-top: 4px;
    margin-right: 10px;
  }

  .menu__item-text { text-transform: capitalize; }

</style>
