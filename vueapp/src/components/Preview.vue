<template>
  <div>
    <el-row class="step">
      <el-col><span style="color:#909399;">Step 2. Download mosaic!</span></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="15">
        <el-card>
          <div slot="header" class="clearfix">
            <span style="color: #409EFF">Preview</span>
          </div>
          <!--<img width="100%" height="100%" src="https://c1.staticflickr.com/8/7378/13997705508_a218e00c81_b.jpg">-->
          <img width="100%" height="100%" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzs21eHt5Z9T1EjYd58xNeCqtorkKsKbudaJ1KBfSiF56U52ejdQ">
        </el-card>
      </el-col>
      <el-col :span="9">
        <el-card>
          <div slot="header" class="clearfix">
            <span style="color: #409EFF;">Options</span>
          </div>
          <el-button type="success">Download</el-button>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Vue from 'vue';

  export default Vue.extend({
    name: 'Preview',
    data() {
      return {

      }
    },
  })
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.step {
  margin-bottom:20px;
}
</style>
