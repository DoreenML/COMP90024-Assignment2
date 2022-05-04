<template>
  <el-image :src="require('@/assets/group.jpg')" fit="contain"
  style="width: 50%; height: 15%"></el-image>
  <figure class='highcharts-figure'>
    <div id='container'></div>
    <p class="highcharts-description">
        <b>Team Member Information </b>
        <b>(names in alphbetical order)</b>
    </p>
    <table id="datatable">
        <thead>
            <tr>
                <th>Name</th>
                <th>Student ID</th>
                <th>Email</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Qi Li</th>
                <td>ID</td>
                <td>Email</td>
            </tr>
            <tr>
                <th>Xiaohan Ma</th>
                <td>1145763</td>
                <td>mxm3@student.unimelb.edu.au</td>
            </tr>
            <tr>
                <th>Yuheng Guo</th>
                <td>1113036</td>
                <td>yuhengg1@student.unimelb.edu.au</td>
            </tr>
            <tr>
                <th>Zhangyu Wei</th>
                <td>1258372</td>
                <td>zhangyuw@student.unimelb.edu.au</td>
            </tr>
            <tr>
                <th>Zhaoyang Zhang</th>
                <td>1240942</td>
                <td>zhaoyangz1@student.unimelb.edu.au</td>
            </tr>
        </tbody>
    </table>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  methods: {
    displayHighCharts() {
      Highcharts.chart('container', {
        data: {
          table: 'datatable',
        },
      });
    },
  },
};
</script>
<style scoped>
.highcharts-data-table table {
  min-width: 310px;
  max-width: 800px;
  margin: 1em auto;
}

#datatable {
    font-family: Verdana, sans-serif;
    border-collapse: collapse;
    border: 1px solid #ebebeb;
    margin: 10px auto;
    text-align: center;
    width: 100%;
    max-width: 2000px;
}

#datatable caption {
    padding: 1em 0;
    font-size: 1.2em;
    color: #555;
}

#datatable th {
    font-weight: 600;
    padding: 0.5em;
}

#datatable td,
#datatable th,
#datatable caption {
    padding: 0.5em;
}

#datatable thead tr,
#datatable tr:nth-child(even) {
    background: #f8f8f8;
}

#datatable tr:hover {
    background: #f1f7ff;
}

</style>
