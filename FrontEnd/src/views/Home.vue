<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
<template>
  <div class="home">
    <el-carousel direction="horizontal"
    autoplay="true"
    arrow="never"
    interval="3000"
    loop="true">
      <el-carousel-item>
        <how-to-use-page></how-to-use-page>
      </el-carousel-item>
      <el-carousel-item>
        <how-to-cite></how-to-cite>
      </el-carousel-item>
      <el-carousel-item>
        <survey-info></survey-info>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
// @ is an alias to /src
import SurveyInfo from '@/components/homepage/SurveyInfo.vue';
import HowToUsePage from '@/components/homepage/HowToUsePage.vue';
import HowToCite from '@/components/homepage/HowToCite.vue';

export default {
  name: 'Home',
  components: {
    SurveyInfo,
    HowToUsePage,
    HowToCite,
  },
  setup() {
    const imgArr = ['@/assets/logo.png'];
    return {
      imgArr,
    };
  },
};
</script>

<style scoped>
.home{
  height: 100%;
}
.el-carousel__item {
  height: 100%;
  background-color: #99a9bf;
}

/deep/ .el-carousel {
  height: 100%;
}
/deep/ .el-carousel__container {
  height: 100%;
}
/deep/ .el-carousel__button {
  background-color: blue;
}
</style>
