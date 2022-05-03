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
    const categories = [
    'area-01', 'area-02', 'area-03', 'area-04',
    'area-05', 'area-06', 'area-07', 'area-08', 'area-09',
    'area-10', 'area-11', 'area-12', 'area-13', 'area-14',
    'area-15', 'area-16', 'area-17', 'area-18', 'area-19',
    'area-20', 'area-21'
    ];
    Highcharts.chart('container1', {
      chart: {
        type: 'bar'
    },
    title: {
        text: 'COVID-19 Affection Number in Top 20 Area for Female and Male'
    },
    subtitle: {
        text: 'Analysis on Gender in Relation with COVID-19 on the top 20 informative areas.'
    },
    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. Age {xDescription}, {value}%.'
        }
    },
    xAxis: [{
        categories: categories,
        reversed: false,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'Age (male)'
        }
    }, { // mirror axis on right side
        opposite: true,
        reversed: false,
        categories: categories,
        linkedTo: 0,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'Age (female)'
        }
    }],
    yAxis: {
        title: {
            text: null
        },
        labels: {
            formatter: function () {
                return Math.abs(this.value) + '%';
            }
        },
        accessibility: {
            description: 'Percentage population',
            rangeDescription: 'Range: 0 to 5%'
        }
    },

    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },

    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + ', ' + this.point.category + '</b><br/>' +
                'Tested Positive: ' + Highcharts.numberFormat(Math.abs(this.point.y), 1);
        }
    },

    series: [{
        name: 'Female',
        color: 'rgba(183,82,241,0.8)',
        data: [
            -2.2, -2.1, -2.2, -2.4,
            -2.7, -3.0, -3.3, -3.2,
            -2.9, -3.5, -4.4, -4.1,
            -3.4, -2.7, -2.3, -2.2,
            -1.6, -0.6, -0.3, -0.0,
            -0.0
        ]
    }, {
        name: 'Male',
        color: 'rgba(238,106,77,0.8)',
        data: [
            2.1, 2.0, 2.1, 2.3, 2.6,
            2.9, 3.2, 3.1, 2.9, 3.4,
            4.3, 4.0, 3.5, 2.9, 2.5,
            2.7, 2.2, 1.1, 0.6, 0.2,
            0.0
        ]
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
