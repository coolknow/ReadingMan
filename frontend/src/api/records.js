import request from '@/utils/request'

// 新增预约
export function add(data) {
  return request({
    url: '/records/add',
    method: 'post',
    data
  })
}
// 批量新增
export function importFile(data) {
  return request({
    url: '/records/bulkAdd',
    method: 'post',
    data
  })
}
// 查看所有预约记录
export function getAllRecords() {
  return request({
    url: '/records/all',
    method: 'get',
  })
}
// 查询我的预约记录
export function getMyRecords(params) {
  return request({
    url: '/records/my',
    method: 'get',
    params
  })
}
// 删除我的预约
export function deleteMyRecords(id) {
  return request({
    url: `/records/${id}`,
    method: 'delete',
  })
}