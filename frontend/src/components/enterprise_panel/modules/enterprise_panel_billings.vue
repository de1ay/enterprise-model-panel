<template>
  <div id="enterprise_panel_billings">
    <div class="billings">
      <vue-good-table
        :columns="billings_columns"
        :rows="billings"
        :paginate="true"
        :lineNumbers="true"
        :rowsPerPageText="rowsPerPage"
        :nextText="nextText"
        :prevText="prevText"
        :onClick="showBilling"
        :ofText="ofText"/>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'EnterprisePanelBillings',
    props: ['requests', 'billings'],
    data () {
      return {
        ofText: 'из',
        nextText: 'След.',
        prevText: 'Пред.',
        rowsPerPage: 'Показывать строк:',
        billings_columns: [
          {
            label: 'Заказчик',
            field: 'billing_deal_info.deal_client.client_name'
          },
          {
            label: 'Бренд',
            field: 'billing_deal_info.deal_brand'
          },
          {
            label: 'Сумма',
            field: 'billing_sum',
            type: 'number'
          },
          {
            label: 'Дата',
            field: 'billing_date',
            type: 'date',
            inputFormat: 'MM/DD/YYYY',
            outputFormat: 'DD/MM/YYYY'
          }
        ]
      }
    },
    methods: {
      showBilling (rowObj, index) {
        this.$emit('showModal', 'enterprise_panel_billings_view', rowObj)
      }
    }
  }
</script>

<style>

  #enterprise_panel_billings { margin:50px; }

  .billings .table-bordered th, .billings .table.table-bordered td {
    border-top: none !important;
    border-right: none !important;
    border-left: none !important;
    border-bottom: 0.5px rgba(52, 152, 219, 0.4) solid !important;
  }

  .billings .table.condensed thead th, .billings .table thead th {
    background-color: #3498db !important;
    color: #fff;
  }

  .billings .good-table .table-footer {
    background: transparent;
    border: none;
  }

  .billings .good-table .table-footer .pagination-controls {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .billings .table .sorting-asc, .billings .table .sorting-desc {
    color: #fff !important;
    user-select: none;
  }

  .billings .table .sorting-asc:after, .billings .table .sorting-desc:after {
    border-top-color: #fff !important;
    border-bottom-color: #fff !important;
  }

  .billings .good-table .table tbody th.line-numbers {
    background-color: transparent !important;
  }

  .billings .good-table .table-footer .pagination-controls .info { font-size: 14px; }

</style>
