import React, { useState, useEffect } from 'react'
import Food_card from './Food.component';
import './App.css'

function Food() {

  const [foodResults, setFoodResults] = useState([]);

  async function fetchFoods() {
    const url = "http://localhost:8000/api/foods";
    const response = await fetch(url);
    const data = await response.json();
    console.log(data)
    setFoodResults(data)
  }

  useEffect(() => {
    fetchFoods()
  }, [])

  return (
    <div className="cards">
      {foodResults.map(food => (
        <Food_card name={food['name']} description={food['description']} image={food['image']} price={food['price']}/>
      ))}
    </div>

  );
}

export default Food;
