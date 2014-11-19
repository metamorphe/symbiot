		//Generates and plots random data points

 			var w = 700;
			var h = 500;
			var padding = 30;

			//Dynamic, random dataset
			var dataset = [];
			var numDataPoints = 50;
			var xRange = Math.random() * 100;
			var yRange = Math.random() * 100;
			for (var i = 0; i < numDataPoints; i++) {
			    var newNumber1 = Math.round(Math.random() * xRange);
			    var newNumber2 = 0;
			    //never return y-value of 0; undefined on log scale
			    while (newNumber2 == 0) {
			    	newNumber2 = Math.round(Math.random() * yRange);
			    }
			    dataset.push([newNumber1, newNumber2]);
			    //sort by increasing x-value
			    dataset.sort(function(a,b) { return parseFloat(a[0]) - parseFloat(b[0]) } );
			}

			//Create scale functions
			var xScale = d3.scale.linear()
								 .domain([0, d3.max(dataset, function(d) { return d[0]; })])
								 .range([padding, w - padding * 2]);
			var yScale = d3.scale.linear()
								 .domain([0, 1000])
								 .range([h - padding, padding]);

			//Define X axis
			var xAxis = d3.svg.axis()
							  .scale(xScale)
							  .orient("bottom");

			//Define Y axis
			var yAxis = d3.svg.axis()
			                  .scale(yScale)
			                  .orient("left")
			                  .ticks(5);
			//Define line
			var line = d3.svg.line()
			    .x(function(d) { return xScale(d[0]); })
			    .y(function(d) { return yScale(d[1]); });

			// Define the div for the tooltip
			var div = d3.select("body").append("div")	
			    .attr("class", "tooltip")				
			    .style("opacity", 0);

			//Create SVG element
			var svg = d3.select("body")
						.append("svg")
						.attr("width", w)
						.attr("height", h);

			//Create circles - plot data points
			svg.selectAll("circle")
			   .data(dataset)
			   .enter().append("circle")
				   .attr("cx", function(d) { return xScale(d[0]); })
				   .attr("cy", function(d) { return yScale(d[1]); })
				   .attr("r", 5)
				   .attr("fill", "steelblue")
			       .on("mouseover", function(d) {		
			            div.transition()		
			                .duration(200)		
			                .style("opacity", .9);		
			            div	.html("[" + d[0] + ", "  + d[1] + "]")	// tool tip message 
			                .style("left", (d3.event.pageX) + "px")		
			                .style("top", (d3.event.pageY - 28) + "px");	
			            })					
			        .on("mouseout", function(d) {		
			            div.transition()		
			                .duration(500)		
			                .style("opacity", 0);	
			        });	
			
			//Create X axis
			svg.append("g")
				.attr("class", "axis")
				.attr("transform", "translate(0," + (h - padding) + ")")
				.call(xAxis);

			//Create Y axis
			svg.append("g")
			    .attr("class", "axis")
			    .attr("transform", "translate(" + padding + ",0)")
			    .call(yAxis);

		    //Create line
		    svg.append("svg:path")
		    	.datum(dataset)
		    	.attr("class", "line")
		    	.attr("d", line)
		    	.style("stroke-width", 2)
		    	.style("stroke", "black")
		    	.style("fill", "none");


		    // returns sum of xValues and log yValues
		    function sumOfProducts(xValues, yValues){
				var sum = 0;
				for (i = 0; i < xValues.length; i++) { 
				    sum += (xValues[i]*yValues[i]);
				}
				return sum;
		    }

		    function sumOfX(xValues){
		    	var sum = 0;
		    	for (i=0; i < xValues.length; i++) {
		    		sum += xValues[i];
		    	}
		    	return sum;
		    }

		    function sumOfY(yValues){
		    	var sum = 0;
		    	for (i=0; i < yValues.length; i++) {
		    		sum += yValues[i];
		    	}
		    	return sum;
		    }

		    function sumOfXSquared(xValues) {
		    	var sum = 0;
		    	for (i=0; i < xValues.length; i++) {
		    		sum += Math.pow(xValues[i], 2);
		    	}
		    	return sum;
		    }

		    function regressionSlope(xValues, yValues) {
		    	var n = xValues.length;
		    	var numerator = n*sumOfProducts(xValues, yValues) - sumOfX(xValues)*sumOfY(yValues);
		    	var denominator = n*sumOfXSquared(xValues) - Math.pow(sumOfX(xValues), 2);
		    	var slope = numerator / denominator;
		    	return slope;
		    }

		    function regressionIntercept(xValues, yValues){
		    	var numerator = sumOfY(yValues) - regressionSlope(xValues, yValues)*sumOfX(xValues);
		    	var n = xValues.length;
		    	var intercept = numerator / n;
		    	return intercept;
		    }

		    function AValue(xValues, yValues) {
		    	var A = Math.pow(10, regressionIntercept(xValues, yValues));
		    	return A;
		    }	

		    function rValue(xValues, yValues) {
		    	var r = Math.pow(10, regressionSlope(xValues, yValues));
		    	return r;
		    }

		    function expRegression(data) {
		    	var newData = $.extend(true, [], data);
		    	var xValues = [];
		    	var yValues = [];
		    	for (var i = 0; i < newData.length; i++) {
		    		xValues[i] = newData[i][0];
		    		yValues[i] = Math.log(newData[i][1]);
		    		console.log(yValues[i]);
		    	}
		    	var A = AValue(xValues, yValues);
		    	var r = rValue(xValues, yValues);
		    	// Calculate new y-values
		    	for (var i = 0; i < newData.length; i++) {
		    		newData[i][1] = A*Math.pow(r, xValues[i]);
		    	}
		    	console.log(newData);
		    	svg.append("svg:path")
			    	.datum(newData)
			    	.attr("class", "line")
			    	.attr("d", line)
			    	.style("stroke-width", 2)
			    	.style("stroke", "black")
			    	.style("fill", "none");
		    }