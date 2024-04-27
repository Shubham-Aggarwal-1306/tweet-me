import React, { useEffect, useState } from 'react'
import { loadTweet } from '../lookup'

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
                setUserLike(false);
            } else {
                setLikes(likes + 1);
                setUserLike(true);
            }
        } else if (action.type === 'retweet') {
            console.log('retweet')
        }
    }

    return (
        <button className={classNameProp} onClick={(handleActionBackendEvent)}>
            {display}
        </button>
    );
}

export function Tweet(props) {
    const { tweet, className } = props;
    const classNameProp = className ? className : 'col-10 mx-auto col-md-6';
    return <div className={classNameProp}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
            <ActionBtn tweet={tweet} action={{ type: 'like', display: 'Likes' }} />
            <ActionBtn tweet={tweet} action={{ type: 'retweet', display: 'Retweet' }} className='btn btn-success btn-sm' />
        </div>
    </div>
}

export function TweetsComponent(props) {
    const textAreaRef = React.createRef();
    const [newTweets, setNewTweets] = useState([]);
    const handleSubmit = (event) => {
        event.preventDefault();
        console.log('submitting')
        const newVal = textAreaRef.current.value;
        let tempNewTweets = [...newTweets];
        tempNewTweets.unshift({
            content: newVal,
            likes: 0,
            id: 1234
        })
        setNewTweets(tempNewTweets);
        textAreaRef.current.value = ''
        
    }
    return (
        <div className={props.className}>
            <div className='col-12 mb-3'>
                <form>
                    <textarea ref={textAreaRef} className='form-control' placeholder='Your tweet' required={true}>

                    </textarea>
                    <button type='submit' className='btn btn-primary my-3' onClick={handleSubmit}>
                        Tweet
                    </button>
                </form>
            </div>
            <TweetList newTweets={newTweets} />
        </div>
    )
}

export function TweetList(props) {
    const [tweetsInit, setTweetsInit] = useState([]); // state variable
    const [tweets, setTweets] = useState([]); // state variable
    useEffect(() => {
        const myCallback = (response, status) => {
            if (status === 200) {
                setTweetsInit(response)
            } else {
                alert('There was an error')
            }
        }
        loadTweet(myCallback)
    }, [])

    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweetsInit])
    console.log(tweetsInit)
    return tweets.map((item, index) => {
        return <Tweet
            tweet={item}
            className='my-5 py-5 border bg-white text-dark h-100 rounded'
            key={`${index}-{item.id}`}
        />
    })
}





