<template>
  <div class="contents">
    <div class="contetn_left">
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="敏感数据识别" style="padding: 0 10px 16px 10px">
        <RightBottom />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="脱敏策略统计"
        style="padding: 0 10px 16px 10px; height:280px">
        <test />
      </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item" title="地图测试" style="padding: 0 10px 16px 10px ;height:40%">
        <test2 />
      </ItemWrap>
    </div>
    <div class="contetn_center">
      <dv-border-box-12>
        <tuominList />
      </dv-border-box-12>
    </div>
    <div class="contetn_right"></div>
  </div>
</template>
<script>
import RightBottom from './right-bottom.vue'
import test from './test.vue'
import test2 from './test2.vue'
import tuominList from './tuominList.vue'
export default {
  components: {
    RightBottom,
    test,
    test2,
    tuominList
  }
}
</script>
<style>
.contetn_left,
.contetn_right {
  width: 540px;
  box-sizing: border-box;
  padding: 16px 0;
}
.contetn_lr-item {
  height: 310px;
  padding: 0 10px 16px 10px;
}
.contetn_center {
  width: 720px;
}
</style>