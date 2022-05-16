<template>
  <figure class='highcharts-figure'>
    <div id='container1'></div>
    <div id='container2'></div>
  </figure>
  <div class="spacer"></div>
</template>

<script>
import Highcharts from 'highcharts';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  mounted() {
    this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
      Highcharts.chart('container1', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Utilisation by treatment site',
        },
        subtitle: {
          text: 'Plot 3-6: Dynamic bar graph for each treatment site (Vertical = % MM-users, fields = ITV, BHG, FBG, TT)',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'ITV',
            'BHG',
            'FBG',
            'MidV',
            'TT',
          ],
          crosshair: true,
        },
        yAxis: {
          title: {
            text: '% MM-users',
          },
        },
        legend: {
          enabled: true,
        },
        plotOptions: {
          series: {
            borderWidth: 0,
            dataLabels: {
              enabled: true,
              format: '{point.y:.1f}%',
            },
          },
        },
        tooltip: {
          headerFormat: "<span style='font-size:11px'>{series.name}</span><br>",
          pointFormat:
            "<span style='color:{point.color}'>{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>",
        },
        series: [
          {
            name: 'Total',
            colorByPoint: false,
            data: [
              {
                name: 'ITV',
                y: 12.74,
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: 20.57,
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: 27.23,
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: 77.23,
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: 17.23,
                drilldown: 'TT',
              },
            ],
          },
          {
            name: 'SABR',
            colorByPoint: false,
            data: [
              {
                name: 'ITV',
                y: 62.74,
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: 70.57,
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: 27.23,
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: 37.23,
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: 76.23,
                drilldown: 'TT',
              },
            ],
          },
          {
            name: 'Conventional',
            colorByPoint: false,
            data: [
              {
                name: 'ITV',
                y: 62.74,
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: 20.57,
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: 50.23,
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: 35.23,
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: 9.23,
                drilldown: 'TT',
              },
            ],
          },
        ],
      });
      Highcharts.chart('container2', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Plot 2: Static pie charts – combinations of utilisation',
        },
        subtitle: {
          text: '',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'ITV',
            'BHG',
            'FBG',
            'MidV',
            'TT',
          ],
          crosshair: true,
        },
        yAxis: {
          title: {
            text: 'Percentage of Motion Management Users',
          },
        },
        legend: {
          enabled: true,
        },
        plotOptions: {
          series: {
            borderWidth: 0,
            dataLabels: {
              enabled: true,
              format: '{point.y:.1f}%',
            },
          },
        },
        tooltip: {
          headerFormat: "<span style='font-size:11px'>{series.name}</span><br>",
          pointFormat:
            "<span style='color:{point.color}'>{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>",
        },
        series: [
          {
            type: 'pie',
            name: 'combination',
            data: [{
              name: 'Total',
              y: 13,
              color: 'rgba(0,0,0,0.7)',
            }, {
              name: 'SABR',
              y: 25,
              color: 'rgba(137,196,244,1)',
            }, {
              name: 'Con',
              y: 25,
              color: 'rgba(0,230,64,.7)',
            }],
            center: [190, 60],
            size: 130,
            showInLegend: false,
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            },
          },
          {
            type: 'pie',
            name: 'combination',
            data: [{
              name: 'Total',
              y: 13,
              color: 'rgba(0,0,0,0.7)',
            }, {
              name: 'SABR',
              y: 25,
              color: 'rgba(137,196,244,1)',
            }, {
              name: 'Con',
              y: 25,
              color: 'rgba(0,230,64,.7)',
            }],
            center: [490, 60],
            size: 130,
            showInLegend: false,
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            },
          }],
      });
    },
  },
};
</script>
<style scoped>
.highcharts-figure,
.highcharts-data-table table {
  min-width: 310px;
  max-width: 800px;
  margin: 1em auto;
}

#container {
  height: 400px;
}

.spacer {
    height: 20px;
}

.highcharts-data-table table {
  font-family: Verdana, sans-serif;
  border-collapse: collapse;
  border: 1px solid #ebebeb;
  margin: 10px auto;
  text-align: center;
  width: 100%;
  max-width: 500px;
}

.highcharts-data-table caption {
  padding: 1em 0;
  font-size: 1.2em;
  color: #555;
}

.highcharts-data-table th {
  font-weight: 600;
  padding: 0.5em;
}

.highcharts-data-table td,
.highcharts-data-table th,
.highcharts-data-table caption {
  padding: 0.5em;
}

.highcharts-data-table thead tr,
.highcharts-data-table tr:nth-child(even) {
  background: #f8f8f8;
}

.highcharts-data-table tr:hover {
  background: #f1f7ff;
}

</style>
