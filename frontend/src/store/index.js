import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		userinfo: null,
		currentIndex: 0,
		playList: [{
			url: '/t.mp3',
			name: '测试'
		}],
		// playList的数据结构如下
		// {
		// 	url: '',
		// 	name: '',
		// }

	},
	mutations: {
		// 删除播放列表
		deletePlayerList(state, {
			list,
			index
		}) {
			if(state.currentIndex == index){
				state.currentIndex = list.length - 1;
			}else{
				if(state.currentIndex > index){
					state.currentIndex = state.currentIndex - 1;
				}
			}
			state.playList = list;

			window.localStorage.setItem("playList", JSON.stringify(list))
		},
		// 新增播放列表
		addPlayeList(state, list) {
			state.playList = list;
			state.currentIndex = list.length - 1;
			window.localStorage.setItem("playList", JSON.stringify(list))
		},
		// 更新播放列表当前歌曲下标
		updateCurrentIndex(state, index) {
			state.currentIndex = index;
		},
		// 更新播放列表
		updatePlayList(state, list) {
			state.playList = list;
			window.localStorage.setItem("playList", JSON.stringify(list))
		},
		// 登录
		login(state, provider) {
			state.userinfo = provider;
			window.localStorage.setItem("userinfo", JSON.stringify(provider))
		},
		// 登出
		logout(state) {
			state.userinfo = null;
			window.localStorage.removeItem("userinfo");
		}
	},
	actions: {

	}
})

export default store
