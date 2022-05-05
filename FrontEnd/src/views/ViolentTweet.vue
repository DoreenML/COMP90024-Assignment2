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
      chart: {
        type: 'column'
    },

    title: {
        text: 'Violent Tweet Key Word for the Top-10 Violent Tweet Areas'
    },

    xAxis: {
        categories: ['area-1', 'area-2', 'area-3', 'area-4', 'area-5', 'area-6', 'area-7', 'area-8', 'area-9', 'area-10']
    },

    yAxis: {
        allowDecimals: false,
        min: 0,
        title: {
            text: 'Number of Violent Key Words'
        }
    },

    legend: {
        labelFormatter: function() {
        return this.name + ' (' + this.userOptions.stack + ')';
        }
    },
    tooltip: {
        formatter: function() {
        var stackName = this.series.userOptions.stack;

        return '<b>Gender: </b>' + stackName + '<br/><b>' + this.x + '</b><br/>' +
            this.series.name + ': ' + this.y + '<br/>' +
            'Total: ' + this.point.stackTotal;
        }
    },

    plotOptions: {
        column: {
            stacking: 'normal'
        }
    },

    series: [{
        name: 'Kill',
        data: [5, 3, 4, 7, 2, 6, 4, 7, 9, 11],
        stack: 'male'
    }, {
        name: 'kill',
        data: [3, 4, 4, 4, 4, 4, 7, 2, 5, 3],
        stack: 'female'
    },{
        name: 'Shoot',
        data: [3, 4, 4, 2, 5, 3, 4, 4, 4, 7],
        stack: 'female'
    },{
        name: 'Shoot',
        data: [3, 4, 4, 2, 5, 3, 4, 4, 4, 7],
        stack: 'male'
    }, {
        name: 'Stab',
        data: [2, 5, 6, 2, 1, 8, 6, 9, 7, 2],
        stack: 'male'
    }, {
        name: 'Stab',
        data: [2, 5, 6, 2, 1, 8, 6, 9, 7, 2],
        stack: 'female'
    }, {
        name: 'Gun',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Gun',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'Drug',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'Drug',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Fight',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Fight',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'hate',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'hate',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Die',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'Die',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Threat',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }, {
        name: 'Threat',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'harm',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'harm',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
    }]
    });
    Highcharts.chart('container2', {
        chart: {
        type: 'area'
    },
    title: {
        text: 'Corresponding COVID-19 Cases for the Top-10 Violent Tweet Areas '
    },
    subtitle: {
        text: 'Source: Wikipedia.org'
    },
    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. {point.category}, {point.y:,.0f} millions, {point.percentage:.1f}%.'
        }
    },
    xAxis: {
        categories: ['1-month', '2-month', '3-month', '4-month', '5-month', '6-month', '7-month'],
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
            enabled: false
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
        data: [502, 635, 809, 947, 1402, 3634, 5268]
    }, {
        name: 'area-2',
        data: [106, 107, 111, 133, 221, 767, 1766]
    }, {
        name: 'area-3',
        data: [163, 203, 276, 408, 547, 729, 628]
    }, {
        name: 'area-4',
        data: [18, 31, 54, 156, 339, 818, 1201]
    }, {
        name: 'area-5',
        data: [2, 2, 2, 6, 13, 30, 46]
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
