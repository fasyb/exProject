import './App.css';
import TableComponent from './components/TableComponent';
import ChartComponent from './components/ChartComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>TypingStats</h1>
      </header>
      <main>
        <TableComponent />
        <ChartComponent />
      </main>
    </div>
  );
}

export default App;