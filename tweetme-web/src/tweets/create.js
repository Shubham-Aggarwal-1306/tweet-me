import { apiCreateTweet } from './lookup'
import React from 'react'

export function TweetCreate(props) {
    const textAreaRef = React.createRef();
    const { didTweet } = props;
    const handleSubmit = (event) => {
        event.preventDefault();
        const newVal = textAreaRef.current.value;
        const handleBackendCreate = (response, status) => {
            if (status === 201) {
                didTweet(response)
            } else {
                console.log(response)
                alert('An error occurred please try again')
            }
        }
        apiCreateTweet(newVal, handleBackendCreate)
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
        </div>
    )
}
