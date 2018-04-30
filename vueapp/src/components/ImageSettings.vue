<template>
  <el-row>
    <el-col :span="12">
      <div style="background: blue">{{ id }}</div>
    </el-col>
    <el-col :span="12">
      <el-row><div style="background: red">asdadasdasdasdasdasdasdasdadadasdasdasd</div></el-row>
      <el-row><div style="background: yellowgreen">asdadasdasdasdasdasdasdasdadadasdasdasd</div></el-row>
      <el-row><div style="background: ivory">asdadasdasdasdasdasdasdasdadadasdasdasd</div></el-row>
      <el-row><div style="background: firebrick">asdadasdasdasdasdasdasdasdadadasdasdasd</div></el-row>

    </el-col>
  </el-row>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'ImageSettings',
  props: ['id'],
  data() {
    return {

    }
  }
})
</script>

