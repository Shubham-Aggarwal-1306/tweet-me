import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { FeedComponent, TweetDetailComponent } from './tweets/components';
import { ProfileBadgeComponent } from './profiles';

if (document.getElementById('root')) {
  const root = ReactDOM.createRoot(document.getElementById('root'));
  const MyApp = React.createElement(App, document.getElementById('root').dataset);
  root.render(
    MyApp
  );
}

if (document.getElementById('root-feed')) {
  const root = ReactDOM.createRoot(document.getElementById('root-feed'));
  const MyApp = React.createElement(FeedComponent, document.getElementById('root-feed').dataset);
  root.render(
    MyApp
  );
}

if (document.getElementById('root-profile-badge')) {
  const root = ReactDOM.createRoot(document.getElementById('root-profile-badge'));
  const MyApp = React.createElement(ProfileBadgeComponent, document.getElementById('root-profile-badge').dataset);
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
