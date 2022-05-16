<!-- Qi Li & 1138875 & lql4@student.unimelb.edu.au
Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au -->
<template>
  <figure class='highcharts-figure'>
    <div id='container'></div>
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
     Highcharts.chart('container', {
    chart: {
        type: 'area'
    },
    title: {
        text: 'Corresponding COVID-19 Cases for the Top-10 Violent Tweet Areas Timeline'
    },
    subtitle: {
        text: 'aaaa'
    },
    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. {point.category}, {point.y:,.0f} millions, {point.percentage:.1f}%.'
        }
    },
    xAxis: {
        categories: ['1-month', '2-month', '3-month', '4-month', '5-month', '6-month', '7-month', '8-month', '9-month', '10-month', '11-month', '12-month'],
        tickmarkPlacement: 'on',
        title: {
            enabled: false
        }
    },
    yAxis: {
        labels: {
            format: '{value}%'
        },
        title: {
            text: 'Number of COVID Cases'
        }
    },
    tooltip: {
        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.percentage:.1f}%</b> ({point.y:,.0f} k)<br/>',
        split: true
    },
    plotOptions: {
        area: {
            stacking: 'percent',
            lineColor: '#ffffff',
            lineWidth: 1,
            marker: {
                lineWidth: 1,
                lineColor: '#ffffff'
            }
        }
    },
    series: [{
        name: 'area-1',
        data: [502, 635, 809, 947, 140, 334, 526, 182, 124, 343, 453, 456]
    }, {
        name: 'area-2',
        data: [106, 107, 111, 133, 221, 767, 176, 140, 364, 568, 892, 343]
    }, {
        name: 'area-3',
        data: [163, 203, 276, 408, 547, 729, 628, 140, 634, 568, 892, 402]
    }, {
        name: 'area-4',
        data: [18, 31, 54, 156, 339, 818, 1201, 408, 547, 729, 628, 422]
    }, {
        name: 'area-5',
        data: [2, 2, 2, 156, 339, 818, 120, 176, 140, 363, 568, 402]
    }, {
        name: 'area-6',
        data: [163, 203, 276, 408, 13, 30, 46, 334, 268, 892, 402, 345]
    }, {
        name: 'area-7',
        data: [502, 635, 809, 947, 134, 303, 462, 628, 402, 634, 526, 324]
    }, {
        name: 'area-8',
        data: [232, 232, 532, 633, 221, 767, 166, 133, 221, 767, 766, 231]
    }, {
        name: 'area-9',
        data: [163, 203, 276, 408, 513, 330, 462, 818, 201, 766, 402, 341]
    }, {
        name: 'area-10',
        data: [276, 408, 547, 729, 213, 340, 646, 408, 413, 530, 446, 634]
    }]
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
  font-weight: 800;
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
