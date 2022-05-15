<template>
  <figure class='highcharts-figure'>
    <div id="sis_games" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
import { GetSentimentWave} from '../api/api';
import $ from 'jquery';
export default {
  data() {
    return {
        stacks: ['wave_1', 'wave_2'],
        stackLabels: [],
        chart: ''
    };
  },
  mounted() {
    GetSentimentWave().then((response) => {
      console.log(response)
      this.w_1 =response.data.w_1;
      this.w_4 =response.data.w_4;
      this.displayHighCharts();
    })
    // this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
        const _this = this;
        Highcharts.chart('sis_games', {
            chart: {
                type: 'column',
                events: {
                    redraw: _this.renderStackLabels,
                    load: function() {
                        const chart = this;
                        console.log(chart);
                    },
                }
            },
            title: {
                text: 'Sentiment and Subjectivity of Wave-1 and Wave-4 for the Top-4 Area'
            },
            legend: {
                align: 'right',
                verticalAlign: 'middle',
                width: 300,
                itemWidth: 100,
                itemMarginBottom: 30
            },
            plotOptions: {
                column: {
                stacking: 'normal'
                }
            },
            xAxis: {
                categories: ['Somerton', 'Beaumaris', 'Southbank', 'Thornbury']
            },
            yAxis: {
                labels: {
                    formatter: function () {
                        return Math.abs(this.value);
                    }
                },
                plotLines: [{
                    value: 0,
                    width: 2,
                    color: 'black'
                }],
                title: {
                    text: 'Numerical Value'
                }
            },
            tooltip: {
                formatter: function() {
                    let stackName = this.series.userOptions.stack;
                    return ''+ this.x +':<br/>'+'<b>'+ this.series.name +'</b>: ' + Math.abs(this.y);
                }
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'w1_n/o',
                type: 'column',
                color: 'rgba(195,195,194,0.8)',
                data: _this.w_1._0,
                stack: _this.stacks[0]
            }, {
                name: 'w1_n/s',
                type: 'column',
                color: 'rgba(64,109,214,0.8)',
                data: _this.w_1._1,
                stack: _this.stacks[0]
            }, {
                name: 'w1_p/o',
                type: 'column',
                color: 'rgba(29,218,94,0.8)',
                data: _this.w_1._2,
                stack: _this.stacks[0]
            },{
                name: 'w1_p/s',
                type: 'column',
                color: 'rgba(255,0,19,0.8)',
                data: _this.w_1._3,
                stack: _this.stacks[0]
            }, {
                name: 'w1_rate',
                type: 'spline',
                data: [23, 41, 48, 46],
                stack: _this.stacks[0]
            },{
                name: 'w4_n/o',
                type: 'column',
                color: 'rgba(123,124,118,0.8)',
                data: _this.w_4._0,
                stack: _this.stacks[1]
            }, {
                name: 'w4_n/s',
                type: 'column',
                color: 'rgba(1,3,165,0.8)',
                data: _this.w_4._1,
                stack: _this.stacks[1]
            }, {
                name: 'w4_p/o',
                type: 'column',
                color: 'rgba(10,135,53,0.8)',
                data: _this.w_4._2,
                stack: _this.stacks[1]
            },{
                name: 'w4_p/s',
                type: 'column',
                color: 'rgba(164,7,18,0.8)',
                data: _this.w_4._3,
                stack: _this.stacks[1]
            }, {
                name: 'w4_rate',
                type: 'spline',
                data: [23, 41, 48, 46],
                stack: _this.stacks[1]
            }]
        });
    },
    renderText() {
        const chart = this;
        console.log(chart);  
    },
    renderStackLabels() {
        const _this = this;
        _this.stackLabels.forEach((label) => label.destroy());
        _this.stackLabels = [];

        // legend position
        var legendMatrix = $(".highcharts-legend")[0].transform.baseVal[0].matrix;

        $(".highcharts-legend-item.highcharts-column-series, .highcharts-legend-item.highcharts-spline-series").toArray().forEach(function(item, i) {
            if (i % 5 === 0) {
                var itemMatrix = item.transform.baseVal[0].matrix; // legend item position
                _this.stackLabels.push(_this.chart.renderer.text(_this.stacks[i / 5] + ':', itemMatrix.e + legendMatrix.e, itemMatrix.f + legendMatrix.f - 5));
            };
        });
        
        _this.stackLabels.forEach((label) => label.add());
    }
}
}
</script> 
