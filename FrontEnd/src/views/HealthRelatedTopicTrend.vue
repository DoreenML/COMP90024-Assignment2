<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
<template>
  <figure class='highcharts-figure'>
    <div id='container1'></div>
    <div id='container2'></div>
  </figure>
  <div class="spacer"></div>
</template>

<script>
import Highcharts from 'highcharts';
import { GetHealthRelatedTopicTrend} from '../api/api';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  data()
 {
   return {
     title: '',
     num_:null,
   }
 },
   mounted() {
    GetHealthRelatedTopicTrend().then((response) => {
      console.log(response)
      this.title =response.data.greeting;
      this.area_1 = response.data.area_1;
      this.area_2 = response.data.area_2;
      this.area_3 = response.data.area_3;
      this.displayHighCharts();
    })
  },
  methods: {
    displayHighCharts() {
      const _this = this;
      Highcharts.chart('container1', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 symptom and Area Analysis",
        },
        subtitle: {
          text: 'Plot 1-2 Key words for COVID-19 that appears frequently for the top 10 area',
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
                y: _this.area_1.vomiting,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: _this.area_1.burn,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: _this.area_1.chill,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: _this.area_1.fever,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: _this.area_1.pimples,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: _this.area_1.fractured,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: _this.area_1.toothache,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: _this.area_1.tumor,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: _this.area_1.mood,
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
                y: _this.area_2.vomiting,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: _this.area_2.burn,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: _this.area_2.chill,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: _this.area_2.fever,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: _this.area_2.pimples,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: _this.area_2.fractured,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y:  _this.area_2.toothache,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y:  _this.area_2.tumor,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y:  _this.area_2.mood,
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
                y: _this.area_3.vomiting,
                drilldown: 'vomiting',
              },
              {
                name: 'burn',
                y: _this.area_3.burn,
                drilldown: 'burn',
              },
              {
                name: 'chill',
                y: _this.area_3.chill,
                drilldown: 'chill',
              },
              {
                name: 'fever',
                y: _this.area_3.fever,
                drilldown: 'fever',
              },
              {
                name: 'pimples',
                y: _this.area_3.pimples,
                drilldown: 'pimples',
              },
              {
                name: 'fractured',
                y: _this.area_3.fractured,
                drilldown: 'fractured',
              },
              {
                name: 'toothache',
                y: _this.area_3.toothache,
                drilldown: 'toothache',
              },
              {
                name: 'tumor',
                y: _this.area_3.tumor,
                drilldown: 'tumor',
              },
              {
                name: 'mood',
                y: _this.area_3.mood,
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
          text: 'Plot 2: Area Percentage & Symptom Percentage',
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
            'area-1',
            'area-2',
            'area-3',
            'area-4',
            'area-5',
            'area-6',
            'area-7',
            'area-8',
            'area-9',
            'area-10',
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
            name: 'Area percentage',
            data: [{
              name: 'area-1',
              y: 13,
            }, {
              name: 'area-2',
              y: 12,
            }, {
              name: 'area-3',
              y: 33,
            },{
              name: 'area-4',
              y: 42,
            },{
              name: 'area-5',
              y: 11,
            },{
              name: 'area-6',
              y: 23,
            },{
              name: 'area-7',
              y: 42,
            },{
              name: 'area-8',
              y: 71,
            },{
              name: 'area-9',
              y: 21,
            },{
              name: 'area-10',
              y: 11,
            }],
            center: [190, 60],
            size: 130,
            showInLegend: false,
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f}%',
            },
          },
          {
            type: 'pie',
            name: 'Symptom Percentage',
            data: [{
              name: 'vomiting',
              y: 13,
            }, {
              name: 'burn',
              y: 12,
            }, {
              name: 'chill',
              y: 33,
            },{
              name: 'fever',
              y: 42,
            },{
              name: 'pimples',
              y: 11,
            },{
              name: 'fractured',
              y: 23,
            },{
              name: 'toothache',
              y: 42,
            },{
              name: 'headache',
              y: 71,
            },{
              name: 'turmor',
              y: 21,
            }],
            center: [590, 60],
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
