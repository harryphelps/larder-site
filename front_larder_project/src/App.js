import ItemList from './larder/item_list' 
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
		<h1>Welcome to the Larder</h1>
        <img src="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/the-health-benefits-of-onions-main-image-700-350-8425535.jpg?webp=true&quality=90&resize=385%2C350" className="App-logo" alt="logo" />
		<ItemList/>
      </header>
    </div>
  );
}

export default App;
