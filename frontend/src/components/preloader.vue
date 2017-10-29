<template>
    <div id="enterprise_panel_preloader">
        <icon class="preloader-icon" name="cog" scale="5" spin></icon>
    </div>
</template>

<script>
    import 'vue-awesome/icons/cog'
    export default {
      name: 'EnterprisePanelPreloader'
    }
</script>

<style scoped>

    #enterprise_panel_preloader {
        z-index: 10000;
        position: fixed;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 100vh;
        background: #3498db;
        color: #fff;
    }

    .preloader-icon {
        color: #fff;
    }

</style>