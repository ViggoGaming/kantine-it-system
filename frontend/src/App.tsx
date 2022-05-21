import React from 'react';
//import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter } from "react-router-dom";

import Foods from './FetchFoods'
import Header from './Header'

function App() {
  return (
    <div>
        <Header />
        <Foods />
    </div>
  );
}

export default App;
