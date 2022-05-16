<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
<template>
  <div id="nav">
    <el-menu mode="horizontal" :default-active="routerIndex" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" router=true @select="selectItems">
      <el-sub-menu index="1">
        <template #title>Map Analysis</template>
        <el-menu-item index="/Hacromap">COVID Cases and Camera Sensor Map</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>Timeline Analysis</template>
        <el-menu-item index="/symptomtimelineanalysis">Hashtag Timeline Analysis</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3">
        <template #title>Sentiment and Subjectivity</template>
        <el-menu-item index="/agedistribution">Sentiment and Subjectivity from Wave-1 to Wave-4</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="4">
        <template #title>Correlation Analysis</template>
        <el-menu-item index="/depressionanalysis">Correlation and Topic analysis for waves</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="5">
        <template #title>Project and Team</template>
        <el-menu-item index="/teaminformation">Team Member Information </el-menu-item>
        <el-menu-item index="/projectinformation">Project Structure</el-menu-item>
      </el-sub-menu>
      <el-menu-item index="/">Home</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      routerIndex: '/',
    }
  },
  mounted() {
    this.$router.push('/');
  },
  methods: {
    selectItems(index, indexPath, item, routerIndex) {
    }
  }
};
</script>

<style scoped>
</style>
