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
        text: 'Sentiment and Subjectivity: The Corelation between Symptom and Depression'
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
                radius: 5,
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
        color: 'rgba(223, 83, 83, .5)',
        data: _this.low

    }, {
        name: 'High Influence',
        color: 'rgba(119, 152, 191, .5)',
        data: _this.high
    }]
    });
    Highcharts.chart('container2', {
        chart: {
          type: 'column',
        },
        title: {
          text: "COVID-19 First Wave Topic",
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
                y: 1499108,
                drilldown: 'coronavirus',
              },
              {
                name: 'covid19',
                y: 478149,
                drilldown: 'covid19',
              },
              {
                name: 'respect',
                y: 299290,
                drilldown: 'respect',
              },
              {
                name: 'COVID19',
                y: 273256,
                drilldown: 'COVID19',
              },
              {
                name: 'BlackLivesMatter',
                y: 193480,
                drilldown: 'BlackLivesMatter',
              },
              {
                name: 'AbolishICE',
                y: 193480,
                drilldown: 'AbolishICE',
              },
              {
                name: 'COVID19Aus',
                y: 91315,
                drilldown: 'COVID19Aus',
              },
              {
                name: 'COVID',
                y: 80478,
                drilldown: 'COVID',
              },
              {
                name: 'FinalFantasy',
                y: 78880,
                drilldown: 'FinalFantasy',
              },
              {
                name: 'medtwitter',
                y: 54687,
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
          text: "COVID-19 Second Wave Topic",
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
                y: 1465705,
                drilldown: '10YearsOf1D',
              },
              {
                name: 'EndSARS',
                y: 617975,
                drilldown: 'EndSARS',
              },
              {
                name: 'TrumpIsNotWell',
                y: 508395,
                drilldown: 'TrumpIsNotWell',
              },
              {
                name: 'WhatsHappeninginThailand',
                y: 337720,
                drilldown: 'WhatsHappeninginThailand',
              },
              {
                name: 'EndSWAT',
                y: 238320,
                drilldown: 'EndSWAT',
              },
              {
                name: 'NewPokemonSnap',
                y: 204560,
                drilldown: 'NewPokemonSnap',
              },
              {
                name: 'PokemonSnapIsBack',
                y: 204230,
                drilldown: 'PokemonSnapIsBack',
              },
              {
                name: 'NintendoSwitch',
                y: 197457,
                drilldown: 'NintendoSwitch',
              },
              {
                name: 'DemocratsStandTall',
                y: 169600,
                drilldown: 'DemocratsStandTall',
              },
              {
                name: 'COVID19',
                y: 158375,
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
          text: "COVID-19 Third Wave Topic",
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
                y: 3747280,
                drilldown: 'BTS',
              },
              {
                name: 'PHI',
                y: 1696185,
                drilldown: 'PHI',
              },
              {
                name: 'Gold',
                y: 1681301,
                drilldown: 'Gold',
              },
              {
                name: '11YearsOfOneDirection',
                y: 1345710,
                drilldown: '11YearsOfOneDirection',
              },
              {
                name: 'LateLateShow',
                y: 823670,
                drilldown: 'LateLateShow',
              },
              {
                name: 'ESCAPE2021',
                y: 500110,
                drilldown: 'ESCAPE2021',
              },
              {
                name: 'mobpsycho100',
                y: 423230,
                drilldown: 'mobpsycho100',
              },
              {
                name: 'Solchicks',
                y: 339445,
                drilldown: 'Solchicks',
              },
              {
                name: 'SEVENTEEN',
                y: 201490,
                drilldown: 'SEVENTEEN',
              },
              {
                name: 'ReturnToHogwarts',
                y: 194035,
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
          text: "COVID-19 Fourth Wave Topic",
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
                y: 2205335,
                drilldown: 'Oscars',
              },
              {
                name: 'SEVENTEEN',
                y: 1799435,
                drilldown: 'SEVENTEEN',
              },
              {
                name: 'TIME100Companies',
                y: 1272200,
                drilldown: 'TIME100Companies',
              },
              {
                name: 'DoctorStrange',
                y: 1035780,
                drilldown: 'DoctorStrange',
              },
              {
                name: 'MINGYU',
                y: 882610,
                drilldown: 'MINGYU',
              },
              {
                name: 'JOSHUA',
                y: 714680,
                drilldown: 'JOSHUA',
              },
              {
                name: 'DINO',
                y: 693805,
                drilldown: 'DINO',
              },
              {
                name: 'JUN',
                y: 690750,
                drilldown: 'JUN',
              },
              {
                name: 'WOODZ',
                y: 680140,
                drilldown: 'WOODZ',
              },
              {
                name: 'JEONGHAN',
                y: 658520,
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
