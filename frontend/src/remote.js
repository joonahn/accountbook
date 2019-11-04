let PREFIX = process.env.REACT_APP_BACKEND_URL_PREFIX

export class ForbiddenError extends Error {}
export class PostError extends Error {
    constructor(message, res) {
        super(message)
        this.res = res
    }
}

export async function getAccountList() {
    const url = PREFIX + `/account/`
    return fetch(url, { credentials: 'include' })
        .then(res => {
            if (res.status === 200) {
                return res.json()
            } else if (res.status === 403) {
                throw new ForbiddenError("forbidden")
            }
            return []
        })
}

export async function getCategoryList() {
    const url = PREFIX + `/category/`
    return fetch(url, { credentials: 'include' })
        .then(res => {
            if (res.status === 200) {
                return res.json()
            } else if (res.status === 403) {
                throw new ForbiddenError("forbidden")
            }
            return []
        })
}

export async function getAccountBookDataByAccount(account) {
    const url = PREFIX + `/accountbook/search/?account=${account}`
    return fetch(url, { credentials: 'include' })
        .then(res => {
            if (res.status === 200) {
                return res.json()
            } else if (res.status === 403) {
                throw new ForbiddenError("forbidden")
            }
            return []
        })
}

async function postData(url, data) {
    const formData = new FormData()
    for (var k in data) {
        formData.append(k, data[k])
    }
    return fetch(url, {
        method: 'POST',
        body: formData,
        credentials: 'include',
    }).then(res => {
        if (res.status === 201) {
            return res.json()
        } 
        throw new PostError(res.statusText, res)
    })
}

export async function addAccountBookData(data) {
    const url = PREFIX + `/accountbook/`
    return postData(url, data)
}

export async function addAccount(data) {
    const url = PREFIX + `/account/`
    return postData(url, data)
}

export async function authenticate(user_id, passwd) {
    const url = PREFIX + '/login/'
    const formData = new FormData()
    formData.append('username', user_id)
    formData.append('password', passwd)
    return fetch(url, {
        method: 'POST',
        body: formData,
        credentials: 'include',
    })
}

export async function deauthenticate() {
    const url = PREFIX + '/logout/'
    return fetch(url, {
        credentials: 'include',
    })
}

export async function checkAuthenticated() {
    const url = PREFIX + '/check_login/'
    return fetch(url, {
        credentials: 'include',
    })
}