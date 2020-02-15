'use strict'

import { hashtagRemoveUrl } from './routes.js'
import { createPostRequest, retriveHashtags, hashtagList } from './helpers.js'

function listenChildren(e) {
    if (e.target !== e.currentTarget) {
        const value = e.target.value

        let requestParams = createPostRequest(hashtagRemoveUrl, {
            'hashtag': value
        })
        fetch(requestParams)
            .then(response => response.json())
            .then(() => retriveHashtags())
            .catch(err => console.log(err))
    }
}

hashtagList.addEventListener('click', listenChildren, false)
