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
            field: 'customer'
          },
          {
            label: 'Бренд',
            field: 'brand'
          },
          {
            label: 'Сумма',
            field: 'sum',
            type: 'number'
          },
          {
            label: 'Дата',
            field: 'date',
            type: 'date',
            inputFormat: 'DD/MM/YYYY',
            outputFormat: 'DD/MM/YYYY'
          }
        ]
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
    border-bottom: 0.5px rgba(46,204,113, 0.4) solid !important;
  }

  .billings .table.condensed thead th, .billings .table thead th {
    background-color: #2ecc71 !important;
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
