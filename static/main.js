let label1 = ["{{ a }}","{{ b }}","{{ c }}","{{ d }}"]
let data1 = ["{{ e }}","{{ f }}","{{ g }}","{{ h }}"]
let myDoughnutChart = document.getElementById("myChart").getContext('2d');
new Chart(myDoughnutChart, {
    type: 'doughnut',
    data: {
        labels: label1,
        datasets: [
            {
              label: "Population (millions)",
              backgroundColor: ["#000", "#8e5ea2","#3cba9f","#e8c3b9"],
              data: data1
            }
          ]
        },
    options: {
        title: {
            display: true,
            text: 'Bachelors Degree Distribution'
          }
        }
    });
