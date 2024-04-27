import logo from './logo.svg';
import './App.css';
import React from 'react'
import { TweetsComponent } from './tweets'


function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Tweetme App by <code>Dev</code> and <code>Dev</code>
        </p>
        <TweetsComponent />
      </header>
    </div>
  );
}

export default App;
