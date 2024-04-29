import React, { useEffect, useState } from 'react'
import { apiTweetList } from './lookup'
import { Tweet } from './detail'

export function TweetList(props) {
    const [tweetsInit, setTweetsInit] = useState([]); // state variable
    const [tweets, setTweets] = useState([]); // state variable
    const [tweetsDidSet, setTweetsDidSet] = useState(false); // state variable
    console.log(props)
    useEffect(() => {
        if (tweetsDidSet === false) {
            const myCallback = (response, status) => {
                if (status === 200) {
                    setTweetsInit(response)
                    setTweetsDidSet(true)
                } else {
                    alert('There was an error')
                }
            }
            apiTweetList(props.username, myCallback)
        }
    }, [tweetsInit, tweetsDidSet, setTweetsInit])

    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweetsInit])
    console.log(tweetsInit)
    const handleRetweet = (newTweet) => {
        let tempNewTweets = [...tweets];
        tempNewTweets.unshift(newTweet);
        setTweets(tempNewTweets);
    }
    return tweets.map((item, index) => {
        return <Tweet
            tweet={item}
            handleBackendEvent={handleRetweet}
            className='my-5 py-5 border bg-white text-dark h-100 rounded col-12'
            key={`${item.id}`}
        />
    })
}

