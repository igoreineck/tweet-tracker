'use strict'

import { messageRetrieveUrl } from './routes.js'
import { createTweetElement, cleanElementList } from './helpers.js'

const tweetList = document.querySelector('.message-list')
const interval = 20000

const sync = () => {
    fetch(messageRetrieveUrl)
        .then(response => response.json())
        .then(content => {
            cleanElementList(tweetList)
            let messages = content.data
            messages.forEach(el => {
                let message = createTweetElement(el)
                tweetList.insertAdjacentHTML('beforeend', message)
            })
        })
        .catch(err => console.log(err))
}

setInterval(sync, interval)
sync()