<template>
  <div class="box">
    <div class="typeBox">
      <div
        @click="handleTypeClick(item, index)"
        v-for="(item, index) in typeList"
        :class="currentTypeIndex == index ? 'typeItemActive' : ''"
        :key="index"
        class="typeItem"
      >
        {{ item }}
      </div>
    </div>
    <h2 class="h2">精选好书</h2>
    <div class="itemBox">
      <div v-for="(item, index) in listData" :key="index" class="item">
        <div class="itemImgBox">
          <img src="../../assets/book.jpg" alt="" srcset="" />
        </div>
        <div class="itemTit">父亲</div>
        <div class="itemDesc">播放量 30w</div>
      </div>
    </div>
    <h2 class="h2">大咖讲书</h2>
    <div class="itemBox">
      <div v-for="(item, index) in listData" @click="handlePlay('父亲')" :key="index" class="item">
        <div class="itemImgBox">
          <img src="../../assets/book.jpg" alt="" srcset="" />
        </div>
        <div class="itemTit">父亲</div>
        <div class="itemDesc">播放量 30w</div>
      </div>
    </div>
    <h2 class="h2">优质作者</h2>
    <div class="itemBox">
      <div v-for="(item, index) in listData" :key="index" class="item">
        <div class="itemImgBox">
          <img src="../../assets/book2.jpg" alt="" srcset="" />
        </div>
        <div class="itemTit">身边的陌生人</div>
        <div class="itemDesc">播放量 30w</div>
      </div>
    </div>
    <h2 class="h2">排行榜</h2>
    <div class="rankBox">
      <div class="rankItem">
        <h3 class="h3">人气热书</h3>
        <div v-for="i in 5" @click="handlePlay('身边的陌生人')" :key="i" class="rankTit">
          <span class="rankTitOrder">{{ i }}</span>
          <span class="rankTitDesc">身边的陌生人</span>
        </div>
      </div>
      <div class="rankItem">
        <h3 class="h3">本周新书</h3>
        <div v-for="i in 5" @click="handlePlay('身边的陌生人')" :key="i" class="rankTit">
          <span class="rankTitOrder">{{ i }}</span>
          <span class="rankTitDesc">身边的陌生人</span>
        </div>
      </div>
      <div class="rankItem">
        <h3 class="h3">职场提升</h3>
        <div @click="handlePlay('身边的陌生人')" v-for="i in 5" :key="i" class="rankTit">
          <span class="rankTitOrder">{{ i }}</span>
          <span class="rankTitDesc">身边的陌生人</span>
        </div>
      </div>
      <div class="rankItem">
        <h3 class="h3">人文社科</h3>
        <div @click="handlePlay('身边的陌生人')" v-for="i in 5" :key="i" class="rankTit">
          <span class="rankTitOrder">{{ i }}</span>
          <span class="rankTitDesc">身边的陌生人</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Index",
  data() {
    return {
      typeList: ["首页", "本周新书", "心灵", "职场", "人文"],
      currentTypeIndex: 0,
      listData: [0, 1, 2, 3],
    };
  },
  computed: {
    ...mapState(["userinfo", "playList"]),
  },
  mounted() {
    // console.log("userinfo = ", this.userinfo);
  },
  methods: {
    // 类型点击
    handleTypeClick(item, index) {
      this.current = 1;
      this.currentTypeIndex = index;
    },
    handlePlay(name) {
      let deepPlayList = [...this.playList];
      deepPlayList.push({
        url: '/t.mp3',
        name,
      });
      this.$store.commit("addPlayeList", deepPlayList);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./index.scss";
</style>

