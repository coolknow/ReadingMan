<template>
  <div class="playerBox">
    <div @click="gotoCurrent" v-if="playList.length"  class="coverBox">
      <img
        style="height: 50px; margin-right: 10px; border-radius: 5px"
        src="/book.jpg"
        alt=""
        srcset=""
      />
      <div class="songName">
        {{ playList.length && playList[currentIndex].name }}
      </div>
    </div>
    <i
      @click="handlePlayMode"
      class="icon"
      :class="playMode ? 'el-icon-refresh' : 'el-icon-refresh-left'"
    ></i>
    <span style="font-size: 12px">{{
      playMode ? "列表循环" : "顺序播放"
    }}</span>
    <i @click="pre" class="el-icon-d-arrow-left icon"></i>
    <audio
      :key="playList.length && playList[currentIndex]"
      ref="myAudio"
      style="margin-left: 30px"
      controls
      autoplay
      controlsList="nodownload"
    >
      <source
        :src="playList.length && playList[currentIndex].url"
        type="audio/mp3"
      />
    </audio>
    <a :href="playList[currentIndex].url" download ><el-button @click="downloadinform">下载</el-button></a>
    <i @click="next" class="el-icon-d-arrow-right icon"></i>
    <!-- 播放列表 -->
    <div class="menuBox">
      <i @click="openMenu" class="el-icon-menu icon"></i>
      <div v-if="showPlayList" class="menuCard">
        <el-card>
          <div class="songList">
            <div
              v-if="playList.length == 0"
              style="color: #888; text-align: center"
            >
              列表为空~
            </div>
            <div
              @click="handleItemClick(index)"
              :class="currentIndex == index ? 'songItemActive' : ''"
              v-for="(item, index) in playList"
              :key="index"
              class="songItem"
            >
              <div class="songItemName">《{{ item.name }}》</div>
              <i
                @click.stop="handleDelete(index)"
                style="color: red; cursor: pointer"
                class="el-icon-delete"
              ></i>
            </div>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { downloadnoti } from "@/api/users";

export default {
  name: "Index",
  data() {
    return {
      showPlayList: false,
      playMode: false,
    };
  },
  computed: {
    ...mapState(["userinfo", "playList", "currentIndex"]),
  },
  mounted() {
    // 监听播放完毕处理事件
    this.$refs["myAudio"].addEventListener("ended", () => {
      this.next();
    });
    // 从缓存中读取歌曲
    if (window.localStorage.playList) {
      this.$store.commit(
        "updatePlayList",
        JSON.parse(window.localStorage.playList)
      );
    }
  },
  methods: {
    gotoCurrent() {
      this.$router.push("/detail");
    },
    // 播放模式（随机播放、列表循环）
    handlePlayMode() {
      this.playMode = !this.playMode;
    },
    // 上一首
    pre() {
      // 列表循环模式
      if (this.playMode) {
        let index = this.currentIndex;
        if (index == 0) {
          index = this.playList.length - 1;
        } else {
          index -= 1;
        }
        this.$store.commit("updateCurrentIndex", index);
      } else {
        // 列表顺序播放
        if (this.currentIndex == 0) {
          this.$message.error("已经是第一首歌了~");
          return;
        }
        this.$store.commit("updateCurrentIndex", this.currentIndex - 1);
      }
    },
    // 下一首
    next() {
      // 列表循环模式
      if (this.playMode) {
        let index = this.currentIndex;
        if (this.currentIndex == this.playList.length - 1) {
          index = 0;
        } else {
          index += 1;
        }
        this.$store.commit("updateCurrentIndex", index);
      } else {
        if (this.currentIndex == this.playList.length - 1) {
          this.$message.error("已经是最后一首歌了~");
          return;
        }
        this.$store.commit("updateCurrentIndex", this.currentIndex + 1);
      }
    },
    // 搜藏
    collect() {},
    // 打开或关闭播放列表
    openMenu() {
      this.showPlayList = !this.showPlayList;
    },
    // 播放列表的点击
    handleItemClick(index) {
      this.$store.commit("updateCurrentIndex", index);
    },
    // 播放列表移除歌曲
    handleDelete(index) {
      let deepList = [...this.playList];
      deepList.splice(index, 1);
      this.$store.commit("deletePlayerList", { index, list: deepList });
    },
    downloadinform(){
      if (this.userinfo){
        const username = this.userinfo.username;
        alert(this.playList[this.currentIndex].url);
        downloadnoti({
          username
        }).then((res) => {
          console.log(res);
          if(res.result){
            this.$router.push(url);
          }
          else{
            alert("资格不符合");
            this.$router.push("/");
          }
        });
        this.$router.push("/");
      }
      else{
        alert("请先登陆");
        this.$router.push("/");
      }
    }
  },
};
</script>

<style scoped lang="scss">
@import "./player.scss";
</style>
