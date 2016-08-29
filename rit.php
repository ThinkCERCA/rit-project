<?php

// $baserit = $_GET["baserit"] + 1;

$output = array();
exec("python calculations.py ".$_GET["grade"]." ".$_GET["baserit"], $output);
//var_dump( $output);

?>

<html>

<head>
  <title>ThinkCERCA RIT Score Calculator</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

      <div style="width: 40%;">
        <canvas id="lineChart" width="100" height="50"></canvas>
      </div>
      <script src="Chart.min.js"></script>


  <script>
  var CHART = document.getElementById('lineChart');

  var withThinkCERCA = <?php echo $output[1] ?>;
  var nationalAverage = <?php echo $output[0] ?>;


  let lineChart = new Chart(CHART,
    {

        type: "bar",
        data: {
            labels: ["Year 1", "Year 2", "Year 3"],
            datasets: [
                {
                  label: "National Average Growth",
                  backgroundColor:'#97bfef',
                  borderColor: "#97bfef",
                  borderWidth: 1,
                  data: nationalAverage,
                },
                {
                  label: "Growth with ThinkCERCA",
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
                      beginAtZero: true,
                      max: 12,
                      stepSize: 2
                    }
                  }]
                }
              }

    });
    </script>


    Years of Growth: <?php echo $output[2]; ?><br>



</body>
<br>

<div class="container-fluid bg-grey">
  <div class="row">
    <div class="col-sm-7">
      <h2>Learn how we can make this happen in your classrooms.</h2>
      <div class="row">
        <div class="col-sm-6 form-group">
          <input class="form-control" id="name" name="name" placeholder="Name" type="text" required>
        </div>
        <div class="col-sm-6 form-group">
          <input class="form-control" id="email" name="email" placeholder="Email" type="email" required>
        </div>
      </div>
      <textarea class="form-control" id="comments" name="message" placeholder="Message" rows="5"></textarea><br>
      <div class="row">
        <div class="col-sm-12 form-group">
          <button class="btn btn-default pull-right" type="submit">Send</button>
        </div>
      </div>


    </div><br>
    <div class="col-sm-7">

      <p><span class="glyphicon glyphicon-map-marker"></span> Chicago, US</p>
      <p><span class="glyphicon glyphicon-phone"></span> (408) 215 - 8610</p>
      <p><span class="glyphicon glyphicon-envelope"></span> katy@thinkCERCA.com</p>



    </div>
  </div>
</div>


</html>
