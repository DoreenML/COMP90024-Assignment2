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
        type: 'column'
    },

    title: {
        text: 'Violent Tweet Key Words and Gender Analysis for the Top-10 Areas'
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
        name: 'Kill',
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
        name: 'Hate',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'Hate',
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
        name: 'Harm',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'male'
    }, {
        name: 'Harm',
        data: [3, 0, 4, 4, 3, 1, 4, 7, 5, 2],
        stack: 'female'
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
