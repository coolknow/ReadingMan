<template>
  <div class="box">
    <div class="detailBox">
      <div class="detailLeft">
        <div class="addBox">
          <el-button size="small" type="primary">加入书架</el-button>
        </div>
        <img
          class="detailLeftImg"
          src="../../assets/book.jpg"
          alt=""
          srcset=""
        />
        <div class="detailRight">
          <div class="detailRightTop">
            <div class="detailRightTopBookName">书名</div>
            <div class="detailRightTopBookAuthor">作者</div>
          </div>
          <div class="detailRightBottom">播放量 30w</div>
        </div>
      </div>
    </div>

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
    <div class="content">
      <!-- 思维导图 -->
      <div v-if="currentTypeIndex == 0" class="imgBox">
        <img src="../../assets/swdt.png" alt="" srcset="" />
      </div>
      <!-- 文字稿 -->
      <div v-if="currentTypeIndex == 1" class="imgBox">
        <img src="../../assets/wz.png" alt="" srcset="" />
      </div>
      <!-- 相关推荐 -->
      <div v-if="currentTypeIndex == 2" class="itemBox">
        <div v-for="(item, index) in listData" :key="index" class="item">
          <div class="itemImgBox">
            <img src="../../assets/book.jpg" alt="" srcset="" />
          </div>
          <div class="itemTit">父亲</div>
          <div class="itemDesc">播放量 30w</div>
        </div>
      </div>
      <!-- 评论 -->
      <div v-if="currentTypeIndex == 3" class="remarkBox">
        <div class="remarkTop">
          <h3>25条评论</h3>
          <el-button icon="el-icon-plus" size="mini" type="primary"
            >添加评论</el-button
          >
        </div>

        <div v-for="i in 5" :key="i" class="remarkListItem">
          <div class="remarkListItemTop">
            <div class="remarkListItemTopLeft">
              <div class="remarkListItemTopLeftName">晨光</div>
              <div class="remarkListItemTopLeftTime">5个月前</div>
            </div>
            <div class="remarkListItemTopRight">
              <span class="remarkListItemTopRightLabel">794</span>
              <!-- <i style="color: #666;" class="el-icon-zan"></i> -->
              <svg-icon icon-class="zan" />
            </div>
          </div>
          <div class="remarkListItemBottom">好美</div>
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
      typeList: ["思维导图", "文字稿", "相关推荐", "评论"],
      currentTypeIndex: 0,
      listData: [0, 1, 2, 3],
    };
  },
  computed: {
    ...mapState(["userinfo"]),
  },
  mounted() {
    console.log("userinfo = ", this.userinfo);
  },
  methods: {
    // 类型点击
    handleTypeClick(item, index) {
      this.current = 1;
      this.currentTypeIndex = index;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./detail.scss";
</style>

