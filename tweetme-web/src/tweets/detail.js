import { ActionBtn } from './buttons'
import React from 'react'

export function Tweet(props) {
    const { tweet, className } = props;
    const classNameProp = className ? className : 'col-10 mx-auto';
    const handleLink = (event) => {
        event.preventDefault();
        window.location.href = `/${tweet.id}`
    }
    var path = window.location.pathname;
    var idRegex = /(?<tweetid>\d+)/;
    var match = path.match(idRegex);
    var urlTweetId = match ? match.groups.tweetid : -1;
    var isDetail = `${tweet.id}` === `${urlTweetId}`;
    return <div className={classNameProp}>
        <div><p>{tweet.id} - {tweet.content}</p></div>
        <ParentTweet tweet={tweet} />
        <div className='btn btn-group'>
            {!props.hideActions &&
                <React.Fragment>
                    <ActionBtn tweet={tweet} action={{ type: 'like', display: 'Likes' }} />
                    <ActionBtn tweet={tweet} action={{ type: 'retweet', display: 'Retweet' }} className='btn btn-success btn-sm' handleBackendEvent={props.handleBackendEvent} />
                </React.Fragment>
            }
            {!isDetail && <button className='btn btn-outline-primary btn-sm' onClick={handleLink}>Visit</button>}
        </div>
    </div>
}

const ParentTweet = (props) => {
    const { tweet } = props;
    return tweet.parent ? <div className='row'>
        <div className='col-11 mx-auto p-3 border rounded'>
            <p className="mb-0 text-muted small">
                Retweet
            </p>
            <Tweet hideActions className={' '} tweet={tweet.parent} />
        </div>
    </div> : null
}