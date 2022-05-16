<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
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
