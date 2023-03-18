const d3 = require('d3');
// Define the data for the scatter plot
const data = [
  { x: 10, y: 20 },
  { x: 20, y: 30 },
  { x: 30, y: 40 },
  { x: 40, y: 50 },
  { x: 50, y: 60 }
];

// Define the dimensions of the SVG container
const width = 500;
const height = 300;

// Create the SVG container
const svg = d3.select('body')
  .append('svg')
  .attr('width', width)
  .attr('height', height);

// Add the data points to the scatter plot
svg.selectAll('circle')
  .data(data)
  .enter()
  .append('circle')
  .attr('cx', d => d.x)
  .attr('cy', d => d.y)
  .attr('r', 5)
  .attr('fill', 'blue');
