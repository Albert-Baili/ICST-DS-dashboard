<!--
 * @Author: daidai
 * @Date: 2022-03-04 09:23:59
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-05-07 11:05:02
 * @FilePath: \web-pc\src\pages\big-screen\view\indexs\index.vue
-->
<template>
  <div class="contents">
    <div class="contetn_left">
      <div class="pagetab">
        <!-- <div class="item">实时监测</div> -->
      </div>
      <ItemWrap class="contetn_left-top contetn_lr-item" title="设备资产监测">
        <LeftTop />

      </ItemWrap>
      <ItemWrap class="contetn_left-center contetn_lr-item" title="设备提醒">
        <LeftBottom />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="数字资产监测" style="padding: 0 10px 16px 10px">
        <LeftCenter />
      </ItemWrap>
    </div>
    <div class="contetn_center">
      <!-- <ItemWrap>
        <div style="height: 60px;">
        </div>
      </ItemWrap> -->
      <dv-border-box-10 class="contetn_center-center">
        <div class="contetn_center-flop-list">
          <p class="flop-list-tittle">今日报警</p>
          <p class="flop-list-tittle"> 设备数量</p>
          <p class="flop-list-tittle">数据总量</p>
          <p class="flop-list-tittle">敏感数据</p>
        </div>
        <div class="contetn_center-flop-list">
          <dv-digital-flop class="contetn_center-flop" :config="config" animationCure="easeOutQuad" animationFrame=50
            style="width:200px;height:50px;" />
          <dv-digital-flop class="contetn_center-flop" :config="config2" style="width:200px;height:50px;" />
          <dv-digital-flop class="contetn_center-flop" :config="config3" style="width:200px;height:50px;" />
          <dv-digital-flop class="contetn_center-flop" :config="config4" style="width:200px;height:50px;" />
        </div>
      </dv-border-box-10>
      <CenterMap class="contetn_center_top" />



      <ItemWrap class="contetn_center-bottom" title="通信信道分析">
        <!-- 安装计划 -->
        <CenterBottom />
      </ItemWrap>
    </div>
    <div class="contetn_right">
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="系统风险监测">
        <RightTop />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="数据脱敏记录" style="padding: 0 10px 16px 10px">
        <RightBottom />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="数据分级分类结果">
        <RightCenter />
      </ItemWrap>
    </div>
  </div>
</template>

<script>
import LeftTop from './left-top.vue'
import LeftCenter from "./left-center.vue";
import LeftBottom from "./left-bottom.vue";
import CenterMap from "./center-map.vue";
import CenterBottom from "./center-bottom.vue";
import RightTop from "./right-top.vue";
import RightCenter from "./right-center.vue";
import RightBottom from "./right-bottom.vue";

export default {
  components: {
    LeftTop,
    LeftCenter,
    LeftBottom,
    CenterMap,
    RightTop,
    RightCenter,
    RightBottom,
    CenterBottom,
  },
  data() {
    return {
      config: {
        number: [1460],
        content: '{nt}条',
      },
      config2: {
        number: [259],
        content: '{nt}个',
      },
      config3: {
        number: [4791],
        content: '{nt}G',
      },
      config4: {
        number: [289],
        content: '{nt}G',
      },
    };
  },
  filters: {
    numsFilter(msg) {
      return msg || 0;
    },
  },
  created() {
  },

  mounted() { },
  methods: {

  },
};
</script>
<style lang="scss" scoped>
// 内容
.contents {

  .contetn_left,
  .contetn_right {
    width: 540px;
    box-sizing: border-box;
    // padding: 16px 0;
  }

  .contetn_center {
    width: 720px;
  }

  //左右两侧 三个块
  .contetn_lr-item {
    height: 310px;
    width: 100%;
  }


  // 中间
  .contetn_center {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    position: relative;
  }

  .contetn_center_top {
    width: 100%;
    height: 400px;
  }

  .contetn_center-bottom {
    height: 230px;
  }

  .contetn_center-center {
    height: 120px;
  }

  .contetn_center-flop {
    border: 5px;
    width: 50%;
  }

  .flop-list-tittle {
    font-size: 25px;
    font-weight: 400;
    letter-spacing: 6px;
    background: linear-gradient(92deg,
        #75a7e4 0%,
        #00eaff 48.8525390625%,
        #01aaff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 10px;

  }

  .contetn_center-flop-list {
    display: flex;
    /* 使用Flex布局 */
    justify-content: space-around;
    /* 在容器中均匀分布子元素 */
    align-items: center;
    /* 在垂直方向上居中对齐子元素 */
    padding: 10px;
  }

  //左边 右边 结构一样
  .contetn_left,
  .contetn_right {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    position: relative;
    width: 30%;
  }
}


@keyframes rotating {
  0% {
    -webkit-transform: rotate(0) scale(1);
    transform: rotate(0) scale(1);
  }

  50% {
    -webkit-transform: rotate(180deg) scale(1.1);
    transform: rotate(180deg) scale(1.1);
  }

  100% {
    -webkit-transform: rotate(360deg) scale(1);
    transform: rotate(360deg) scale(1);
  }
}</style>
