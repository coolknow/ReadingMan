<template>
  <div class="box">
    <div class="userBox">
      <div>
        <el-avatar
          style="width: 100px; height: 100px"
          src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        ></el-avatar>
        <div class="username">非典型TA<el-button type="vipbutton" circle="boolean" @click="open">VIP</el-button>
        </div>

        <div class="detailBox">
          <div class="detailItem">
            <div class="detailItemTop">16</div>
            <div class="detailItemBottom">关注</div>
          </div>
          <div class="detailItem">
            <div class="detailItemTop">16</div>
            <div class="detailItemBottom">关注</div>
          </div>
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
      <!-- 书架 -->
      <div v-if="currentTypeIndex == 0" class="itemBox">
        <div v-for="(item, index) in listData" :key="index" class="item">
          <div class="itemImgBox">
            <img src="../../assets/book.jpg" alt="" srcset="" />
          </div>
          <div class="itemTit">父亲</div>
          <div class="itemDesc">播放量 30w</div>
        </div>
      </div>
      <!-- 书单 -->
      <div v-if="currentTypeIndex == 1" class="bookListBox">
        <div style="text-align: right">
          <el-button icon="el-icon-plus" size="mini" type="primary">创建书单</el-button>
        </div>
        <el-table header-cell-style="text-align: center;" :data="tableData" style="width: 100%">
          <el-table-column prop="date" label="书单" width="180">
          </el-table-column>
          <el-table-column prop="name" label="节目数" width="180">
          </el-table-column>
          <el-table-column prop="address" label="创建人"> </el-table-column>
           <el-table-column prop="address" label="收藏"> </el-table-column>
        </el-table>
      </div>
      <!-- 关注 -->
      <div v-if="currentTypeIndex == 2" class="followBox">
        <el-row>
          <el-col v-for="i in 30" :key="i" :span="4">
            <div class="followItem">
              <el-avatar
                size="large"
                src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
              ></el-avatar>
              <div class="followItemName">张三</div>
              <div>
                <el-button size="mini" type="primary">已关注</el-button>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
      <!-- 粉丝 -->
      <div v-if="currentTypeIndex == 3" class="followBox">
        <el-row>
          <el-col v-for="i in 30" :key="i" :span="4">
            <div class="followItem">
              <el-avatar
                size="large"
                src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
              ></el-avatar>
              <div class="followItemName">张三</div>
              <div>
                <el-button size="mini" type="primary">已关注</el-button>
              </div>
            </div>
          </el-col>
        </el-row>
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
      vipbutton: '',
      typeList: ["书架", "书单", "关注", "粉丝"],
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
	  open() {
	          this.$alert('您已成功注册vip~', '欢迎小可爱！', {
	            confirmButtonText: '确定',
	            callback: action => {
	              this.$message({
	                type: 'info',
	                message: `action: ${ action }`
	              });
	            }
	          });
	        },
    // 类型点击
    handleTypeClick(item, index) {
      this.current = 1;
      this.currentTypeIndex = index;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./my.scss";
</style>
