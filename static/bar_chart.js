"use strict";


/**
 * Constructs a bar chart
 *
 * @param data: dictionary where keys are date and frequency
 * @param svg_id: id attribute to svg for placement of the chart
 */
function makeBarChart(data, svg_id) {
    const svg = d3.select(svg_id),
        margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom,
        x = d3.scaleBand().rangeRound([0, width]).padding(0.2),
        y = d3.scaleLinear().rangeRound([height, 0]),
        g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

    x.domain(data.map(d => d.date));
    y.domain([0, d3.max(data, d => d.frequency)]);

    g.append("g")
        .attr("class", "axis axis-x")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));

    g.append("g")
        .attr("class", "axis axis-y")
        .call(d3.axisLeft(y).ticks(10).tickSize(8));

    g.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.date))
        .attr("y", d => y(d.frequency))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.frequency));
}