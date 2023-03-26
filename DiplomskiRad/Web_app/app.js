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
app.get('/air_conditions', (req, res) => {
    res.sendFile(__dirname + '/air_conditions.html');
  });
  
app.get('/rain', (req, res) => {
    res.sendFile(__dirname + '/rain.html');
});
app.get('/temperature', (req, res) => {
    res.sendFile(__dirname + '/temperature.html');
});
app.get('/wind', (req, res) => {
    res.sendFile(__dirname + '/wind.html');
});


// Start the server
app.listen(5000, () => {
    console.log('Server started on port 5000');
});
