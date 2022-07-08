import request from '@/utils/request'
import qs from 'qs'

// 登录
export function login(data) {
  return request({
    // url: '/users/login',
    url: 'http://127.0.0.1:5000/login',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 注册
export function register(data) {
  return request({
    url: 'http://127.0.0.1:5000/register',
    method: 'post',
    data: qs.stringify(data)
  })
}

// 上传文件
export function upload(data) {
  return request({
    url: 'http://127.0.0.1:5000/uploadFilepathToDB',
    method: 'post',
    data: qs.stringify(data)
  })
}

// 上传评论
export function comment(data) {
  return request({
    url: 'http://127.0.0.1:5000/comment',
    method: 'post',
    data: qs.stringify(data)
  })
}

// 是否符合资格
export function right(data) {
  return request({
    // url: '/users/login',
    url: 'http://127.0.0.1:5000/right',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 成为vip
export function vip(data) {
  return request({
    // url: '/users/login',
    url: 'http://127.0.0.1:5000/vip',
    method: 'POST',
    data: qs.stringify(data)
  })
}

// 下载记录
export function downloadnoti(data) {
  return request({
    // url: '/users/login',
    url: 'http://127.0.0.1:5000/download',
    method: 'POST',
    data: qs.stringify(data)
  })
}
