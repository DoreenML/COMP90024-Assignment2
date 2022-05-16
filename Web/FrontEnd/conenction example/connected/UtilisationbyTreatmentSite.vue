<template>
  <figure class='highcharts-figure'>
    <div id='lowerAbdo'></div>
    <div id='other'></div>
    <div id='thorax'></div>
    <div id='upperAbdo'></div>
    <div id='container2'></div>
  </figure>
  <div class="spacer"></div>
</template>

<script>
import Highcharts from 'highcharts';
import { getTreatmentSite } from '../api/api';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  data() {
    return {
      treatmentsites: null
    }
  },
  mounted() {
    getTreatmentSite().then(response => {
        this.treatmentsites = response.data.data;
        console.log(this.treatmentsites);
        this.displayHighCharts();
    });
  },
  methods: {
    displayHighCharts() {
      Highcharts.chart('lowerAbdo', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Lower Abdomen',
        },
        subtitle: {
          text: '<b>Lower Abdomen</b>: Dynamic bar graph for each treatment site (Vertical = % MM-users, fields = ITV, BHG, FBG, TT)',
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
                y: this.treatmentsites.lowerAbdo.series[0].Total[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.lowerAbdo.series[0].Total[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.lowerAbdo.series[0].Total[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.lowerAbdo.series[0].Total[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.lowerAbdo.series[0].Total[4],
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
                y: this.treatmentsites.lowerAbdo.series[1].SABR[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.lowerAbdo.series[1].SABR[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.lowerAbdo.series[1].SABR[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.lowerAbdo.series[1].SABR[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.lowerAbdo.series[1].SABR[4],
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
                y: this.treatmentsites.lowerAbdo.series[2].Conventional[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.lowerAbdo.series[2].Conventional[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.lowerAbdo.series[2].Conventional[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.lowerAbdo.series[2].Conventional[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.lowerAbdo.series[2].Conventional[4],
                drilldown: 'TT',
              },
            ],
          },
        ],
      });

      // OTHER

      Highcharts.chart('other', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Other',
        },
        subtitle: {
          text: '<b>Other</b>: Dynamic bar graph for each treatment site (Vertical = % MM-users, fields = ITV, BHG, FBG, TT)',
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
                y: this.treatmentsites.other.series[0].Total[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.other.series[0].Total[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.other.series[0].Total[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.other.series[0].Total[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.other.series[0].Total[4],
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
                y: this.treatmentsites.other.series[1].SABR[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.other.series[1].SABR[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.other.series[1].SABR[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.other.series[1].SABR[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.other.series[1].SABR[4],
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
                y: this.treatmentsites.other.series[2].Conventional[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.other.series[2].Conventional[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.other.series[2].Conventional[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.other.series[2].Conventional[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.other.series[2].Conventional[4],
                drilldown: 'TT',
              },
            ],
          },
        ],
      });

      // THORAX

      Highcharts.chart('thorax', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Thorax',
        },
        subtitle: {
          text: '<b>Thorax</b>: Dynamic bar graph for each treatment site (Vertical = % MM-users, fields = ITV, BHG, FBG, TT)',
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
                y: this.treatmentsites.thorax.series[0].Total[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.thorax.series[0].Total[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.thorax.series[0].Total[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.thorax.series[0].Total[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.thorax.series[0].Total[4],
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
                y: this.treatmentsites.thorax.series[1].SABR[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.thorax.series[1].SABR[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.thorax.series[1].SABR[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.thorax.series[1].SABR[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.thorax.series[1].SABR[4],
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
                y: this.treatmentsites.thorax.series[2].Conventional[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.thorax.series[2].Conventional[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.thorax.series[2].Conventional[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.thorax.series[2].Conventional[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.thorax.series[2].Conventional[4],
                drilldown: 'TT',
              },
            ],
          },
        ],
      });

      // Upper Abdomen

      Highcharts.chart('upperAbdo', {
        chart: {
          type: 'column',
        },
        title: {
          text: 'Upper Abdomen',
        },
        subtitle: {
          text: '<b>Upper Abdomen</b>: Dynamic bar graph for each treatment site (Vertical = % MM-users, fields = ITV, BHG, FBG, TT)',
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
                y: this.treatmentsites.upperAbdo.series[0].Total[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.upperAbdo.series[0].Total[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.upperAbdo.series[0].Total[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.upperAbdo.series[0].Total[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.upperAbdo.series[0].Total[4],
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
                y: this.treatmentsites.upperAbdo.series[1].SABR[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.upperAbdo.series[1].SABR[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.upperAbdo.series[1].SABR[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.upperAbdo.series[1].SABR[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.upperAbdo.series[1].SABR[4],
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
                y: this.treatmentsites.upperAbdo.series[2].Conventional[0],
                drilldown: 'ITV',
              },
              {
                name: 'BHG',
                y: this.treatmentsites.upperAbdo.series[2].Conventional[1],
                drilldown: 'BHG',
              },
              {
                name: 'FBG',
                y: this.treatmentsites.upperAbdo.series[2].Conventional[2],
                drilldown: 'FBG',
              },
              {
                name: 'MidV',
                y: this.treatmentsites.upperAbdo.series[2].Conventional[3],
                drilldown: 'MidV',
              },
              {
                name: 'TT',
                y: this.treatmentsites.upperAbdo.series[2].Conventional[4],
                drilldown: 'TT',
              },
            ],
          },
        ],
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
