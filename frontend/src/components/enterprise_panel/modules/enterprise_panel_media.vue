<template>
  <div id="enterprise_panel_media">
    <div class="media">
      <vue-good-table
        :columns="media_columns"
        :rows="media"
        :paginate="true"
        :lineNumbers="true"
        :rowsPerPageText="rowsPerPage"
        :nextText="nextText"
        :prevText="prevText"
        :onClick="deleteMediaConfirm"
        :ofText="ofText"/>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'EnterprisePanelMedia',
    props: ['requests', 'billings', 'media', 'clients', 'deals'],
    data () {
      return {
        ofText: 'из',
        nextText: 'След.',
        prevText: 'Пред.',
        rowsPerPage: 'Показывать строк:',
        media_columns: [
          {
            label: 'Название',
            field: 'media_name'
          },
          {
            label: 'Адрес',
            field: 'media_address'
          },
          {
            label: 'Тип',
            field: this.parseMediaType
          }
        ]
      }
    },
    methods: {
      parseMediaType (rowObj) {
        switch (rowObj.media_type) {
          case '1': return 'Баннер'
          case '2': return 'Радиостанция'
          default: return 'Ошибка'
        }
      },
      deleteMediaConfirm (rowObj, index) {
        this.$snotify.confirm('Удалить медиа-носитель?', 'Удаление', {
          timeout: 2000,
          showProgressBar: true,
          closeOnClick: false,
          pauseOnHover: true,
          buttons: [
            {text: 'Да', action: (notifyId) => { this.deleteMedia(rowObj); this.$snotify.remove(notifyId) }},
            {text: 'Нет', action: (notifyId) => this.$snotify.remove(notifyId)}
          ]
        })
      },
      deleteMedia (rowObj) {
        this.$snotify.async(
          'Запрос выполняется',
          'Подождите...',
          () => new Promise((resolve, reject) => {
            axios.delete('https://beta.project.nullteam.info/api/media/' + rowObj.media_id).then(resp => {
              this.media.splice(this.media.indexOf(rowObj))
              this.$emit('update:media', this.media)
              resolve({
                title: 'Успешно',
                body: 'Медиа-носитель удален',
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
                body: 'Медиа-носитель не удален',
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

  #enterprise_panel_media { margin:50px; }

  .media .table-bordered th, .media .table.table-bordered td {
    border-top: none !important;
    border-right: none !important;
    border-left: none !important;
    border-bottom: 0.5px rgba(52, 152, 219, 0.4) solid !important;
  }

  .media .table.condensed thead th, .media .table thead th {
    background-color: #3498db !important;
    color: #fff;
  }

  .media .good-table .table-footer {
    background: transparent;
    border: none;
  }

  .media .good-table .table-footer .pagination-controls {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .media .table .sorting-asc, .media .table .sorting-desc {
    color: #fff !important;
    user-select: none;
  }

  .media .table .sorting-asc:after, .media .table .sorting-desc:after {
    border-top-color: #fff !important;
    border-bottom-color: #fff !important;
  }

  .media .good-table .table tbody th.line-numbers {
    background-color: transparent !important;
  }

  .media .good-table .table-footer .pagination-controls .info { font-size: 14px; }

</style>
