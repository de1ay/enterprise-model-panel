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
  export default {
    name: 'EnterprisePanelGantt',
    props: ['requests', 'billings', 'media', 'clients', 'deals'],
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
    mounted () {
      this.requests.forEach((request, index) => {
        var startDate = new Date(request.start_date)
        var endDate = new Date(request.end_date)
        var duration = new Date(endDate - startDate)
        var percentComplete = 0
        if (new Date() > startDate) {
          var timeToCurrentDate = new Date(new Date() - startDate)
          percentComplete = timeToCurrentDate * 100 / duration
        }
        var row = [
          request.deal_id.toString(),
          request.deal_client.client_name,
          null,
          startDate,
          endDate,
          null,
          percentComplete,
          null
        ]
        this.rows.push(row)
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
