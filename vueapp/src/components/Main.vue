<template>
  <div>
    <el-row type="flex" justify="space-between">
      <el-col :span="11">
        <el-row type="flex" justify="center">
          <img width="100%" height="100%" v-if="imageData.length > 0" :src="imageData">
          <i v-else class="el-icon-picture-outline" style="font-size: 100px;"></i>
        </el-row>
        <el-row type="flex" justify="center">
          <form enctype="multipart/form-data" novalidate>
            <input type="file" :name="uploadFieldName" @change="previewImage"
                   accept="image/*" class="input-file">
          </form>
        </el-row>
      </el-col>
      <el-col :span="11"></el-col>
    </el-row>
  </div>
</template>

<script>
  import Vue from 'vue';
  import {upload} from './file-upload.service';

  const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;
  export default Vue.extend({
    name: 'HelloWorld',
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photo',
        imageData: ""
      }
    },
    computed: {
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isSuccess() {
        return this.currentStatus === STATUS_SUCCESS;
      },
      isFailed() {
        return this.currentStatus === STATUS_FAILED;
      }
    },
    methods: {
      reset() {
        // reset form to initial state
        this.currentStatus = STATUS_INITIAL;
        this.uploadedFiles = [];
        this.uploadError = null;
      },
      previewImage(event) {
        let input = event.target;
        if (input.files && input.files[0]) {
          let reader = new FileReader();
          reader.onload = (e) => {
            this.imageData = e.target.result;
          };
          reader.readAsDataURL(input.files[0]);
        }
      }
    },
    mounted() {
      this.reset();
    },
  })
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .input-file {
    padding: 10px 0;
    background: gainsboro;
    width: 100%;
  }
  .el-col {
    border: 1px solid black;
  }
  .el-row {
    border: 1px solid darkgoldenrod;
  }
</style>
