<template>
   <div id="container"></div>
</template>

<script>
import Highcharts from 'highcharts';

export default {
    data() {
        return {
            mapData: {}
        }
    },
    mounted() {
        this.displayMap();
    },
    methods: {
        async displayMap() {
             const _this = this;
            const topology = await fetch('https://code.highcharts.com/mapdata/countries/au/au-all.topo.json').then(response => response.json());
            _this.mapData = [
                { 
                    code: 'au-nt',
                    value: 10,
                }, {
                    code: 'au-wa',
                    value: 11,
                }, {
                    code: 'au-ct',
                    value: 12,
                }, {
                    code: 'au-sa',
                    value: 13,
                }, {
                    code:'au-ql', 
                    value: 14
                }, {
                    code:'au-2557', 
                    value: 15
                }, { 
                    code:'au-ts', 
                    value: 16
                }, {
                    code:'au-jb', 
                    value: 17
                }, {
                    code: 'au-ns',
                    value: 18,
                }, {
                    code: 'au-vi',
                    value: 19,
                }
            ]

            Highcharts.mapChart('container', {
                chart: {
                    map: topology
                },
                title: {
                    text: 'The Distribution of the Clincal Data'
                },
                legend: {
                    layout: 'horizontal',
                    borderWidth: 0,
                    backgroundColor: 'rgba(255, 255, 255, 0.85)',
                    floating: true,
                    verticalAlign: 'top',
                    y: 25
                },
                mapNavigation: {
                    enabled: true,
                },
                colorAxis: {
                    min: 1,
                    type: 'logarithmic',
                    minColor: '#EEEEFF',
                    maxColor: '#000022',
                    stops: [
                        [0, '#EFEFFF'],
                        [0.67, '#4444FF'],
                        [1, '#000022']
                    ]
                },
                series: [{
                    animation: {
                        duration: 1000
                    },
                    data: _this.mapData,
                    joinBy: ['hc-key', 'code'],
                    states: {
                        hover: {
                            color: '#BADA55'
                        }
                    },
                    dataLabels: {
                        enabled: true,
                        color: '#FFFFFF',
                        format: '{point.name}'
                    },
                    name: 'Clinc Count',
                    tooltip: {
                        pointFormat: '{point.name}: {point.value}',
                    }
                }]
            })

        }
    }
}
</script>