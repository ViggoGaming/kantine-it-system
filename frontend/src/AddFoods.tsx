import React from 'react';
//import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter } from "react-router-dom";

import AddFoodForm from './AddFoodForm';
import Header from './Header'

function AddFoods() {
  return (
    <div>
    <Header />
    <AddFoodForm />
    </div>
  );
}

export default AddFoods;
