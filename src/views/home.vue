<!--
 * @Author: daidai
 * @Date: 2022-01-12 14:23:32
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-09-09 14:47:24
 * @FilePath: \web-pc\src\pages\big-screen\view\home.vue
-->
<template>
  <!-- <div id="index" ref="appRef" class="index_home" :class="{ pageisScale: isScale }"> -->
  <ScaleScreen :width="1920" :height="1080" class="scale-wrap" :selfAdaption="$store.state.setting.isScale">
    <div class="bg">
      <dv-loading v-if="loading">Loading...</dv-loading>
      <div v-else class="host-body">
        <!-- 头部 s -->
        <div class="d-flex jc-center title_wrap">
          <div class="zuojuxing"></div>
          <div class="youjuxing"></div>
          <div class="guang"></div>

          <div class="d-flex jc-center">
            <div class="menu-container">
              <router-link class="menu-title" to="/index"
                :class="{ 'active-link': isCurrentPage('/index'), 'inactive-link': !isCurrentPage('/index') }">大屏首页</router-link>
              <router-link class="menu-title" to="/page1"
                :class="{ 'active-link': isCurrentPage('/page1'), 'inactive-link': !isCurrentPage('/page1') }">数据资产管理</router-link>
              <router-link class="menu-title" to="/page2"
                :class="{ 'active-link': isCurrentPage('/page2'), 'inactive-link': !isCurrentPage('/page2') }">数据安全管理</router-link>
              <router-link class="menu-title" to="/page3"
                :class="{ 'active-link': isCurrentPage('/page3'), 'inactive-link': !isCurrentPage('/page3') }">数据质量管理</router-link>              
              </div>
            <div class="title">
              <span class="title-text">工业互联网数据安全管控平台</span>
            </div>
            <div class="title">
            </div>
          </div>
          <div class="timers">
            {{ dateYear }} {{ dateWeek }} {{ dateDay }} 
            <i class="blq-icon-shezhi02" style="margin-left: 10px" @click="showSetting"></i>
            <i onclick="window.location.href='http://127.0.0.1:5000/manage/index'">后台管理系统</i>
          </div>
        </div>
        <!-- 头部 e-->
        <!-- 内容  s-->
        <router-view>
        </router-view>
        <!-- 内容 e -->
      </div>
    </div>
    <Setting ref="setting" />
  </ScaleScreen>
  <!-- </div> -->
</template>

<script>
import { formatTime } from "../utils/index.js";
import Setting from "./setting.vue";
import ScaleScreen from "@/components/scale-screen/scale-screen.vue";
export default {
  components: { Setting, ScaleScreen },
  data() {
    return {
      timing: null,
      loading: true,
      dateDay: null,
      dateYear: null,
      dateWeek: null,
      weekday: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
    };
  },
  filters: {
    numsFilter(msg) {
      return msg || 0;
    },
  },
  computed: {},
  created() { },
  mounted() {
    this.timeFn();
    this.cancelLoading();
  },
  beforeDestroy() {
    clearInterval(this.timing);
  },
  methods: {
    showSetting() {
      this.$refs.setting.init();
    },
    timeFn() {
      this.timing = setInterval(() => {
        this.dateDay = formatTime(new Date(), "HH: mm: ss");
        this.dateYear = formatTime(new Date(), "yyyy-MM-dd");
        this.dateWeek = this.weekday[new Date().getDay()];
      }, 1000);
    },
    cancelLoading() {
      let timer = setTimeout(() => {
        this.loading = false;
        clearTimeout(timer);
      }, 500);
    },
    isCurrentPage(route) {
      // 使用 this.$route.path 来获取当前路由路径
      return this.$route.path === route;
    }
  },
};
</script>

<style lang="scss">
@import "./home.scss";

.d-flex.jc-center {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  /* 在容器中均匀分布子元素 */
  align-items: center;
  /* 在垂直方向上居中对齐子元素 */
}

.menu-title {
  font-size: 17px;
  margin-left: 10px;
}

.title {
  position: relative;
  left: -200px;
}

/* 当前页面的链接样式 */
.active-link {
  color: rgb(38, 83, 232);
}

/* 其他页面的链接样式 */
.inactive-link {
  color: gray;
}</style>
