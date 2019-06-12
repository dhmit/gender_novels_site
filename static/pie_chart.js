"use strict";
// const data = [{name: "Subject", val: 72}, {name: "Object", val: 28}];

function pieChart (dataset, colors){
    const data = dataset;

    const svg = d3.select("svg"),
        width = svg.attr("width"),
        height = svg.attr("height"),
        radius = Math.min(width, height) / 2,
        g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    // const color = d3.scaleOrdinal(['#ca3542', '#27647b']);
    const color = colors


    // Generate the arcs
    const arc = d3.arc()
                .innerRadius(0)
                .outerRadius(radius);

    const label = d3.arc()
                      .outerRadius(radius)
                      .innerRadius(radius - 90);

        // Generate the pie
    const create_pie = d3.pie()
                .value(function(d) {
                    return d.val;
                });

    const pie_data = create_pie(data);



    //Generate groups
    const arcs = g.selectAll("arc")
                .data(pie_data)
                .enter()
                .append("g")
                .attr("class", "arc")

    //Draw arc paths
    arcs.append("path")
        .attr("fill", function(d, i) {
            return color(i);
        })
        .attr("d", arc);


    arcs.append("text")
        .attr("transform", function(d) {
                        return "translate(" + label.centroid(d) + ")";
                })
               .text(function(d) { return d.data.name; });
}

