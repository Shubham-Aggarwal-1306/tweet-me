import logo from './logo.svg';
import './App.css';
import React from 'react'
import { TweetsComponent } from './tweets'


function App(props) {
  console.log(props)

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Tweetme App by <code>Dev</code> and <code>Dev</code>
        </p>
        <TweetsComponent className='col-8 mx-auto' {...props} />
      </header>
    </div>
  );
}

export default App;
