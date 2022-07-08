<template>
  <div class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      :rules="loginRules"
      class="login-form"
      auto-complete="on"
      label-position="left"
    >
      <div class="title-container">
        <h3 class="title">友趣读书</h3>
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="hone" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="用户名"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>

      <el-form-item v-if="!isLogin" prop="ph">
        <span class="svg-container">
          <svg-icon icon-class="phone" />
        </span>
        <el-input
          ref="ph"
          v-model="loginForm.ph"
          placeholder="电话"
          name="ph"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>

      <el-form-item v-if="!isLogin" prop="em">
        <span class="svg-container">
          <svg-icon icon-class="email" />
        </span>
        <el-input
          ref="em"
          v-model="loginForm.em"
          placeholder="Email"
          name="em"
          type="email"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>

      <el-form-item prop="pwd">
        <span class="svg-container">
          <el-icon icon-class="hone" />
        </span>
        <el-input
          :key="passwordType"
          v-model="loginForm.pwd"
          :type="passwordType"
          placeholder="密码"
          name="pwd"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon
            :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'"
          />
        </span>
      </el-form-item>

      <el-form-item v-if="!isLogin" prop="morePwd">
        <span class="svg-container">
          <svg-icon icon-class="hone" />
        </span>
        <el-input
          :key="passwordType"
          v-model="loginForm.morePwd"
          :type="passwordType"
          placeholder="再次输入密码"
          name="morePwd"
          tabindex="2"
          auto-complete="on"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon
            :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'"
          />
        </span>
      </el-form-item>

      <div class="codeBox">
        <slide-verify
          :l="42"
          :r="10"
          :w="450"
          :h="100"
          :imgs="bgImgs"
          slider-text="向右滑动"
          @success="onSuccess"
          @fail="onFail"
          @refresh="onRefresh"
          ref="slideblock"
        ></slide-verify>
      </div>

      <el-button
        :loading="loading"
        type="primary"
        style="width: 100%; margin-bottom: 30px"
        @click.native.prevent="handleLogin"
        >{{ !isLogin ? "立即注册" : "立即登录" }}</el-button
      >
      <div @click="setIsLogin" class="tipBox">
        {{ isLogin ? "还没账号？立即注册" : "已有账号，立即登录" }}
      </div>
    </el-form>
  </div>
</template>

<script>
import { login, register } from "@/api/users";
import b1 from "../../assets/b1.jpg";
import b2 from "../../assets/b2.jpg";
import b3 from "../../assets/b3.jpg";
import b4 from "../../assets/b4.jpg";
import b5 from "../../assets/b5.jpg";

export default {
  name: "Login",
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.loginForm.pwd) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      imgCode: false,
      loginForm: {
        username: "",
        ph:"",
        em:"",
        pwd: "",
        morePwd: "",
      },
      bgImgs: [b1, b2, b3, b4, b5],
      loginRules: {
        username: [
          { required: true, trigger: "blur", message: "请输入您的用户名" },
        ],
        ph:[
          {required:true,trigger:"blur",message:"请输入您的电话"},
        ],
        em:[
          {required:true,trigger:"blur",message:"请输入您的Email"},
        ],
        pwd: [{ required: true, trigger: "blur", message: "请输入您的密码" }],
        morePwd: [
          { required: true, trigger: "blur", message: "请再次输入您的密码" },
          { validator: validatePass, trigger: "blur" },
        ],
      },
      loading: false,
      passwordType: "password",
      redirect: undefined,
      isLogin: true,
    };
  },
  watch: {
    $route: {
      handler: function (route) {
        this.redirect = route.query && route.query.redirect;
      },
      immediate: true,
    },
  },
  methods: {
    setIsLogin() {
      this.isLogin = !this.isLogin;
      this.imgCode = false;
      this.$refs.slideblock.reset();
    },
    onSuccess() {
      this.imgCode = true;
    },
    onFail() {
      this.imgCode = false;
    },
    onRefresh() {
      this.imgCode = false;
    },
    showPwd() {
      if (this.passwordType === "password") {
        this.passwordType = "";
      } else {
        this.passwordType = "password";
      }
      this.$nextTick(() => {
        this.$refs.password.focus();
      });
    },
    handleLogin() {
      if (!this.imgCode) {
        this.$message.error("请完成滑块验证！");
        return;
      }
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          const { username,pwd } = this.loginForm;
          this.loading = true;
          // this.$router.push("/");
          // return;
          if (this.isLogin) {
            // 登录处理
            login({
              username,
              pwd,
            })
              .then((res) => {
                console.log(res);
                if(res.pass){
                  this.loading = false;
                  this.$store.commit("login", res);
                  this.$router.push("/");
                }
                else{
                  alert("用户名或密码错误\n请重新输入");
                  this.loading = false;
                  this.$router.push("/");
                }
              })
              .catch(() => {
                this.loading = false;
              });
          } else {
            // 注册
            const { username,ph,em,pwd } = this.loginForm;
            register({
              username,
              ph,
              em,
              pwd,
            })
              .then((res) => {
                this.loading = false;
                this.setIsLogin();
                if(res.pass){
                  this.$message.success("注册成功，请立即登录！");
                }
                else{
                  alert("注册失败，请重新注册。。");
                  this.$router.push("/");
                }
              })
              .catch(() => {
                this.loading = false;
              });
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
  },
};
</script>

<style lang="scss">
@import "./login.scss";
</style>
