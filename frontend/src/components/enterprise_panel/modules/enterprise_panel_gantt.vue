<template>
  <div id="enterprise_panel_gantt">
    <div class="gantt">
      <vue-chart
        :chart-type="'Gantt'"
        :packages="packages"
        :options="options"
        :columns="columns"
        :rows="rows"
    ></vue-chart>
    </div>
  </div>
</template>

<script>
  import moment from 'moment'
  export default {
    name: 'EnterprisePanelGantt',
    props: ['billings', 'media', 'clients', 'deals'],
    data () {
      return {
        packages: ['gantt'],
        options: {
          width: screen.width - 316.5,
          backgroundColor: {
            fill: '#fff'
          },
          gantt: {
            criticalPathEnabled: false,
            labelStyle: {
              fontName: 'OpenSans',
              fontSize: 14,
              color: '#757575'
            },
            innerGridHorizLine: {
              fill: '#fff',
              strokeWidth: 1
            }
          }
        },
        columns: [
          {
            'type': 'string',
            'label': 'Task ID'
          },
          {
            'type': 'string',
            'label': 'Task Name'
          },
          {
            'type': 'string',
            'label': 'Resource'
          },
          {
            'type': 'date',
            'label': 'Start Date'
          },
          {
            'type': 'date',
            'label': 'End Date'
          },
          {
            'type': 'number',
            'label': 'Duration'
          },
          {
            'type': 'number',
            'label': 'Percent Complete'
          },
          {
            'type': 'string',
            'label': 'Dependencies'
          }
        ],
        rows: []
      }
    },
    created () {
      this.deals.forEach((deal, index) => {
        deal.deal_periods.forEach((period, periodIndex) => {
          let startDate = moment(period.period_start, 'DD/MM/YYYY').toDate()
          let endDate = moment(period.period_end, 'DD/MM/YYYY').toDate()
          let duration = new Date(endDate - startDate)
          let percentComplete = 0
          if (new Date() > startDate) {
            let timeToCurrentDate = new Date(new Date() - startDate)
            percentComplete = timeToCurrentDate * 100 / duration
            if (percentComplete > 100) {
              percentComplete = 100
            }
          }
          let row = [
            deal.deal_id.toString() + periodIndex.toString(),
            deal.deal_brand,
            deal.deal_client.client_name,
            startDate,
            endDate,
            null,
            percentComplete,
            null
          ]
          this.rows.push(row)
        })
      })
    }
  }
</script>

<style scoped>

  #enterprise_panel_gantt { margin:50px; }

  .gantt {
    overflow: hidden
  }

</style>
