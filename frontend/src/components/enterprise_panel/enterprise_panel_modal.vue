<template>
  <div id="enterprise_panel_modal" @click="hideModal">
    <div class="modal">
      <component 
        :is="modal_type"
        :requests.sync="requests"
        :billings.sync="billings"
        @addRequest="addRequest">
      </component>
    </div>
  </div>
</template>

<script>
  import EnterprisePanelModalRequests from '@/components/enterprise_panel/modals/enterprise_panel_modal_requests'
  export default {
    name: 'EnterprisePanelModal',
    props: ['requests', 'billings', 'modal_type', 'modal_active'],
    data () {
      return {
        temp: ''
      }
    },
    components: {
      'enterprise_panel_modal_requests': EnterprisePanelModalRequests
    },
    methods: {
      hideModal (e) {
        if (e.target.id === 'enterprise_panel_modal') {
          this.$emit('update:modal_active', false)
        }
      },
      addRequest (request) {
        this.requests.push(request)
        this.$emit('update:requests', this.requests)
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
