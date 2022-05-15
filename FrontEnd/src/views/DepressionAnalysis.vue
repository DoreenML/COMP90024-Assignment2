<template>
  <figure class='highcharts-figure'>
    <div id='container1'></div>
    <div id='container2'></div>
    <div id='container3'></div>
    <div id='container4'></div>
    <div id='container5'></div>
  </figure>
  <div class="spacer"></div>
</template>

<script>
import Highcharts from 'highcharts';
import { GetDepressChart } from '../api/api';

export default {
  mounted() {
    GetDepressChart().then((response) => {
      console.log(response)
      this.high = response.data.high;
      this.low = response.data.low;
      this.first_wave = response.data.first_wave
      this.second_wave = response.data.second_wave
      this.third_wave = response.data.third_wave
      this.fourth_wave = response.data.fourth_wave
      this.displayHighCharts();
    })
    // this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
    const _this = this
    Highcharts.chart('container1', {
        data: {
          table: 'datatable',
        },
        chart: {
        type: 'scatter',
        zoomType: 'xy'
    },
    title: {
        text: 'Sentiment and Subjectivity: The Corelation between Sentiment and Subjectivity'
    },
    subtitle: {
        text: 'The x-axis is the code for depression. The y-axis is the code for Symptom '
    },
    xAxis: {
        title: {
            enabled: true,
            text: 'Sentiment'
        },
        startOnTick: true,
        endOnTick: true,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Subjectivity'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 100,
        y: 70,
        floating: true,
        backgroundColor: Highcharts.defaultOptions.chart.backgroundColor,
        borderWidth: 1
    },
    plotOptions: {
        scatter: {
            marker: {
                radius: 3,
                states: {
                    hover: {
                        enabled: true,
                        lineColor: 'rgb(100,100,100)'
                    }
                }
            },
            states: {
                hover: {
                    marker: {
                        enabled: false
                    }
                }
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br>',
                pointFormat: '{point.x}, {point.y}'
            }
        }
    },
    series: [{
        name: 'Low Influence',
        color: 'rgba(118, 245, 39, .8)',
        data: _this.low

    }, {
        name: 'High Influence',
        color: 'rgba(223, 83, 83, .8)',
        data: _this.high
    }]
    });
    Highcharts.chart('container2', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 First Wave Hashtag",
        },
        subtitle: {
          text: '# wave 1: 2020-03 to 2020-05',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'coronavirus',
            'covid19',
            'respect',
            'COVID19',
            'BlackLivesMatter',
            'AbolishICE',
            'COVID19Aus',
            'COVID',
            'FinalFantasy',
            'medtwitter'
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
            name: 'Enable',
            colorByPoint: true,
            data: [
              {
                name: 'coronavirus',
                y: _this.first_wave._1,
                drilldown: 'coronavirus',
              },
              {
                name: 'covid19',
                y: _this.first_wave._2,
                drilldown: 'covid19',
              },
              {
                name: 'respect',
                y: _this.first_wave._3,
                drilldown: 'respect',
              },
              {
                name: 'COVID19',
                y: _this.first_wave._4,
                drilldown: 'COVID19',
              },
              {
                name: 'BlackLivesMatter',
                y: _this.first_wave._5,
                drilldown: 'BlackLivesMatter',
              },
              {
                name: 'AbolishICE',
                y: _this.first_wave._6,
                drilldown: 'AbolishICE',
              },
              {
                name: 'COVID19Aus',
                y: _this.first_wave._7,
                drilldown: 'COVID19Aus',
              },
              {
                name: 'COVID',
                y: _this.first_wave._8,
                drilldown: 'COVID',
              },
              {
                name: 'FinalFantasy',
                y: _this.first_wave._9,
                drilldown: 'FinalFantasy',
              },
              {
                name: 'medtwitter',
                y: _this.first_wave._10,
                drilldown: 'medtwitter',
              }
            ],
          },
        ],
      });
      Highcharts.chart('container3', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 Second Wave Hashtag",
        },
        subtitle: {
          text: '# wave 2: 2020-06 to 2020-10',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            '10YearsOf1D',
            'EndSARS',
            'TrumpIsNotWell',
            'WhatsHappeninginThailand',
            'EndSWAT',
            'NewPokemonSnap',
            'PokemonSnapIsBack',
            'NintendoSwitch',
            'DemocratsStandTall',
            'COVID19',
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
            name: 'Enable',
            colorByPoint: true,
            data: [
              {
                name: '10YearsOf1D',
                y: _this.second_wave._1,
                drilldown: '10YearsOf1D',
              },
              {
                name: 'EndSARS',
                y: _this.second_wave._2,
                drilldown: 'EndSARS',
              },
              {
                name: 'TrumpIsNotWell',
                y: _this.second_wave._3,
                drilldown: 'TrumpIsNotWell',
              },
              {
                name: 'WhatsHappeninginThailand',
                y: _this.second_wave._4,
                drilldown: 'WhatsHappeninginThailand',
              },
              {
                name: 'EndSWAT',
                y: _this.second_wave._5,
                drilldown: 'EndSWAT',
              },
              {
                name: 'NewPokemonSnap',
                y: _this.second_wave._6,
                drilldown: 'NewPokemonSnap',
              },
              {
                name: 'PokemonSnapIsBack',
                y: _this.second_wave._7,
                drilldown: 'PokemonSnapIsBack',
              },
              {
                name: 'NintendoSwitch',
                y: _this.second_wave._8,
                drilldown: 'NintendoSwitch',
              },
              {
                name: 'DemocratsStandTall',
                y: _this.second_wave._9,
                drilldown: 'DemocratsStandTall',
              },
              {
                name: 'COVID19',
                y: _this.second_wave._10,
                drilldown: 'COVID19',
              },
            ],
          },
        ],
      });
      Highcharts.chart('container4', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 Third Wave Hashtag",
        },
        subtitle: {
          text: '# wave 3: 2021-07 to 2021-12',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'BTS',
            'PHI',
            'Gold',
            '11YearsOfOneDirection',
            'LateLateShow',
            'ESCAPE2021',
            'mobpsycho100',
            'Solchicks',
            'SEVENTEEN',
            'ReturnToHogwarts'
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
            name: 'Enable',
            colorByPoint: true,
            data: [
              {
                name: 'BTS',
                y: _this.third_wave._1,
                drilldown: 'BTS',
              },
              {
                name: 'PHI',
                y: _this.third_wave._2,
                drilldown: 'PHI',
              },
              {
                name: 'Gold',
                y: _this.third_wave._3,
                drilldown: 'Gold',
              },
              {
                name: '11YearsOfOneDirection',
                y: _this.third_wave._4,
                drilldown: '11YearsOfOneDirection',
              },
              {
                name: 'LateLateShow',
                y: _this.third_wave._5,
                drilldown: 'LateLateShow',
              },
              {
                name: 'ESCAPE2021',
                y: _this.third_wave._6,
                drilldown: 'ESCAPE2021',
              },
              {
                name: 'mobpsycho100',
                y: _this.third_wave._7,
                drilldown: 'mobpsycho100',
              },
              {
                name: 'Solchicks',
                y: _this.third_wave._8,
                drilldown: 'Solchicks',
              },
              {
                name: 'SEVENTEEN',
                y: _this.third_wave._9,
                drilldown: 'SEVENTEEN',
              },
              {
                name: 'ReturnToHogwarts',
                y: _this.third_wave._10,
                drilldown: 'ReturnToHogwarts',
              },
            ],
          },
        ],
      });
      Highcharts.chart('container5', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 Fourth Wave Hashtag",
        },
        subtitle: {
          text: '# wave 4: 2022-01 to present',
        },
        accessibility: {
          announceNewData: {
            enabled: true,
          },
        },
        xAxis: {
          categories: [
            'Oscars',
            'SEVENTEEN',
            'TIME100Companies',
            'DoctorStrange',
            'MINGYU',
            'JOSHUA',
            'DINO',
            'JUN',
            'WOODZ',
            'JEONGHAN',
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
            name: 'Enable',
            colorByPoint: true,
            data: [
              {
                name: 'Oscars',
                y: _this.fourth_wave._1,
                drilldown: 'Oscars',
              },
              {
                name: 'SEVENTEEN',
                y: _this.fourth_wave._2,
                drilldown: 'SEVENTEEN',
              },
              {
                name: 'TIME100Companies',
                y: _this.fourth_wave._3,
                drilldown: 'TIME100Companies',
              },
              {
                name: 'DoctorStrange',
                y: _this.fourth_wave._4,
                drilldown: 'DoctorStrange',
              },
              {
                name: 'MINGYU',
                y: _this.fourth_wave._5,
                drilldown: 'MINGYU',
              },
              {
                name: 'JOSHUA',
                y: _this.fourth_wave._6,
                drilldown: 'JOSHUA',
              },
              {
                name: 'DINO',
                y: _this.fourth_wave._7,
                drilldown: 'DINO',
              },
              {
                name: 'JUN',
                y: _this.fourth_wave._8,
                drilldown: 'JUN',
              },
              {
                name: 'WOODZ',
                y: _this.fourth_wave._9,
                drilldown: 'WOODZ',
              },
              {
                name: 'JEONGHAN',
                y: _this.fourth_wave._10,
                drilldown: 'JEONGHAN',
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
