'use strict'

import { hashtagRetrieveUrl } from './routes.js'

export const hashtagList = document.querySelector('.hashtag-list')

export const createPostRequest = (url, data) => {
    return new Request(url, {
        method: 'POST',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        body: JSON.stringify(data),
        mode: 'cors'
    })
}

export const retriveHashtags = () => {
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

export function cleanElementList(list) {
    let child = list.lastElementChild

    while (child) {
        list.removeChild(child)
        child = list.lastElementChild
    }
}

export const createTweetElement = content => {
    return `<div class="tweet-box">
        <div class="image-area">
            <img src="${content.user_profile_image}" class="img-responsive" />
        </div>
        <div class="tweet-area">
            <div class="user-info">
                <p><strong>${content.user_name}</strong> <span class="text-muted">@ ${content.user_screen_name} - ${content.created_at}</span></p>
            </div>
            <div class="user-message">
                <p class="tweet-user-message">${content.message}</p>
            </div>
        </div>
    </div>`
}

export const createHashtagElement = content => (
    `<button type="button" class="hashtag" value="${content}">${content} <span>X</span></button>`
)