<template>
  <div id="app">
    <el-container>
      <el-header>
        <span style="font-size: 24px; color: #409EFF;">Mozapp - application to create mosaic from photos</span>
      </el-header>
      <el-main>
        <transition name="slide-fade" mode="out-in">
          <router-view></router-view>
        </transition>
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

.slide-fade-enter-active {
  transition: all .2s ease-in;
}
.slide-fade-leave-active {
  transition: all .2s ease-in;
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(100px);
  opacity: 0;
}
</style>
