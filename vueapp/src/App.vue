<template>
  <div id="app">
    <el-container>
      <el-header></el-header>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
    <!--<img src="./assets/logo.png">-->

  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'app'
})
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
