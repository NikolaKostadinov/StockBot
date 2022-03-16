export function setUserData(data) {
    sessionStorage.setItem('userData', JSON.stringify(data));
}

export function getUserData(data) {
    return JSON.parse(sessionStorage.getItem('userData'));
}

export function clearUserData(data) {
    sessionStorage.removeItem('userData');
}