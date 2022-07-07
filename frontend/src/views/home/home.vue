<template>
  <div>
    <div class="headerBox">
      <div class="headerCenter">
        <div class="headerLeft">
          <h3 class="titBox">
            <img src="../../assets/logo.png" alt="" srcset="" />
            友趣读书
          </h3>
          <div @click="goto('/')" class="navItem">听书馆</div>
          <div @click="goto('/')" class="navItem">我的书架</div>
          <div @click="goto('/create')" class="navItem">创作平台</div>
           <div @click="goto('/com')" class="navItem">评书社区</div>
        </div>
        <div class="headerRight">
          <el-popover placement="top-start" width="200" trigger="hover">
            <div class="headpicBox" slot="reference">
              <el-avatar
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
              ></el-avatar>
              <div class="nickname">{{ userinfo && userinfo.username }}</div>
            </div>
            <div class="menuBox">
              <div @click="goto('/my')" class="menuItem">听书记录</div>
              <div @click="goto('/vip')" class="menuItem">VIP</div>
            </div>
          </el-popover>
          <div @click="handleLogin" class="out">
            {{ userinfo ? "登出" : "登录" }}
          </div>
        </div>
      </div>
    </div>
    <router-view />
    <!-- 播放器组件 -->
    <player />

    <div class="bottomBox">友趣读书</div>
    <div style="height: 70px;"></div>
  </div>
</template>

<script>
import player from "../../components/player/player.vue";
import { mapState } from "vuex";

export default {
  name: "Home",
  computed: {
    ...mapState(["userinfo"]),
  },
  components: {
    player: player,
  },
  methods: {
    goto(url) {
      this.$router.push(url);
    },
    handleLogin() {
      if (this.userinfo) {
        // 登出
        this.$store.commit("logout");
        this.$router.push("/login");
      } else {
        this.$router.push("/login");
      }
    },
  },
};
</script>
<style>
@import url("./home.css");
</style>
