<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
<template>
  <figure class='highcharts-figure'>
    <div id="sis_games" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
        <p class="highcharts-description">
        <b>Abbreviation and City Introduction </b>
    </p>
    <table id="datatable">
        <thead>
            <tr>
                <th>Abbreviation</th>
                <th>Full Name</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>n/o</th>
                <td>negative and objective</td>
                <td>Collect the COVID with negative and objective tweets</td>
            </tr>
            <tr>
                <th>n/s</th>
                <td>negative and subjective</td>
                <td>Collect the COVID with negative and subjective tweets</td>
            </tr>
            <tr>
                <th>p/o</th>
                <td>positive and objective</td>
                <td>Collect the COVID with positive and objective tweets</td>
            </tr>
            <tr>
                <th>p/s</th>
                <td>positive and subjective</td>
                <td>Collect the COVID with positive and subjective tweets</td>
            </tr>
            <tr>
                <th>Somerton</th>
                <td>suburb city</td>
                <td>Somerton is a seaside suburb of Adelaide in South Australia.</td>
            </tr>
            <tr>
                <th>Beaumaris</th>
                <td>suburb city</td>
                <td>Beaumaris  is located on Port Phillip Bay, which is a suburb of Melbourne, Australia, 20km south-east of Melbourne's central business district.</td>
            </tr>
            <tr>
                <th>Southbank</th>
                <td>suburb city</td>
                <td>Southbank is an inner urban neighbourhood of Melbourne, Victoria, Australia, 1 km south of the Melbourne central business district. Southbank was formerly a mostly industrial area.</td>
            </tr>
            <tr>
                <th>Thornbury</th>
                <td>suburb city</td>
                <td>Thornbury is an inner suburb of Melbourne, Victoria, Australia, 7 km north of Melbourne's Central Business District. Thornbury is universally understood to be a demographic and commercial satellite of Northcote.</td>
            </tr>
        </tbody>
    </table>
  </figure>
</template>

<script>
import Highcharts from 'highcharts';
import { GetSentimentWave} from '../api/api';
import $ from 'jquery';
export default {
  data() {
    return {
        stacks: ['wave_1', 'wave_2', 'wave_3', 'wave_4'],
        stackLabels: [],
        chart: ''
    };
  },
  mounted() {
    GetSentimentWave().then((response) => {
      console.log(response)
      this.w_1 =response.data.w_1;
      this.w_2 =response.data.w_2;
      this.w_3 =response.data.w_3;
      this.w_4 =response.data.w_4;
      this.displayHighCharts();
    })
    // this.displayHighCharts();
  },
  methods: {
    displayHighCharts() {
        const _this = this;
        Highcharts.chart('sis_games', {
            data: {
                table: 'datatable',
            },
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
                text: 'Sentiment and Subjectivity from Wave-1 to Wave-4 for the Top-4 Area'
            },
            subtitle: {
                text: 'Wave 1:2020-03 to 2020-05; Wave 2: 2020-06 to 2020-10; Wave 3: 2021-07 to 2021-12; Wave 4: 2022-01 to now'
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
                color: 'rgba(255,118,208,0.8)',
                data: _this.w_1._0,
                stack: _this.stacks[0]
            }, {
                name: 'w1_n/s',
                type: 'column',
                color: 'rgba(251,39,178,0.8)',
                data: _this.w_1._1,
                stack: _this.stacks[0]
            }, {
                name: 'w1_p/o',
                type: 'column',
                color: 'rgba(204,31,145,0.8)',
                data: _this.w_1._2,
                stack: _this.stacks[0]
            },{
                name: 'w1_p/s',
                type: 'column',
                color: 'rgba(184,29,131,0.8)',
                data: _this.w_1._3,
                stack: _this.stacks[0]
            },{
                name: 'w2_n/o',
                type: 'column',
                color: 'rgba(117,255,248,0.8)',
                data: _this.w_2._0,
                stack: _this.stacks[1]
            }, {
                name: 'w2_n/s',
                type: 'column',
                color: 'rgba(98,210,205,0.8)',
                data: _this.w_2._1,
                stack: _this.stacks[1]
            }, {
                name: 'w2_p/o',
                type: 'column',
                color: 'rgba(80,169,164,0.8)',
                data: _this.w_2._2,
                stack: _this.stacks[1]
            },{
                name: 'w2_p/s',
                type: 'column',
                color: 'rgba(59,129,125,0.8)',
                data: _this.w_2._3,
                stack: _this.stacks[1]
            },{
                name: 'w3_n/o',
                type: 'column',
                color: 'rgba(241,245,117,0.8)',
                data: _this.w_3._0,
                stack: _this.stacks[2]
            }, {
                name: 'w3_n/s',
                type: 'column',
                color: 'rgba(200,203,99,0.8)',
                data: _this.w_3._1,
                stack: _this.stacks[2]
            }, {
                name: 'w3_p/o',
                type: 'column',
                color: 'rgba(158,161,80,0.8)',
                data: _this.w_3._2,
                stack: _this.stacks[2]
            },{
                name: 'w3_p/s',
                type: 'column',
                color: 'rgba(119,120,60,0.8)',
                data: _this.w_3._3,
                stack: _this.stacks[2]
            },{
                name: 'w4_n/o',
                type: 'column',
                color: 'rgba(139,253,188,0.8)',
                data: _this.w_4._0,
                stack: _this.stacks[3]
            }, {
                name: 'w4_n/s',
                type: 'column',
                color: 'rgba(114,206,154,0.8)',
                data: _this.w_4._1,
                stack: _this.stacks[3]
            }, {
                name: 'w4_p/o',
                type: 'column',
                color: 'rgba(92,166,124,0.8)',
                data: _this.w_4._2,
                stack: _this.stacks[3]
            },{
                name: 'w4_p/s',
                type: 'column',
                color: 'rgba(73,131,97,0.8)',
                data: _this.w_4._3,
                stack: _this.stacks[3]
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
<style scoped>
.highcharts-data-table table {
  min-width: 310px;
  max-width: 800px;
  margin: 1em auto;
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

