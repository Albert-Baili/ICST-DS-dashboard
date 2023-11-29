<template>
    <div>

        <dv-active-ring-chart :config="config" style="width:300px;height:300px" />


    </div>
</template>
  
<script>
export default {
    components: {},

    data() {
        return {
            config: {
                radius: '40%',
                activeRadius: '45%',
                data: [
                    {
                        name: '掩盖',
                        value: 55
                    },
                    {
                        name: '哈希',
                        value: 120
                    },
                    {
                        name: '映射',
                        value: 78
                    },
                    {
                        name: '关联计算',
                        value: 66
                    },
                    {
                        name: '混合规则',
                        value: 80
                    }
                ]
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