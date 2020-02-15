'use strict'

import { hashtagRemoveUrl } from './routes.js'
import { createPostRequest } from './helpers.js'

const renderedHashtagList = document.querySelector('.hashtag-list')

function listenChildren(e) {
    if (e.target !== e.currentTarget) {
        const value = e.target.value

        let requestParams = createPostRequest(hashtagRemoveUrl, {
            'hashtag': value
        })
        fetch(requestParams)
            .then(response => response.json())
            .then(content => console.log(content))
            .catch(err => console.log(err))
    }
}

renderedHashtagList.addEventListener('click', listenChildren, false)
