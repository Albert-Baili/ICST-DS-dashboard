<!--
 * @Author: daidai
 * @Date: 2022-03-01 09:43:37
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-09-09 11:40:22
 * @FilePath: \web-pc\src\pages\big-screen\view\indexs\left-bottom.vue
-->
<template>
  <div v-if="pageflag" class="left_boottom_wrap beautify-scroll-def" :class="{ 'overflow-y-auto': !sbtxSwiperFlag }">
    <component :is="components" :data="list" :class-option="defaultOption">
      <ul class="left_boottom">
        <li class="left_boottom_item" v-for="(item, i) in list" :key="i">
          <span class="orderNum doudong">{{ i + 1 }}</span>
          <div class="inner_right">
            <div class="dibu"></div>
            <div class="flex">
              <div class="info">
                <span class="labels">设备名称：</span>
                <span class="contents zhuyao doudong wangguan">
                  {{ item.devicename }}</span>
              </div>
              <div class="info">
                <span class="labels">IP地址：</span>
                <span class="contents " style="font-size: 12px">
                  {{ item.deviceip }}</span>
              </div>
            </div>

            <span class="types doudong" :class="{
              typeRed: item.onlineState == 0,
              typeGreen: item.onlineState == 1,
            }">{{ item.onlineState == 1 ? "上线" : "下线" }}</span>

            <div class="info addresswrap">
              <span class="labels">MAC地址：</span>
              <span class="contents ciyao" style="font-size: 12px">
                {{ item.devicemac }}</span>
            </div>
          </div>
        </li>
      </ul>
    </component>
  </div>

  <Reacquire v-else @onclick="getData" style="line-height: 200px" />
</template>

