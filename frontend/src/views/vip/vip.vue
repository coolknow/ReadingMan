<template>
  <div class="box">
    <div class="list-title">
      <div class="list-title-item">
        排名
      </div>
      <div class="list-title-item">
        姓名
      </div>
      <div class="list-title-item">
        总分
      </div>
    </div>
    <div class="list-data">
      <div class="list-data-item" v-for="(item,index) in dataList">
        <div class="val">
          <div v-if="index == 0" style="color: red;">
            第{{index+1}}名
          </div>
          <div v-if="index == 1" style="color: yellow;">
            第{{index+1}}名
          </div>
          <div v-if="index == 2" style="color: green;">
            第{{index+1}}名
          </div>
          <div v-if="index>=3">
            第{{index+1}}名
          </div>
        </div>
        <div class="val">
          {{item.name}}
        </div>
        <div class="val">
          {{item.totalpoints}}分
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {
    mapState
  } from "vuex";

  export default {

    data() {
      return {
        typeList: ["书架", "书单", "关注", "粉丝"],
        currentTypeIndex: 0,
        listData: [0, 1, 2, 3],
        dataList: [{
          index: 1,
          totalpoints: '232323',
          name: '秋月'
        }, {
          index: 1,
          totalpoints: '232323',
          name: '秋月'
        }, {
          index: 1,
          totalpoints: '232323',
          name: '秋月'
        }, {
          index: 1,
          totalpoints: '232323',
          name: '秋月'
        }, {
          index: 1,
          totalpoints: '232323',
          name: '秋月'
        }, ]
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
  @import "./vip.scss";

  .box {
    background-color: rgb(20, 26, 81);
    height: 600px;
    overflow: hidden;

    .list-title {
      display: flex;
      height: 50px;
      line-height: 50px;
      color: rgb(125, 197, 225);
      background-color: rgb(20, 26, 81);
      border: 2px solid #1da3c2;
      margin-top: 20px;

      .list-title-item {
        flex: 1;
        text-align: center;
      }
    }

    .list-data {
      color: rgb(125, 197, 225);

      .list-data-item {
        height: 50px;
        border-bottom: 2px solid #1da3c2;
        display: flex;
        align-items: center;

        .val {
          flex: 1;
          text-align: center;

          img {
            width: 40px;
            height: 40px;
          }
        }
      }
    }
  }
</style>
