<template>
  <div class="box">
    <div class="boxLeft">
      <div class="tabItem tabItemAvtive">发布作品</div>
      <div class="tabItem">我的发布</div>
      <div class="tabItem">数据看板</div>
    </div>
    <div class="boxRight">
      <el-card style="margin-bottom: 20px;">
        <div class="uploadBox">
          <el-upload
            class="upload-demo"
            drag
            action="https://jsonplaceholder.typicode.com/posts/"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或<em>点击上传</em>
            </div>
            <div class="el-upload__tip" slot="tip">音频格式：mp3</div>
          </el-upload>
        </div>
      </el-card>
      <el-card style="margin-bottom: 20px;">
        <div class="uploadBox">
          <el-upload
            class="upload-demo"
            drag
            action="https://jsonplaceholder.typicode.com/posts/"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将文件拖到此处，或<em>点击上传</em>
            </div>
            <div class="el-upload__tip" slot="tip">文件可识别类型：思维导图.jpg/.png;文字稿.txt</div>
          </el-upload>
        </div>
      </el-card>

      <el-card>
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="视频标题" prop="title">
            <el-input v-model="ruleForm.title"></el-input>
          </el-form-item>
          <el-form-item label="书名" prop="bookName">
            <el-input v-model="ruleForm.bookName"></el-input>
          </el-form-item>
          <el-form-item label="标签" prop="tag">
            <el-select
              style="width: 100%"
              v-model="ruleForm.tag"
              multiple
              placeholder="请选择标签"
            >
              <el-option
                v-for="item in [
                  {
                    label: '职场',
                    value: '职场',
                  },
                  {
                    label: '人文',
                    value: '人文',
                  },
                ]"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="简介" prop="desc">
            <el-input type="textarea" v-model="ruleForm.desc"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')"
              >立即创建</el-button
            >
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Index",
  data() {
    return {
      ruleForm: {
        title: "",
        bookName: "",
        tag: "",
        desc: "",
      },
      rules: {
        title: [{ required: true, trigger: "blur", message: "请输入标题" }],
        bookName: [{ required: true, trigger: "blur", message: "请输入书名" }],
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
  methods: {},
};
</script>

<style lang="scss" scoped>
@import "./create.scss";
</style>
