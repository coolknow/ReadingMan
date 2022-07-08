<template>
  <div class="box">
    <div @click="open" class="pulishBtn">
      <i class="el-icon-edit"></i>
      <span>发布</span>
    </div>
    <el-dialog
      title="发布评书"
      :visible.sync="dialogVisible"
      width="50%"
      :before-close="handleClose"
    >
      <div>
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="感想" prop="remark">
            <el-input
              type="textarea"
              :rows="4"
              v-model="ruleForm.remark"
            ></el-input>
          </el-form-item>

          <el-form-item label="封面" prop="cover">
            <el-upload
              :action="`${baseURL}/uploadFile`"
              list-type="picture-card"
              :on-change="handleImgChange"
              :file-list="fileList"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')"
              >立即发表</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>
    <div class="listBox">
      <div v-for="(item, index) in list" :key="index" class="listItem">
        <div class="listItemTop">
          <img
            class="listItemTopHeadpic"
            :src="`https://joeschmoe.io/api/v1/random?a=${index}`"
            alt=""
            srcset=""
          />
          <div class="listItemTopName">{{ `用户${index + 1}` }}</div>
          <div class="listItemTopTime">{{ moment(item.time).fromNow() }}</div>
        </div>
        <div class="listItemDesc">
          {{ item.remark }}
        </div>
        <div v-if="item.cover" class="listItemImgBox">
          <img :src="item.cover" alt="" srcset="" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import t from '../../assets/banner.jpg'
import { comment } from "@/api/users";
import moment from "moment";
moment.locale("zh-cn");
export default {
  name: "Index",
  data() {
    return {
      dialogVisible: false,
      moment,
      list: [
        {
          time: "2020-05-04 18:00:32",
          remark:
            "很多非经济的东西，比如思想启蒙，对美好生活的向往，不对物质保持盲目崇拜，这些只有经历足够多的时间和风雨，才能体会的到。而现在，人们之所以提出内卷，996等各种话题，并且认为这些是有问题的，就是因为：我国经过了几十年的发展，在积累了足够的阅历后，人们才从思想上认识到，这些是有问题的。",
          cover: t,
        },
        {
          time: "2020-05-04 18:00:32",
          remark:
            "很多非经济的东西，比如思想启蒙，对美好生活的向往，不对物质保持盲目崇拜，这些只有经历足够多的时间和风雨，才能体会的到。而现在，人们之所以提出内卷，996等各种话题，并且认为这些是有问题的，就是因为：我国经过了几十年的发展，在积累了足够的阅历后，人们才从思想上认识到，这些是有问题的。",
          cover: t,
        },
      ],
      fileList: [],
      ruleForm: {
        remark: "",
      },
      rules: {
        remark: [{ required: true, trigger: "blur", message: "请输入感想" }],
      },
      formLabelWidth: "120px",
    };
  },
  computed: {
    ...mapState(["userinfo"]),
  },
  mounted() {
    console.log("userinfo = ", this.userinfo);
  },
  methods: {
    // 图片上传双向绑定
    handleImgChange(file, fileList) {
      this.fileList = [file];
    },
    getBase64(file) {
      return new Promise((resolve, reject) => {
        let reader = new FileReader();
        let fileResult = "";
        reader.readAsDataURL(file); //开始转
        reader.onload = function () {
          fileResult = reader.result;
        }; //转 失败
        reader.onerror = function (error) {
          reject(error);
        };
        reader.onloadend = function () {
          resolve(fileResult);
        };
      });
    },
    open() {
      this.dialogVisible = true;
      this.ruleForm = {
        remark: "",
      };
      this.fileList = [];
    },
    submitForm(formName) {
      const remark = this.ruleForm.remark;
      const username = this.userinfo.username;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 上传评论
          comment({
            remark,
            username
          }).then((res) => {
            console.log(res);
            this.$router.push("/");
          });
          //
          if (this.fileList[0]) {
            let file = this.fileList[0].raw;
            this.getBase64(file).then((res) => {
              this.list.unshift({
                time: moment().format("YYYY-MM-DD HH:mm:ss"),
                remark: this.ruleForm.remark,
                cover: res,
              });
            });
          } else {
            this.list.unshift({
              time: moment().format("YYYY-MM-DD HH:mm:ss"),
              remark: this.ruleForm.remark,
            });
          }
          this.dialogVisible = false;
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./com.scss";
</style>
