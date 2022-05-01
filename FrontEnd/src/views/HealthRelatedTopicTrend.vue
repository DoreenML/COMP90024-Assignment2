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
          text: 'COVID-19 Related Topic Trend',
        },
        subtitle: {
          text: 'Plot 1-1 Key words for COVID-19 that appears frequently for the top 4 area',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'vomiting',
            'burn',
            'chill',
            'fever',
            'pimples',
            'fractured',
            'toothache',
            'headache',
            'tumor',
            'mood',
          ],
          crosshair: true,
        },
        yAxis: {
          title: {
            text: 'Number of tweets',
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
              format: '{point.y:1f}',
            },
          },
        },
        tooltip: {
          headerFormat: "<span style='font-size:11px'>{series.name}</span><br>",
          pointFormat:
            "<span style='color:{point.color}'>{point.name}</span>: <b>{point.y:1f}</b><br/>",
        },
        series: [
          {
            name: 'area-1',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 12.74,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 20.57,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 27.23,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 77.23,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 17.23,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 17.23,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 17.23,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 17.23,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 17.23,
                drilldown: 'mood',
              },
            ],
          },
          {
            name: 'area-2',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 8,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 6,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 43,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 9,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 7,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 17.23,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 14,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 2,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 19,
                drilldown: 'mood',
              },
            ],
          },
          {
            name: 'area-3',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 45,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 76,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 12,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 91,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 34,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 56,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 18,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 82,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 79,
                drilldown: 'mood',
              },
            ],
          },
            {
            name: 'area-4',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 96,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 43,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 65,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 37,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 22,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 17.23,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 81,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 65,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 44,
                drilldown: 'mood',
              },
            ],
          }, {
            name: 'area-5',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 47,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 56,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 93,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 3,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 16,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 68,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 12,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 56,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 77,
                drilldown: 'mood',
              },
            ],
          }, {
            name: 'area-6',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 23,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 42,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 66,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 54,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 82,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 69,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 23,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 64,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 21,
                drilldown: 'mood',
              },
            ],
          },{
            name: 'area-7',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 23,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 47,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 12,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 91,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 36,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 87,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 12,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 84,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 91,
                drilldown: 'mood',
              },
            ],
          },
          {
            name: 'area-8',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 19,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 57,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 23,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 31,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 57,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 23,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 11,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 6,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 3,
                drilldown: 'mood',
              },
            ],
          },{
            name: 'area-9',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 65,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 14,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 82,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 32,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 67,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 51,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 49,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 82,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 13,
                drilldown: 'mood',
              },
            ],
          },
          {
            name: 'area-10',
            colorByPoint: false,
            data: [
              {
                name: 'vomiting',
                y: 71,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: 15,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: 82,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: 17,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: 31,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: 82,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: 91,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: 44,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: 57,
                drilldown: 'mood',
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
