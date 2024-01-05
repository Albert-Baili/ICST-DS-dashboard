<template>
  <div>
    <ItemWrap class="contetn_left-top contetn_lr-item1" title="设备资产监测">
      <LeftTop />
    </ItemWrap>
    <ItemWrap class="contetn_left-center contetn_lr-item1" title="设备提醒">
      <LeftBottom />
    </ItemWrap>
      <ItemWrap class="contetn_left-bottom contetn_lr-item1" title="设备类型分布" style="padding: 0 10px 16px 10px">
        <LeftCenter />
      </ItemWrap>
  </div>
</template>

<script>
import LeftTop from './left-top.vue'
import LeftBottom from './left-bottom.vue'
import LeftCenter from './left-center.vue'
export default {
  components: {
    LeftTop,
    LeftBottom,
    LeftCenter,
  }
}
</script>
<style>
.contetn_lr-item1 {
  height: 310px;
  padding: 0 10px 16px 10px;
  width: 30%;
}
.contetn_left,
.contetn_right {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  width: 30%;
}

</style>