import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar';
import Home from './components/Home';
import InventoryFunc from './components/Inventory';

function App() {
  const [count, setCount] = useState(0)
  const title = "Welcome to the new blog";
  const likes = 50;
  return (
    <div className="App">
      <Navbar />
      <div className="content"></div>
      <Home />
      <p>Liked {likes} times</p>
      <Inventory />
    </div>
  )
}

export default App
