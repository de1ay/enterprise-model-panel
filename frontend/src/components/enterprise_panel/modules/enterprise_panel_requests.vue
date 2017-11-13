<template>
  <div id="enterprise_panel_requests">
    <div class="requests">
      <vue-good-table
        :columns="requests_columns"
        :rows="requests"
        :paginate="true"
        :lineNumbers="true"
        :rowsPerPageText="rowsPerPage"
        :nextText="nextText"
        :prevText="prevText"
        :onClick="showDeal"
        :ofText="ofText"/>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'EnterprisePanelRequests',
    props: ['requests', 'billings', 'media', 'clients', 'deals'],
    data () {
      return {
        ofText: 'из',
        nextText: 'След.',
        prevText: 'Пред.',
        rowsPerPage: 'Показывать строк:',
        requests_columns: [
          {
            label: 'Место',
            field: 'deal_media.media_name'
          },
          {
            label: 'Заказчик',
            field: 'deal_client.client_name'
          },
          {
            label: 'Бренд',
            field: 'deal_brand'
          },
          {
            label: 'Сумма',
            field: 'deal_sum',
            type: 'number'
          },
          {
            label: 'Начало',
            field: 'start_date',
            type: 'date',
            inputFormat: 'MM/DD/YYYY',
            outputFormat: 'DD/MM/YYYY'
          },
          {
            label: 'Конец',
            field: 'end_date',
            type: 'date',
            inputFormat: 'MM/DD/YYYY',
            outputFormat: 'DD/MM/YYYY'
          },
          {
            label: 'Статус',
            field: this.parseStatus
          }
        ]
      }
    },
    methods: {
      parseStatus (rowObj) {
        switch (rowObj.deal_status) {
          case '0': return 'В обработке'
          case '1': return 'Ожидается оплата'
          case '2': return 'Оплачен'
          case '3': return 'Активен'
          case '4': return 'Завершён'
          default: return 'Ошибка'
        }
      },
      showDeal (rowObj, index) {
        this.$emit('showModal', 'enterprise_panel_requests_view', rowObj)
      }
    }
  }
</script>

<style>

  #enterprise_panel_requests { margin:50px; }

  .requests .table-bordered th, .requests .table.table-bordered td {
    border-top: none !important;
    border-right: none !important;
    border-left: none !important;
    border-bottom: 0.5px rgba(52, 152, 219, 0.4) solid !important;
  }

  .requests .table.condensed thead th, .requests .table thead th {
    background-color: #3498db !important;
    color: #fff;
  }

  .requests .good-table .table-footer {
    background: transparent;
    border: none;
  }

  .requests .good-table .table-footer .pagination-controls {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .requests .table .sorting-asc, .requests .table .sorting-desc {
    color: #fff !important;
    user-select: none;
  }

  .requests .table .sorting-asc:after, .requests .table .sorting-desc:after {
    border-top-color: #fff !important;
    border-bottom-color: #fff !important;
  }

  .requests .good-table .table tbody th.line-numbers {
    background-color: transparent !important;
  }

  .requests .good-table .table-footer .pagination-controls .info { font-size: 14px; }

</style>
