
import React, { useState } from 'react';
import axios from 'axios';

const CalculatriceSalaire = () => {
    const [employeId, setEmployeId] = useState('');
    const [autresParametres, setAutresParametres] = useState('');
    const [resultat, setResultat] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:3001/calculer', {
                employeId,
                autresParametres
            });
            setResultat(response.data.resultat);
        } catch (error) {
            console.error('Erreur lors du calcul', error);
        }
    };

    return (
        <div>
            <h1>Calcul du Salaire</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    ID de l'employé :
                    <input 
                        type="text" 
                        value={employeId} 
                        onChange={(e) => setEmployeId(e.target.value)} 
                    />
                </label>
                <br />
                <label>
                    Autres paramètres :
                    <input 
                        type="text" 
                        value={autresParametres} 
                        onChange={(e) => setAutresParametres(e.target.value)} 
                    />
                </label>
                <br />
                <button type="submit">Calculer</button>
            </form>

            {resultat && (
                <div>
                    <h2>Résultat :</h2>
                    <p>{resultat}</p>
                </div>
            )}
        </div>
    );
};

export default CalculatriceSalaire;
