import HomePage from '../../video-store-demo/src/components/HomePage';
import './App.css';
import inventory from './data/inventory.json';

export default function App() {
  return (
    <div id="app_root">
      <header>
        <h1>Video Store</h1>
      </header>
      <main>
        <HomePage inventory={inventory} />
      </main>
      <footer>© 2023 Video Store</footer>
    </div>
  );
}
