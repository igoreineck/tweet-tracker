'use strict'

import { hashtagSaveUrl } from './routes.js'
import {
    createPostRequest,
    retriveHashtags
} from './helpers.js'

const form = document.querySelector('.search-form')

form.addEventListener('submit', e => {
    e.preventDefault()

    let values = e.target.elements['hashtags'].value
    let requestParams = createPostRequest(hashtagSaveUrl, {
        'hashtags': values
    })
    fetch(requestParams)
        .then(response => response.json())
        .then(() => retriveHashtags())
        .catch(err => console.log(err))
})

retriveHashtags()