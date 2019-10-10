import axios from 'axios';

export const test_url = 'http://127.0.0.1:8000';

// 登录
export const requestLogin = params => { return axios.post(`${test_url}/api/user/login`, params).then(res => res.data); };
// 记录访客
export const recordVisitor = params => { return axios.post(`${test_url}/api/user/VisitorRecord`, params).then(res => res.data); };
// 获取项目
export const getProject = (headers, params) => {
    return axios.get(`${test_url}/api/project/project_list`, { params: params, headers:headers}).then(res => res.data); };
// 添加项目
export const addProject = (headers, params) => {
  return axios.post(`${test_url}/api/project/add_project`, params, {headers}).then(res => res.data);};
