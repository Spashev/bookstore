(function ($) {
    'use strict';
    if($("#chart-01").length){

        var options = {
            colors: ["#07427a", "#87bbfd"],
            chart: {
                height:400,
                type: 'bar',
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    endingShape: 'rounded',
                    columnWidth: '55%',
                },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            series: [{
                name: 'Last Month',
                data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
            }, {
                name: 'This Month',
                data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
            }],
            xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },

            fill: {
                opacity: 1

            },
            // legend: {
            //     floating: true
            // },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + " thousands"
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#chart-01"),
            options
        );

        chart.render();
    }
    if($("#chart-02").length){

        var options = {
            colors: ["#ffc100", "#f5a623"],
            chart: {
                height:400,
                type: 'bar',
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: '60%',
                },
            },
            dataLabels: {
                enabled: false
            },
            legend: {
                labels: {
                    colors: "#fff",
                },
            },
            grid: {
                borderColor: 'rgba(255,225,255,0.2)',
                strokeDashArray: '3',

            },
            stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
            },
            series: [{
                name: 'Last Month',
                data: [44, 55, 42, 25, 58, 58, 63, 60, 33]
            }, {
                name: 'This Month',
                data: [76, 20, 40, 98, 87, 50, 91, 98, 60]
            }],
            xaxis: {
                categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            },

            fill: {
                opacity: 1

            },
            // legend: {
            //     floating: true
            // },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + " thousands"
                    }
                }
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#chart-02"),
            options
        );

        chart.render();
    }
    if ($("#chart-03").length) {

        var options = {
            colors: colors[0],
            chart: {
                sparkline: {
                    enabled: true
                },
                height: 150,
                type: 'area',
                toolbar: {
                    show: false
                },
            },
            dataLabels: {
                enabled: false
            },
            fill: {
                opacity: 1,
                type: 'solid'
            },
            stroke: {
                curve: 'straight'
            },
            series: [{
                name: 'series1',
                data: [51, 42, 45, 31, 40, 28, 35]
            }],

            xaxis: {
                type: 'datetime',
                categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"],
            },
            tooltip: {
                x: {
                    format: 'dd/MM/yy HH:mm'
                },
            }
        }

        var chart = new ApexCharts(
            document.querySelector("#chart-03"),
            options
        );

        chart.render();

    }
})(window.jQuery);