<script>
import { currentGET } from "api/modules";
import vueSeamlessScroll from "vue-seamless-scroll"; // vue2引入方式
import Kong from "../../components/kong.vue";
export default {
  components: { vueSeamlessScroll, Kong },
  data() {
    return {
      list: [],
      pageflag: true,
      components: vueSeamlessScroll,
      defaultOption: {
        ...this.$store.state.setting.defaultOption,
        singleHeight: 240,
        limitMoveNum: 5,
        step: 0,
      },
    };
  },
  computed: {
    sbtxSwiperFlag() {
      let sbtxSwiper = this.$store.state.setting.sbtxSwiper;
      if (sbtxSwiper) {
        this.components = vueSeamlessScroll;
      } else {
        this.components = Kong;
      }
      return sbtxSwiper;
    },
  },
  created() {

  },

  mounted() {
    // 在组件创建时发送GET请求
    this.getData();
  },
  methods: {
    // addressHandle(item) {
    //   let name = item.provinceName;
    //   if (item.cityName) {
    //     name += "/" + item.cityName;
    //     if (item.countyName) {
    //       name += "/" + item.countyName;
    //     }
    //   }
    //   return name;
    // },
    getData() {
      this.pageflag = true;
       // this.pageflag =false
       const fixedData = {
        success: true,
        data:[
                {
                  'devicename': 'Personal Computer',
                  'onlineState': 1,
                  'deviceip': '192.168.123.46',
                  'devicemac': '04:7C:16:DC:7A:D6'

                },
                {
                  'devicename': 'CyberTAN Technology',
                  'onlineState': 1,
                  'deviceip': '192.168.123.198',
                  'devicemac': '28:39:26:63:39:9D'

                },
                {
                  'devicename': 'Micro-Star Intl',
                  'onlineState': 1,
                  'deviceip': '192.168.123.45',
                  'devicemac': '24:7C:26:DC:7A:A6'

                },
                {
                  'devicename': 'Beijing Xiaomi Mobile Software',
                  'onlineState': 1,
                  'deviceip': '192.168.123.1',
                  'devicemac': 'D4:DA:21:0B:89:4F'

                },
                {
                  'devicename': 'Ruijie Networks',
                  'onlineState': 1,
                  'deviceip': '192.168.24.1',
                  'devicemac': '58:69:6C:4C:47:53'

                },
                {
                  'devicename': 'CyberTAN Technology',
                  'onlineState': 1,
                  'deviceip': '192.168.24.29',
                  'devicemac': '45:C0:7D:38:11:6D'
                },
                {                    
                  'devicename': 'Beijing Xiaomi Mobile Software',
                  'onlineState': 1,
                  'deviceip': '192.168.24.168',
                  'devicemac': "E4:9D:31:C1:24:44"
                },
                {
                  'devicename': 'Ruijie Networks',
                  'onlineState': 1,
                  'deviceip': '192.168.24.60',
                  'devicemac': '41:E7:E8:BB:BC:B2'
                },
                {
                  'devicename': 'Microsoft',
                  'onlineState': 1,
                  'deviceip': '192.168.24.120',
                  'devicemac': '06:58:24:8C:59:67'
                },
                {
                  'devicename': 'Microsoft',
                  'onlineState': 1,
                  'deviceip': '192.168.24.11',
                  'devicemac': '7E:1D:A8:51:BD:B3'
                },
                {
                  'devicename': 'CyberTAN Technology',
                  'onlineState': 1,
                  'deviceip': '192.168.24.23',
                  'devicemac': '45:BF:0C:39:77:93'
                },
                {
                  'devicename': 'CyberTAN Technology',
                  'onlineState': 1,
                  'deviceip': '192.168.24.195',
                  'devicemac': 'C3:75:84:F3:47:A7'
                },
                {
                  'devicename': 'Ruijie Networks',
                  'onlineState': 1,
                  'deviceip': '192.168.24.6',
                  'devicemac': '1D:83:E4:5B:21:98'
                },
                {
                  'devicename': 'Ruijie Networks',
                  'onlineState': 1,
                  'deviceip': '192.168.24.77',
                  'devicemac': '6F:71:53:8C:FB:AA'
                },
                {
                  'devicename': 'Ruijie Networks',
                  'onlineState': 1,
                  'deviceip': '192.168.24.103',
                  'devicemac': '91:8A:2C:8D:93:5E'
                },
                {
                  'devicename': 'Beijing Xiaomi Mobile Software',
                  'onlineState': 1,
                  'deviceip': '192.168.24.18',
                  'devicemac': '02:DF:0D:B9:EA:D7'
                },
                {   
                  'devicename': 'CyberTAN Technology',
                  'onlineState': 1,
                  'deviceip': '192.168.24.122',
                  'devicemac': 'F3:79:6B:EB:16:55'
                },
                
            ],
          msg: '出错啦！',
       }

         if (fixedData.success) {
           // this.countUserNumData = res.data;
           // this.list = res.data.list;
           this.list = fixedData.data
          let timer = setTimeout(() => {
            clearTimeout(timer);
            this.defaultOption.step =
              this.$store.state.setting.defaultOption.step;
          }, this.$store.state.setting.defaultOption.waitTime);
        } else {
          this.pageflag = false;
          this.$Message({
            text: fixedData.msg,
            type: "warning",
          });
        }

    },
  },
};
</script>
<style lang='scss' scoped>
.left_boottom_wrap {
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.doudong {
  //  vertical-align:middle;
  overflow: hidden;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  backface-visibility: hidden;
}

.overflow-y-auto {
  overflow-y: auto;
}

.left_boottom {
  width: 100%;
  height: 100%;

  .left_boottom_item {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
    font-size: 14px;
    margin: 10px 0;

    .orderNum {
      margin: 0 16px 0 -20px;
    }

    .info {
      margin-right: 10px;
      display: flex;
      align-items: center;
      color: #fff;

      .labels {
        flex-shrink: 0;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.6);
      }

      .zhuyao {
        color: $primary-color;
        font-size: 12px;
      }

      .ciyao {
        color: rgba(255, 255, 255, 0.8);
      }

      .warning {
        color: #e6a23c;
        font-size: 15px;
      }
    }

    .inner_right {
      position: relative;
      height: 100%;
      width: 380px;
      flex-shrink: 0;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;

      .dibu {
        position: absolute;
        height: 2px;
        width: 104%;
        background-image: url("../../assets/img/zuo_xuxian.png");
        bottom: -10px;
        left: -2%;
        background-size: cover;
      }

      .addresswrap {
        width: 100%;
        display: flex;
        margin-top: 8px;
      }
    }

    .wangguan {
      color: #1890ff;
      font-weight: 900;
      font-size: 15px;
      width: 80px;
      flex-shrink: 0;
    }


    .time {
      font-size: 12px;
      // color: rgba(211, 210, 210,.8);
      color: #fff;
    }

    .address {
      font-size: 12px;
      cursor: pointer;
      // @include text-overflow(1);
    }

    .types {
      width: 30px;
      flex-shrink: 0;
    }

    .typeRed {
      color: #fc1a1a;
    }

    .typeGreen {
      color: #29fc29;
    }
  }
}
</style>