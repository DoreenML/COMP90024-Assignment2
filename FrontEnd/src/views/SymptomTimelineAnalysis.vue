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
      title: {
        text: 'Symptom Key Word Timeline Analysis'
    },

    subtitle: {
        text: 'y-axis shows the totoal numebr of mentions, x-axis shows the time line.'
    },

    yAxis: {
        title: {
            text: 'Number of Appearance for Each Symptom Word'
        }
    },

    xAxis: {
        accessibility: {
            rangeDescription: 'Range: 2010 to 2020'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 1
        }
    },
    tooltip: {
    headerFormat: "<span style='font-size:11px'>{series.name}</span><br>",
    pointFormat:
    "<span style='color:{point.color}'>{point.name}</span>: <b>{point.y:1f}</b><br/>",
    },

    series: [{
        name: 'vomiting',
        data: [10234, 23451, 26734, 12345, 19862, 19931, 37133, 54175]
    }, {
        name: 'burn',
        data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        name: 'chill',
        data: [31744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        name: 'fever',
        data: [2632, 6245, 1988, 2169, 5112, 2452, 4400, 4227]
    }, {
        name: 'pimples',
        data: [12908, 2948, 3105, 41248, 7989, 61816, 58274, 48111]
    }, {
        name: 'fractured',
        data: [9290, 8948, 7105, 61248, 5989, 41816, 38274, 28111]
    },{
        name: 'toothache',
        data: [7290, 4948, 1105, 2124, 3989, 9181, 7827, 18111]
    },{
        name: 'headache',
        data: [12908, 2948, 3105, 51248, 7989, 91816, 28274, 78111]
    },{
        name: 'turmor',
        data: [32908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
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
