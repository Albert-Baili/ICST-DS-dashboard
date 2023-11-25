<template>
  <div>
    <ItemWrap class="contetn_left-top contetn_lr-item" title="设备资产监测">
      <LeftTop />
    </ItemWrap>
    <ItemWrap class="contetn_left-center contetn_lr-item" title="设备提醒">
      <LeftBottom />
    </ItemWrap>
  </div>
</template>

<script>
import LeftTop from './left-top.vue'
import LeftBottom from './left-bottom.vue'
export default {
  components: {
    LeftTop,
    LeftBottom,
  }
}
</script>
<style>
.contetn_lr-item {
  height: 310px;
  padding: 0 10px 16px 10px;
  width: 30%;
}
</style>