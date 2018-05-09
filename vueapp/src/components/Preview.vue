<template>
  <div>
    <el-row class="step">
      <el-col><span style="color:#909399;">Step 2. Download mosaic!</span></el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="15">
        <el-card v-loading="loading">
          <div slot="header" class="clearfix">
            <span style="color: #409EFF">Preview</span>
          </div>
          <!--<img width="100%" height="100%" src="https://c1.staticflickr.com/8/7378/13997705508_a218e00c81_b.jpg">-->
          <img width="100%" height="100%" v-if="imageUrl.length" :src="imageUrl">
          <i v-else class="el-icon-picture-outline" style="font-size: 100px;"></i>
          <el-alert v-if="hasError"
            :title="errorMessage"
            type="error"
            :description="errorDescription"
            show-icon
            center
          ></el-alert>
        </el-card>
      </el-col>
      <el-col :span="9">
        <el-card>
          <div slot="header" class="clearfix">
            <span style="color: #409EFF;">Options</span>
          </div>
          <el-row class="button-row" type="flex" justify="center">
            <el-col :span="6">
              <el-button
                style="width: 100%;"
                type="success"
                icon="el-icon-download"
                :disabled="hasError"
                @click="downloadImage"
              >Download</el-button>
            </el-col>
          </el-row>
          <el-row class="button-row"  type="flex" justify="center">
            <el-col :span="6">
              <el-button
                style="width: 100%"
                type="primary"
                icon="el-icon-refresh"
                @click="$router.push('/')"
              >Start again</el-button>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Vue from 'vue';
  import {get_image_url, get_download_link } from './file-upload.service';

  export default Vue.extend({
    name: 'Preview',
    props: ['id'],
    data() {
      return {
        imageUrl: "",
        loading: true,
        errorMessage: "",
        errorDescription: "",
        hasError: false
      }
    },

    methods: {
      downloadImage: function () {
        window.open(get_download_link(this.id));
      }
    },

    created: function () {
      get_image_url(this.id).then(r => {
        this.imageUrl = r.data.src;
        console.log(r);
        this.loading = false;
      }).catch(e => {
        this.hasError = true;
        this.errorMessage = e.response.statusText;
        this.errorDescription = e.response.data.message
        this.loading = false;
      })
    }
  })
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.step {
  margin-bottom:20px;
}
.button-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0px;
   }
}

</style>
