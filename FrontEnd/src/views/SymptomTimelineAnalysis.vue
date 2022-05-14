<template>
  <figure class='highcharts-figure'>
    <div id='container'></div>
    <div id='container2'></div>
  </figure>
  <div class="spacer"></div>
</template>

<script>
import Highcharts from 'highcharts';
// import { GetMentalTimeline} from '../api/api';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  mounted() {
    // GetMentalTimeline().then((response) => {
    //   console.log(response)
    //   this.mental =response.data.mental;
    //   this.displayHighCharts();
    // })
    this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
      // const _this = this;
      Highcharts.chart('container', {
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
        },
        title: {
            text: 'Number of Months Since the Outbreak',
        },
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

    series: [{name: 'auspol', data: [3690, 32417, 35120, 62434, 228056, 72306, 695554]}, 
    {name: 'Australia', data: [2531, 4512, 2056, 11497, 54077, 472, 1668]}, 
    {name: 'PokemonGO', data: [4204, 1096, 1577, 106, 4982, 1499, 6110]}, 
    {name: 'COVID19', data: [3338767, 101118, 52636, 89719, 115309, 302063, 123423]}, 
    {name: 'OnThisDay', data: [5823, 306, 211, 5116, 566, 281, 30710]}, 
    {name: 'MedTwitter', data: [55836, 1621, 351, 1351, 5150, 7268, 3897]}, 
    {name: 'BREAKING', data: [9633, 728, 24725, 20419, 26095, 20573, 53830]}],

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
  height: 600px;
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
