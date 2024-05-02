import { ActionBtn } from './buttons'
import React from 'react'
import {
    UserDisplay,
    UserPicture
} from '../profiles'

export function Tweet(props) {
    const { tweet, isRetweet, retweeter } = props;
    let className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    className = isRetweet === true ? `${className} p-2 border rounded` : className
    const handleLink = (event) => {
        event.preventDefault();
        window.location.href = `/${tweet.id}`
    }
    var path = window.location.pathname;
    var idRegex = /(?<tweetid>\d+)/;
    var match = path.match(idRegex);
    var urlTweetId = match ? match.groups.tweetid : -1;
    var isDetail = `${tweet.id}` === `${urlTweetId}`;
    return <div className={className}>
        {isRetweet === true && <div className='mb-2'>
            <span className='small text-muted'>Retweet via <UserDisplay user={retweeter} /></span>
        </div>}
        <div className='d-flex'>

            <div className=''>
                <UserPicture user={tweet.user} />
            </div>
            <div className='col-11'>
                <div>

                    <p>
                        <UserDisplay includeFullName user={tweet.user} />
                    </p>
                    <p>{tweet.content}</p>

                    <ParentTweet tweet={tweet} retweeter={tweet.user} />
                </div>
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
        </div>
    </div>
}

export function ParentTweet(props) {
    const { tweet } = props
    return tweet.parent ? <Tweet isRetweet retweeter={props.retweeter} hideActions className={' '} tweet={tweet.parent} /> : null
}