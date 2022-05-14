<template>
  <figure class='highcharts-figure'>
    <div id='container'></div>
    <div id='container2'></div>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
import { GetMentalTimeline} from '../api/api';
// import accessibility from 'highcharts/modules/accessibility';

export default {
  mounted() {
    GetMentalTimeline().then((response) => {
      console.log(response)
      this.mental_0 =response.data.mental._0;
      this.mental_1 =response.data.mental._1;
      this.mental_2 =response.data.mental._2;
      this.mental_3 =response.data.mental._3;
      this.mental_4 =response.data.mental._4;
      this.mental_5 =response.data.mental._5;
      this.mental_6 =response.data.mental._6;
      this.displayHighCharts();
    })
    // this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
      const _this = this;
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

    series: [{name: 'auspol', data: _this.mental_0}, 
    {name: 'Australia', data: _this.mental_1}, 
    {name: 'PokemonGO', data: _this.mental_2}, 
    {name: 'COVID19', data: _this.mental_3}, 
    {name: 'OnThisDay', data: _this.mental_4}, 
    {name: 'MedTwitter', data: _this.mental_5}, 
    {name: 'BREAKING', data: _this.mental_6}],

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
