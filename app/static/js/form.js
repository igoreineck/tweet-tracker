'use strict'

import { hashtagSaveUrl, hashtagRetrieveUrl } from './routes.js'
import {
    createPostRequest,
    createHashtagElement,
    cleanElementList,
    hashtagList
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
        .catch(err => console.log(err))

    retriveHashtags()
})

retriveHashtags()

function retriveHashtags() {
    fetch(hashtagRetrieveUrl)
        .then(response => response.json())
        .then(content => {
            cleanElementList(hashtagList)
            content.data.forEach(el => {
                let hashtag = createHashtagElement(el)
                hashtagList.insertAdjacentHTML('beforeend', hashtag)
            })
        })
        .catch(err => console.log(err))
}