import logo from './logo.svg';
import './App.css';
import React from 'react'
import { TweetsComponent } from './tweets'


function App(props) {
  console.log(props)

  return (
    <div className="App">
        <TweetsComponent className='col-8 mx-auto' {...props} />
    </div>
  );
}

export default App;
