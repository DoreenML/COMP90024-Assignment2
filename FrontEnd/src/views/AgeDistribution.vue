<template>
  <figure class='highcharts-figure'>
    <div id="sis_games" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
import $ from 'jquery';
export default {
  data() {
    return {
        stacks: ['area-1', 'area-2', 'area-3', 'area-4', 'area-5'],
        stackLabels: [],
        chart: ''
    };
  },
  mounted() {
    this.displayHighCharts();
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
                        chart.renderer.text("Average Age", chart.chartWidth/3 + 30, chart.chartHeight/6)
                            .css({
                                color: 'black',
                                fontSize: '16px'
                            })
                            .add();
                        chart.renderer.text("Population/Cases (in k)", chart.chartWidth/3, chart.chartHeight- 70)
                            .css({
                                color: 'black',
                                fontSize: '16px'
                            })
                            .add()
                        chart.renderer.text("area-1:", chart.chartWidth-310, chart.chartHeight-320)
                            .css({
                                color: 'black',
                                fontSize: '14px'
                            })
                            .add()
                        chart.renderer.text("area-2:", chart.chartWidth-310, chart.chartHeight-275)
                            .css({
                                color: 'black',
                                fontSize: '14px'
                            })
                            .add()
                        chart.renderer.text("area-3:", chart.chartWidth-310, chart.chartHeight-230)
                            .css({
                                color: 'black',
                                fontSize: '14px'
                            })
                            .add()
                        chart.renderer.text("area-4:", chart.chartWidth-310, chart.chartHeight-185)
                            .css({
                                color: 'black',
                                fontSize: '14px'
                            })
                            .add()
                        chart.renderer.text("area-5:", chart.chartWidth-310, chart.chartHeight-140)
                            .css({
                                color: 'black',
                                fontSize: '14px'
                            })
                            .add()
                    },
                }
            },
            title: {
                text: 'COVID-19 Cases in Polulation through Time for the Top-5 Area'
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
                categories: ['1-month', '2-month', '3-month', '4-month', '5-month', '6-month', '7-month', '8-month', '9-month', '10-month', '11-month', '12-month']
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
                    return ''+ this.x +':<br/>'
                            + '<b>Area Name</b>: ' + stackName + '<br/>'
                            +'<b>'+ this.series.name +'</b>: ' + Math.abs(this.y);
                }
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Age',
                type: 'column',
                color: 'rgba(223, 83, 83, .5)',
                data: [46, 30, 41, 23, 49, 25, 70, 60, 33, 82, 60, 46],
                stack: _this.stacks[0]
            }, {
                name: 'People',
                type: 'column',
                color: 'rgba(223, 83, 83, .5)',
                data: [-41, -27, -38, -57, -14, -39, -65, -55, -32, -41, -27],
                stack: _this.stacks[0]
            }, {
                name: 'Cases',
                type: 'spline',
                color: 'rgba(223, 83, 83, .5)',
                data: [-23, -41, -48, -46, -18, -23, -26, -59, -49, -54, -49, -54],
                stack: _this.stacks[0]
            },{
                name: 'Age',
                type: 'column',
                data: [49, 25, 70, 60, 46, 30, 41, 23, 33, 82, 60, 46],
                stack: _this.stacks[1]
            }, {
                name: 'People',
                type: 'column',
                data: [-14, -39, -65, -55, -41, -27, -38, -57, -32, -41, -27],
                stack: _this.stacks[1]
            }, {
                name: 'Cases',
                type: 'spline',
                data: [-23, -26, -59, -49, -54, -23, -41, -48, -46, -18, -49, -54],
                stack: _this.stacks[1]
            }, {
                name: 'Age',
                type: 'column',
                data: [88, 65, 36, 55, 28, 82, 20, 48, 81, 28, 36, 55],
                stack: _this.stacks[2]
            }, {
                name: 'People',
                type: 'column',
                data: [-40, -98, -38, -16, -45, -13, -31, -34, -28, -19, -98, -38],
                stack: _this.stacks[2]
            }, {
                name: 'Cases',
                type: 'spline',
                data: [-51, -33, -16, -17, -68, -53, -21, -16, -74, -78, -33, -16],
                stack: _this.stacks[2]
            }, {
                name: 'Age',
                type: 'column',
                data: [11, 10, 48, 37, 33, 23, 27, 29, 22, 15, 10, 48],
                stack: _this.stacks[3]
            }, {
                name: 'People',
                type: 'column',
                data: [-46, -43, -38, -61, -16, -30, -27, -58, -25, -72, -43, -38],
                stack: _this.stacks[3]
            }, {
                name: 'Cases',
                type: 'spline',
                data: [-15, -76, -87, -60, -78, -51, -86, -26, -33, -63, -87, -60],
                stack: _this.stacks[3]
            },{
                name: 'Age',
                type: 'column',
                data: [23, 27, 29, 22, 11, 10, 48, 37, 33, 15, 10, 48],
                stack: _this.stacks[4]
            }, {
                name: 'People',
                type: 'column',
                data: [-16, -30, -27, -58, -25, -46, -43, -38, -61, -72, -43, -38],
                stack: _this.stacks[4]
            }, {
                name: 'Cases',
                type: 'spline',
                data: [-51, -86, -26, -33, -63, -15, -76, -87, -60, -78, -87, -60],
                stack: _this.stacks[4]
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
            if (i % 4 === 0) {
                var itemMatrix = item.transform.baseVal[0].matrix; // legend item position
                _this.stackLabels.push(_this.chart.renderer.text(_this.stacks[i / 4] + ':', itemMatrix.e + legendMatrix.e, itemMatrix.f + legendMatrix.f - 5));
            };
        });
        
        _this.stackLabels.forEach((label) => label.add());
    }
}
}
</script> 