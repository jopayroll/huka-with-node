// filepath: my-react-app/src/App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [employeeId, setEmployeeId] = useState('');
    const [salary, setSalary] = useState(null);

    const handleCalculateSalary = async () => {
        try {
            const response = await axios.get(`http://localhost:3000/calculate-salary/${employeeId}`);
            setSalary(response.data.salary);
        } catch (error) {
            console.error('Error calculating salary', error);
        }
    };

    return (
        <div>
            <h1>Calculate Employee Salary</h1>
            <input
                type="text"
                value={employeeId}
                onChange={(e) => setEmployeeId(e.target.value)}
                placeholder="Enter Employee ID"
            />
            <button onClick={handleCalculateSalary}>Calculate Salary</button>
            {salary !== null && <p>Calculated Salary: {salary}</p>}
        </div>
    );
}

export default App;