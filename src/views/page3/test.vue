<!--
 * @Author: daidai
 * @Date: 2022-03-01 15:27:58
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-05-07 11:24:14
 * @FilePath: \web-pc\src\pages\big-screen\view\indexs\right-center.vue
-->
<template>
    <div>
        <dv-capsule-chart :config="config" style="width:100%;height:200px" />
    </div>
</template>
  
<script>
export default {
    components: {},

    data() {
        return {
            config: {
                data: [
                    {
                        name: '哈希',
                        value: 167
                    },
                    {
                        name: '掩盖',
                        value: 123
                    },
                    {
                        name: '映射',
                        value: 98
                    },
                    {
                        name: '关联计算',
                        value: 75
                    },
                    {
                        name: '混合规则',
                        value: 66
                    },
                ],
                colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
                unit: '字段数'
            },
            
           
        }
    },
    computed: {

    },
    created() {
        this.getData()
    },

    mounted() { },
    methods: {
        getData() {

        },
    },
};
</script>
<style></style>