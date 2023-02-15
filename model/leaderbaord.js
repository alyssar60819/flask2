  // API endpoints for adding a new score to the leaderboard, getting a list of the top scores, 
  // and getting a player's score. Here's an example implementation in Node.js using the Express 
  // framework:
  
  const express = require('express');
  const mysql = require('mysql');
  
  const app = express();
  const port = 3000;
  
  const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'leaderboard'
  });
  
  app.use(express.json());
  
  app.post('/scores', (req, res) => {
    const { player_name, score } = req.body;
    const query = 'INSERT INTO leaderboard (player_name, score) VALUES (?, ?)';
    connection.query(query, [player_name, score], (error, results) => {
      if (error) {
        console.error(error);
        res.status(500).send('Error adding score');
      } else {
        res.status(201).send('Score added');
      }
    });
  });
  
  app.get('/scores/top', (req, res) => {
    const query = 'SELECT player_name, score FROM leaderboard ORDER BY score DESC LIMIT 10';
    connection.query(query, (error, results) => {
      if (error) {
        console.error(error);
        res.status(500).send('Error getting top scores');
      } else {
        res.json(results);
      }
    });
  });
  
  app.get('/scores/:player_name', (req, res) => {
    const { player_name } = req.params;
    const query = 'SELECT score FROM leaderboard WHERE player_name = ?';
    connection.query(query, [player_name], (error, results) => {
      if (error) {
        console.error(error);
        res.status(500).send('Error getting score');
      } else if (results.length === 0) {
        res.status(404).send('Player not found');
      } else {
        res.json(results[0]);
      }
    });
  });
  
  app.listen(port, () => {
    console.log(`Listening on port ${port}`);
  });