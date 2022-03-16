import * as api from './api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

export async function getAllInvestments() {
    return api.get('/data/investments?sortBy=_createdOn%20desc');
}

export async function getInvestmentyId(ticker) {
    return api.get('/data/investments/' + ticker);
}

export async function createInvestment(investment) {
    return api.post('/data/investments', investment);
}

export async function editInvestment(id, investment) {
    return api.put('/data/investments/' + id, investment);
}

export async function deleteById(id) {
    return api.del('/data/investments/' + id);
}

export async function getMyInvestments(userId) {
    return api.get(`/data/investments?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}