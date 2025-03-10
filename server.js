// filepath: my-node-api/src/server.js
const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.get('/calculate-salary/:employeeId', async (req, res) => {
    const employeeId = req.params.employeeId;
    try {
        const response = await axios.get(`http://localhost:5000/calculate-salary/${employeeId}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error calculating salary');
    }
});

app.listen(port, () => {
    console.log(`API server running at http://localhost:${port}`);
});