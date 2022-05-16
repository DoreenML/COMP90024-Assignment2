<template>
    <div class="header-div">
      <Header></Header>
    </div>
    <div class="view-div">
      <router-view/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.header-div {
  flex-basis: 3rem;
  flex-shrink: 0;
}

.view-div {
  flex-grow: 1;
}

.view-div {
  height: calc(100vh - 5rem);
}
</style>
