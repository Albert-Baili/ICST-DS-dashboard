<template>
  <div class="centerRight2">
    <div class="bg-color-black">
      <div class="d-flex pt-2 pl-2">
        <span>
          <i class="iconfont icon-vector" />
        </span>
        <div class="d-flex">
          <span class="fs-xl text mx-2">数据访问记录</span>
        </div>
      </div>
      <div class="d-flex mt-1 jc-center body-box">
        <dv-scroll-board class="dv-scr-board" :config="config" />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, reactive } from 'vue'
export default defineComponent({
  setup() {
    const config = reactive({
      header: ['数据', '级别', '访问者'],
      data: [
        ['数据1', '生产-1', "<span  class='colorGrass'>admin</span>"],
        ['数据2', '生产-2', "<span  class='colorRed'>admin</span>"],
        ['数据3', '生产-3', "<span  class='colorGrass'>user-01</span>"],
        ['数据4', '运维-1', "<span  class='colorGrass'>admin</span>"],
        ['数据5', '管理-1', "<span  class='colorGrass'>user-01</span>"],
        ['数据6', '研发-3', "<span  class='colorGrass'>user-02</span>"],
        ['数据7', '运维-3', "<span  class='colorGrass'>user-01</span>"],
        ['数据8', '研发-2', "<span  class='colorRed'>unknow</span>"],
        ['数据9', '研发-3', "<span  class='colorRed'>unknow</span>"],
        ['数据10', '管理-1', "<span  class='colorGrass'>admin</span>"]
      ],
      rowNum: 7, //表格行数
      headerHeight: 35,
      headerBGC: '#0f1325', //表头
      oddRowBGC: '#0f1325', //奇数行
      evenRowBGC: '#171c33', //偶数行
      index: true,
      columnWidth: [50],
      align: ['center']
    })
    return { config }
  }
})
</script>

<style lang="scss" scoped>
$box-height: 410px;
$box-width: 300px;
.centerRight2 {
  padding: 16px;
  padding-top: 20px;
  height: $box-height;
  width: $box-width;
  border-radius: 5px;
  .bg-color-black {
    height: $box-height - 30px;
    border-radius: 10px;
  }
  .text {
    color: #c3cbde;
  }
  .body-box {
    border-radius: 10px;
    overflow: hidden;
    .dv-scr-board {
      width: 270px;
      height: 340px;
    }
  }
}
</style>
