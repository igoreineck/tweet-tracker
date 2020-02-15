'use strict'

export const createPostRequest = (url, data) => {
    return new Request(url, {
        method: 'POST',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        body: JSON.stringify(data),
        mode: 'cors'
    })
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

export const createHashtagElement = content => `<div>${content} <span>X</span></div>`