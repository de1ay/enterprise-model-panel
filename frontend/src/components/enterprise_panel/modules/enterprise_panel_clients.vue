<template>
  <div id="enterprise_panel_clients">
    <div class="clients">
      <vue-good-table
        :columns="clients_columns"
        :rows="clients"
        :paginate="true"
        :lineNumbers="true"
        :rowsPerPageText="rowsPerPage"
        :nextText="nextText"
        :prevText="prevText"
        :onClick="deleteClientConfirm"
        :ofText="ofText"/>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'EnterprisePanelClients',
    props: ['requests', 'billings', 'media', 'clients', 'deals'],
    data () {
      return {
        ofText: 'из',
        nextText: 'След.',
        prevText: 'Пред.',
        rowsPerPage: 'Показывать строк:',
        clients_columns: [
          {
            label: 'Имя/Название',
            field: 'client_name'
          }
        ]
      }
    },
    methods: {
      deleteClientConfirm (rowObj, index) {
        this.$snotify.confirm('Удалить клиента?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.deleteClient(rowObj); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      deleteClient (rowObj) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.delete('https://beta.project.nullteam.info/api/clients/' + rowObj.client_id).then(resp => {
              this.clients.splice(this.clients.indexOf(rowObj))
              this.$emit('update:clients', this.clients)
              resolve({
                title: 'Успешно',
                body: 'Клиент удален',
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
                body: 'Клиент не удален',
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
      }
    }
  }
</script>

<style>

  #enterprise_panel_clients { margin:50px; }

  .clients .table-bordered th, .clients .table.table-bordered td {
    border-top: none !important;
    border-right: none !important;
    border-left: none !important;
    border-bottom: 0.5px rgba(52, 152, 219, 0.4) solid !important;
  }

  .clients .table.condensed thead th, .clients .table thead th {
    background-color: #3498db !important;
    color: #fff;
  }

  .clients .good-table .table-footer {
    background: transparent;
    border: none;
  }

  .clients .good-table .table-footer .pagination-controls {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .clients .table .sorting-asc, .clients .table .sorting-desc {
    color: #fff !important;
    user-select: none;
  }

  .clients .table .sorting-asc:after, .clients .table .sorting-desc:after {
    border-top-color: #fff !important;
    border-bottom-color: #fff !important;
  }

  .clients .good-table .table tbody th.line-numbers {
    background-color: transparent !important;
  }

  .clients .good-table .table-footer .pagination-controls .info { font-size: 14px; }

</style>
