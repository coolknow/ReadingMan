import request from '@/utils/request'
import qs from 'qs'

// 登录
export function login(data) {
  return request({
    // url: '/users/login',
    url: 'http://127.0.0.1:5000/test/',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 注册
export function register(data) {
  return request({
    url: '/users/register',
    method: 'post',
    data
  })
}
