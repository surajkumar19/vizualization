function getData() {
  var data = [];
  for (var i = 0; i < 50; i++) {
    data.push([Math.ceil(Math.random() * 500), Math.ceil(Math.random() * 500)]);
  }
  return data;
}
var xScale,
    yScale,
    xAxis,
    yAxis,
    rScale,
    svg,
    circles,
    text,
    width = 1000,
    height = 180,
    padding = 30,
    dataset = getData();

xScale = d3.scale.linear();
xScale
.domain([0, d3.max(dataset, function (d) {
  return d[0];
})])
.range([padding, width - padding * 2]);

yScale = d3.scale.linear();
yScale.domain([0, d3.max(dataset, function (d) {
  return d[1];
})])
.range([height - padding, padding]);

rScale = d3.scale.linear();
rScale.domain([0, d3.max(dataset, function (d) {
  return d[1];
})])
.range([2,6]);

xAxis = d3.svg.axis();
xAxis
.scale(xScale)
.orient('bottom')
.ticks(20);

yAxis = d3.svg.axis();
yAxis
.scale(yScale)
.orient('left')
.ticks(5);

svg = d3.select('body').append('svg');
svg.attr({
  width: width,
  height: height
});

circles = svg.append('g')
             .attr('id', 'circles')
             .attr('clip-path', 'url(#chart-area)')
             .selectAll('circle');
circles
.data(dataset)
.enter()
.append('circle')
.attr({
  cx: function (d) {
    return xScale(d[0]);
  },
  cy: function (d) {
    return yScale(d[1]);
  },
  r: function (d) {
    return 2;
  }
});

svg
.append('g')
.attr({
  class: 'x-axis',
  transform: 'translate(0,' + (height - padding) + ')'
})
.call(xAxis);

svg
.append('g')
.attr({
  class: 'y-axis',
  transform: 'translate(' + padding + ', 0)'
})
.call(yAxis);

svg
.append('clipPath')
.attr('id', 'chart-area')
.append('rect')
.attr({
  x: padding,
  y: padding,
  width: width - padding * 3,
  height: height - padding * 2
});

d3.select('p').on('click', function () {
  dataset = getData();
  xScale.domain([0, d3.max(dataset, function (d) { return d[0]})]);
  yScale.domain([0, d3.max(dataset, function (d) { return d[1]})]);
  
  svg
  .select('.x-axis')
  .transition()
  .duration(1000)
  .call(xAxis);
  
  svg
  .select('.y-axis')
  .transition()
  .duration(1000)
  .call(yAxis);
  
    svg
  .selectAll('circle')
  .data(dataset)
  .transition()
  .duration(1000)
  .attr({
    cx: function (d) {
      return xScale(d[0]);
    },
    cy: function (d) {
      return yScale(d[1]);
    }
  });
});