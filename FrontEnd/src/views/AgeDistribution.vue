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
        stacks: ['vacataion', 'home', 'work'],
        stackLabels: []
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
                    redraw: _this.renderStackLabels
                }
            },
            title: {
                text: 'New vs Solves'
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
                categories: ['06/27/2017 Tuesday', '06/28/2017 Wednesday', '06/29/2017 Thursday', '06/30/2017 Friday', '07/01/2017 Saturday', '07/02/2017 Sunday', '07/03/2017 Monday', '07/04/2017 Tuesday', '07/05/2017 Wednesday', '07/06/2017 Thursday', '07/07/2017 Friday', '07/08/2017 Saturday', '07/09/2017 Sunday', '07/10/2017 Monday', '07/11/2017 Tuesday']
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'seconds',
                type: 'column',
                data: [149, 3825, 7025, 6083, 4696, 3033, 4137, 4105, 3301, 3382, 3829, 3765, 2427, 2440, 3186],
                stack: _this.stacks[0]
            }, {
                name: 'streets',
                type: 'column',
                data: [-149, -3589, -6516, -5591, -4172, -2770, -3896, -3757, -3255, -2864, -3689, -3767, -2634, -2874, -3568],
                stack: _this.stacks[0]
            }, {
                name: 'sis',
                type: 'spline',
                data: [0, 236, 509, 492, 524, 263, 241, 348, 46, 518, 140, -2, -207, -434, -382],
                stack: _this.stacks[0]
            }, {
                name: 'seconds',
                type: 'column',
                data: [3488, 3665, 3706, 3155, 2837, 2682, 2920, 3048, 2781, 2843, 2914, 2956, 2625, 3231, 2536],
                stack: _this.stacks[1]
            }, {
                name: 'streets',
                type: 'column',
                data: [-4039, -4098, -3869, -4916, -4405, -3213, -3181, -3264, -3528, -2465, -3363, -4056, -2907, -3338, -3241],
                stack: _this.stacks[1]
            }, {
                name: 'sis',
                type: 'spline',
                data: [-551, -433, -163, -1761, -1568, -531, -261, -216, -747, 378, -449, -1100, -282, -107, -705],
                stack: _this.stacks[1]
            }, {
                name: 'seconds',
                type: 'column',
                data: [4911, 5101, 4708, 3701, 3033, 2473, 2701, 2932, 2522, 2615, 3539, 2837, 2960, 2290, 2176],
                stack: _this.stacks[2]
            }, {
                name: 'streets',
                type: 'column',
                data: [-4806, -4337, -3851, -3761, -3816, -3064, -2787, -3558, -2905, -1972, -3168, -4077, -2680, -3209, -2818],
                stack: _this.stacks[2]
            }, {
                name: 'sis',
                type: 'spline',
                data: [105, 764, 857, -60, -783, -591, -86, -626, -383, 643, 371, -1240, 280, -919, -642],
                stack: _this.stacks[2]
            }]
        });
    },
    renderStackLabels() {
        stackLabels.forEach((label) => label.destroy());
        stackLabels = [];
        // legend position
        var legendMatrix = $(".highcharts-legend")[0].transform.baseVal[0].matrix;
        $(".highcharts-legend-item.highcharts-column-series, .highcharts-legend-item.highcharts-spline-series").toArray().forEach(function(item, i) {
            if (i % 3 === 0) {
                var itemMatrix = item.transform.baseVal[0].matrix; // legend item position
                stackLabels.push(chart.renderer.text(_this.stacks[i / 3] + ':', itemMatrix.e + legendMatrix.e, itemMatrix.f + legendMatrix.f - 5));
            };
        });
        
        stackLabels.forEach((label) => label.add());
    }
}
}
</script> 