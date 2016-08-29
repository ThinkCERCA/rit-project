<?php

// $baserit = $_GET["baserit"] + 1;

$output = array();
exec("python calculations.py ".$_GET["grade"]." ".$_GET["baserit"], $output);
//var_dump( $output);

?>

<html>
<body>
Hello there
      <div style="width: 40%;">
        <canvas id="lineChart" width="100" height="50"></canvas>
      </div>
      <script src="Chart.min.js"></script>

  <script>
  var CHART = document.getElementById('lineChart');

  var withThinkCERCA = <?php echo $output[3] ?>;
  var nationalAverage = <?php echo $output[4] ?>;

  let lineChart = new Chart(CHART,
    {

        type: "bar",
        data: {
            labels: ["Year 1", "Year 2", "Year 3", "Year 4"],
            datasets: [
                {
                  label: "National Average Score",
                  backgroundColor:'#97bfef',
                  borderColor: "#97bfef",
                  borderWidth: 1,
                  data: nationalAverage,
                },
                {
                  label: "Score using ThinkCERCA",
                  backgroundColor: '#307fe2',
                  borderColor: "#333F48",
                  borderWidth: 1,
                  categoryPercentage: 0.8,
                  barPercentage: 0.9,
                  data: withThinkCERCA,
                }]
              },

        options:
              {
                scales:{
                  yAxes:[{
                    ticks:{
                      beginAtZero: false,
                      //min: 180
                      stepSize: 5
                    }
                  }]
                }
              }

    });
    </script>


    Years of Growth: <?php echo $output[2]; ?><br>



</body>
</html>
