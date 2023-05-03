import { Outlet } from 'react-router-dom';
import './App.css';
// import SubComponent from './components/SubComponent';
import { useState } from 'react';

export default function App() {
  const [name, setname] = useState();
  return (
    <div id="app_root">
      <header>
        <h1>Video Store</h1>
      </header>
      <main>
        {/* <SubComponent name={name} setName={setName}/> */}
        <Outlet />
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}