<template>
  <el-image :src="require('@/assets/group.jpg')" fit="contain"
  style="width: 50%; height: 15%"></el-image>
  <figure class='highcharts-figure'>
    <div id='container'></div>
    <p class="highcharts-description">
        <b>Project Description Table</b>
    </p>
    <table id="datatable">
        <thead>
            <tr>
                <th>Page Name</th>
                <th>Category</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>COVID Cases and Camera Sensor Map</th>
                <td>Map Analysis</td>
                <td>The page shows the COVID cases inside each polygon by the difference of colors and some important camera information.</td>
            </tr>
            <tr>
                <th>Hashtag Timeline Analysis</th>
                <td>Timeline Analysis</td>
                <td>The page shows the top 7 hashtags existing on Twitter for 7 months.</td>
            </tr>
            <tr>
                <th>Sentiment and Subjectivity from Wave-1 to Wave-4</th>
                <td>Sentiment and Subjectivity</td>
                <td>The page shows the top 4 cities' sentiment and subjectivity analysis for 4 waves of COVID-19.</td>
            </tr>
            <tr>
                <th>Correlation and Topic Analysis for Waves</th>
                <td>Correlation Analysis</td>
                <td>The page shows the correlation between sentiment and subjectivity for low and high influence data and the top topics happening for the 4 waves.</td>
            </tr>
            <tr>
                <th>Team Member Information</th>
                <td>Project and Team</td>
                <td>The page shows the team information.</td>
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
