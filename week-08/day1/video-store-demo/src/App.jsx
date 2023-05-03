import HomePage from './components/HomePage';
import './App.css';
import inventory from './data/inventory.json';
import Header from './components/Header'
import { useState, useEffect } from 'react';


export default function App() {
  const [data, setData] = useState(inventory)
  useEffect(()=>{}, [data])
  console.log(data)
  return (
    <div id="app_root">
        <Header />
      <main>
        <HomePage inventory={data} changeInventory={setData} name='Terry'/>
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}

