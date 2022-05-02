<template>
  <div id="nav">
    <el-menu mode="horizontal" :default-active="routerIndex" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" router=true @select="selectItems">
      <el-sub-menu index="1">
        <template #title>Health Anlysis</template>
        <el-menu-item index="/Hacromap">Hospital Resources and COVID cases Map</el-menu-item>
        <el-menu-item index="/healthrelatedtopictrend">Health Related Topic Trend</el-menu-item>
        <el-menu-item index="/symptomtimelineanalysis">COVID Symptom Timeline Analysis</el-menu-item>
        <el-menu-item index="depressionanalysis">COVID and Depression Analysis</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="2">
        <template #title>Income Analysis</template>
        <el-menu-item index="/Hacromap">Income Level and COVID cases Map</el-menu-item>
        <el-menu-item index="/Hacromap">Motion assessment method</el-menu-item>
        <el-menu-item index="/Hacromap">Dose calculation dataset</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3">
        <template #title>Crime Analysis</template>
        <el-menu-item index="/Hacromap">Crime Cases and COVID Cases Map</el-menu-item>
        <el-menu-item index="/Hacromap">IGRT matching procedures</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="4">
        <template #title>Real Estate Analysis</template>
        <el-menu-item index="/Hacromap">Real Estate price and COVID Map</el-menu-item>
        <el-menu-item index="/Hacromap">Barriers to implementing</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="5">
        <template #title>Project and Team Information</template>
        <el-menu-item index="/Hacromap">Team Member Information </el-menu-item>
        <el-menu-item index="/Hacromap">Project Structure</el-menu-item>
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
