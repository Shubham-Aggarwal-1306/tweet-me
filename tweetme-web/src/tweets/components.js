import React, { useEffect, useState } from 'react'
import { TweetList } from './list';
import { TweetCreate } from './create';
import { Tweet } from './detail';
import { apiTweetDetail } from './lookup';

export function TweetsComponent(props) {
    const canTweet = props.canTweet === 'false' ? false : true;
    const [newTweets, setNewTweets] = useState([]);

    const handleBackendCreate = (newTweet) => {
        let tempNewTweets = [...newTweets];
        tempNewTweets.unshift(newTweet);
        setNewTweets(tempNewTweets);
    }
    return (
        <div className={props.className}>
            {canTweet === true &&
                <TweetCreate didTweet={handleBackendCreate} className='col-12 mb-3' />
            }
            <TweetList newTweets={newTweets} {...props} />
        </div>
    )
}


export function TweetDetailComponent(props) {
    const { tweetId } = props;
    console.log("tweetId", tweetId) // tweetId 1
    const [didLookup, setDidLookup] = useState(false);
    const [tweet, setTweet] = useState(null);
    const handleBackendLookup = (response, status) => {
        if (status === 200) {
            setTweet(response);
            console.log("tweet:", response) // {content: "tweet 1", likes: 0, id: 1}
        } else {
            alert('There was an error finding your tweet.')
        }
    }
    useEffect(() => {
        if (didLookup === false) {
            apiTweetDetail(tweetId, handleBackendLookup);
            setDidLookup(true);
        } 
    }, [tweetId, didLookup, setDidLookup, setTweet])
    return tweet === null ? null : <Tweet tweet={tweet} className={props.className} />
}






