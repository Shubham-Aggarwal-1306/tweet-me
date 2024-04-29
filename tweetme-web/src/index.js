import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { TweetDetailComponent } from './tweets/components';

if (document.getElementById('root')) {
  const root = ReactDOM.createRoot(document.getElementById('root'));
  const MyApp = React.createElement(App, document.getElementById('root').dataset);
  root.render(
    MyApp
  );
}

const tweetDetailElements = document.querySelectorAll('.tweetme-2-detail')

tweetDetailElements.forEach(container => {
  const element = React.createElement(TweetDetailComponent, container.dataset);
  const Base = ReactDOM.createRoot(container);
  Base.render(element);
});
