import React, { useEffect, useState } from 'react'
import { apiTweetAction } from './lookup'

export function ActionBtn(props) {

    const { tweet, action, className } = props;
    const actionDisplay = action.display ? action.display : 'Action';
    const classNameProp = className ? className : 'btn btn-primary btn-sm';
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0);
    const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false);
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay;

    const handleActionBackendEvent = (event) => {
        event.preventDefault();
        console.log(tweet.id, action.type);
        if (action.type === 'like') {
            if (userLike === true) {
                // perhaps i Unlike it?
                setLikes(likes - 1);
                apiTweetAction(tweet.id, action.type, (response, status) => {
                    if (status === 200) {
                        setUserLike(false);
                    }
                })
                setUserLike(false);
            } else {
                setLikes(likes + 1);
                apiTweetAction(tweet.id, action.type, (response, status) => {
                    if (status === 200) {
                        setUserLike(true);
                    }
                })
                setUserLike(true);
            }
        } else if (action.type === 'retweet') {
            apiTweetAction(tweet.id, action.type, (response, status) => {
                if (status === 201) {
                    props.handleBackendEvent(response)
                }
            })
        }
    }

    return (
        <button className={classNameProp} onClick={(handleActionBackendEvent)}>
            {display}
        </button>
    );
}