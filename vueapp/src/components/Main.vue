<template>
  <div>
    <!--<router-link to="/preview/2">preview page</router-link>-->
    <el-row class="step">
      <el-col><span style="color:#909399;">Step 1. Choose image and settings</span></el-col>
    </el-row>
    <el-row type="flex" justify="space-around">
      <el-col :span="9">
        <el-card>
          <div slot="header" class="clearfix">
            <span style="color: #409EFF; font-weight: bold;">1. Image is required:</span>
          </div>
          <el-row type="flex" justify="center">
            <img width="100%" height="100%" v-if="imageData.length > 0" :src="imageData">
            <i v-else class="el-icon-picture-outline" style="font-size: 100px;"></i>
          </el-row>
          <el-row type="flex" justify="center">
            <!--<form enctype="multipart/form-data" novalidate>-->
              <input type="file" :name="uploadFieldName" @change="previewImage"
                     accept="image/*" class="input-file">

              <!--<el-upload-->
                <!--ref="form"-->
                <!--drag-->
                <!--action=""-->
                <!--:show-file-list="false"-->
                <!--:on-change="previewImage"-->
                <!--:auto-upload="false">-->
                <!--&lt;!&ndash;<i class="el-icon-upload"></i>&ndash;&gt;-->
                <!--<i class="el-icon-picture-outline" style="font-size: 100px;"></i>-->
                <!--<div class="el-upload__text">Drop file here or <em>click to upload</em></div>-->
                <!--<div class="el-upload__tip" slot="tip">jpg/png files with a size less than 500kb</div>-->
              <!--</el-upload>-->
            <!--</form>-->
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="10">
        <el-card>
          <div slot="header" class="clearfix">
            <span style="color: #409EFF">2. Following settings are optional:</span>
            <!--<el-button style="float: right; padding: 3px 0" type="text">Operation button</el-button>-->
          </div>
          <el-form ref="form" :model="form" label-width="200px">
            <el-form-item label="Output filename">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="Image format">
              <el-select v-model="form.image_format" placeholder="Please select output image format">
                <el-option label="PNG" value="png"></el-option>
                <el-option label="JPEG" value="jpg"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Apply sepia effect">
              <el-switch v-model="form.apply_sepia"></el-switch>
            </el-form-item>
            <el-form-item label="Apply greyscale effect">
              <el-switch v-model="form.apply_greyscale"></el-switch>
            </el-form-item>
            <el-form-item label="Tile style">
              <el-select v-model="form.tile_style" placeholder="Select how tiles shoud be resized">
                <el-option label="Squared" value="1"></el-option>
                <el-option label="Keep ratio of original image" value="2"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Upscale">
              <el-select v-model="form.enlargement" placeholder="You can upscale image to see better details of mosaic">
                <el-option label="None" value="1"></el-option>
                <el-option label="2x" value="2"></el-option>
                <el-option label="3x" value="3"></el-option>
                <el-option label="4x" value="4"></el-option>
                <el-option label="5x" value="5"></el-option>
                <el-option label="6x" value="6"></el-option>
                <el-option label="7x" value="7"></el-option>
                <el-option label="8x" value="8"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="Square size">
              <el-slider
                v-model="form.square_size"
                :min="4"
                :max="100"
                show-input>
              </el-slider>
            </el-form-item>
            <el-form-item label="Tiles per image dimension">
              <!--<el-input-number v-model="form.tiles_per_image_dimension" :min="10" :max="1000"></el-input-number>-->
              <el-slider
                v-model="form.tiles_per_image_dimension"
                :min="10"
                :max="1000"
                show-input>
              </el-slider>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm">Submit</el-button>
              <el-button>Reset</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
      <!--<el-col :span="1"></el-col>-->
    </el-row>
  </div>
</template>

<script>
  import Vue from 'vue';
  import {upload} from './file-upload.service';

//  const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;
  export default Vue.extend({
    name: 'HelloWorld',
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'photo',
        imageFile: null,
        imageData: "",
        imageName: "",

        form: {
          name: '',
          image_format: '',
          apply_sepia: false,
          apply_greyscale: false,
          tile_style: '',
          enlargement: '',
          square_size: 10,
          tiles_per_image_dimension: 100,
        }
      }
    },
    methods: {
      previewImage(event) {
        let input = event.target;
        if (input.files && input.files[0]) {
          this.imageFile = input.files[0];
          let tmp = event.target.value.split('\\');
          this.imageName = tmp[tmp.length-1];
          let reader = new FileReader();
          reader.onload = (e) => {
            this.imageData = e.target.result;
          };
          reader.readAsDataURL(input.files[0]);
        }
      },

      submitForm() {
        this.$refs['form'].validate((valid) => {
          if(valid) {
              let formData = new FormData();
              if(this.imageData.length > 0) {
                formData.set('image', this.imageFile, this.imageName);
              }
              let fields = Object.keys(this.form);
              for(let field of fields){
                if(this.form[field]){
                  formData.set(field, this.form[field]);
                }
              }
              const loading = this.$loading({
                lock: true,
                text: 'Your image is being processed...',
                spinner: 'el-icon-setting',
                background: 'rgba(250, 250, 250, 0.5)',
                customClass: 'my-loader',
              });
              upload(formData).then(r => {
                console.log(r);
                let data = r.data;
                loading.close();
                console.log(data['pk']);
                this.$router.push({name: 'Preview', params: {id: data['pk']}});
              }).catch(e => {
                loading.close();
                console.log(e);
              })
          } else {
            alert("Error!");
            return false;
          }
        });
      }
    },
  })
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .input-file {
    margin-top:20px;
    padding: 10px 10px;
    cursor: pointer;
    /*background: gainsboro;*/
    width: 100%;
    border: 1px dashed #409eff;
    border-radius: 3px;
  }

  .input-file:hover {
    border: 1px dashed #73cfff;
  }
  .el-col {
    /*border: 1px solid black;*/
  }
  .el-row {
    /*border: 1px solid darkgoldenrod;*/
  }

  .el-select, .el-switch{
    width: 100%;
  }

  .step {
    margin-bottom: 20px;
  }

  .my-loader > .el-loading-spinner > .el-icon-setting {
    font-size: 72px;
    -webkit-animation:spin 1.5s linear infinite;
    -moz-animation:spin 1.5s linear infinite;
    animation:spin 1.5s linear infinite;
  }

  .my-loader > .el-loading-spinner > .el-loading-text {
    font-size: 24px;
  }

  @-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }
  @-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } }
  @keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }

</style>
