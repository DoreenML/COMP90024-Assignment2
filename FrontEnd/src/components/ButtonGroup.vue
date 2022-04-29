<template>
  <div>
    <el-button v-for="(item, index) in buttonArray" :key="item.key" plain :type="item.type" @click="changeDataset(item.key)">
      {{item.text}}
    </el-button>
  </div>
</template>

<script>
export default {
  props: ['buttonArray'],
  methods: {
    changeDataset(key) {
      this.$emit('changeDataset', key);
    },
  },
  mounted() {

  },
};
</script>

<style scoped>
</style>
