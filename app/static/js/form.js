const url = `${location.origin}/save`

const form = document.querySelector('.search-form')
const tweetList = document.querySelector('.message-list')

const createRequestObject = (url, data) => {
    return new Request(url, {
        method: 'POST',
        headers: new Headers({ 'Content-Type': 'application/json' }),
        body: JSON.stringify(data),
        mode: 'cors',
        cache: 'default'
    })
}

const createTweetElement = (content) => {
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

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let paramValue = e.target.elements['hashtags'].value
    fetchData = createRequestObject(url, { 'hashtags': paramValue })

    fetch(fetchData)
        .then(response => response.json())
        .then(content => {
            const data = content.data
            data.forEach(function (el, index) {
                let tweet = createTweetElement(el)
                tweetList.insertAdjacentHTML('beforeend', tweet)
            })
        })
        .catch(err => console.log(err))
})