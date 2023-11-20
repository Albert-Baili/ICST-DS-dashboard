<template>
<div>
    <ItemWrap class="contetn_left-bottom contetn_lr-item" title="敏感数据识别" style="padding: 0 10px 16px 10px">
        <RightBottom />
      </ItemWrap>
</div>
</template>
<script>
import RightBottom from './right-bottom.vue'
export default {
  components: {
    RightBottom,
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