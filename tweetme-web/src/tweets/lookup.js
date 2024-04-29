import { backendLookup } from '../lookup'

export function apiTweetList(username, callback) {
    const endpoint = username ? `/tweets/?username=${username}` : '/tweets/'
    backendLookup('GET', endpoint, callback)
}

export function apiCreateTweet(newTweet, callback) {
    backendLookup('POST', '/tweets/create/', callback, { content: newTweet })
}

export function apiTweetAction(tweetId, action, callback) {
    const data = { id: tweetId, action: action }
    backendLookup('POST', '/tweets/action/', callback, data)
}

export function apiTweetDetail(tweetId, callback) {
    backendLookup('GET', `/tweets/${tweetId}/`, callback)
}