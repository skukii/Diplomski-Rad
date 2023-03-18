// Import the necessary packages
const express = require('express');

// Create a new Express.js app
const app = express();

app.use(express.static('public'));

// Set the view engine to use EJS templates
app.set('view engine', 'ejs');

// Define a route for the home page
app.get('/', (req, res) => {
    // Render the home page template
    res.render('index', {
        title: 'My Web Page',
        message: 'Welcome to my web page!'
    });
});
app.get('/scatterplot', (req, res) => {
    res.sendFile(__dirname + '/scatterplot.html');
  });
  
app.get('/heatmap', (req, res) => {
    res.sendFile(__dirname + '/heatmap.html');
});


// Start the server
app.listen(5000, () => {
    console.log('Server started on port 5000');
});
