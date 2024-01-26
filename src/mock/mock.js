import Mock from 'mockjs'
//延时200-600毫秒请求到数据
Mock.setup({
    timeout: '200-600'
})

const Random = Mock.Random;
// 数字资产监测
function countUserNum() {
    const a = Mock.mock({
        success: true,
        data: {
            offlineNum:'@integer(1, 100)',
            lockNum: '@integer(1, 10)',
            totalNum:218
        }
    })
    a.data.onlineNum=a.data.totalNum-a.data.offlineNum-a.data.lockNum
    return a
}

// 接口，第一个参数url，第二个参数请求类型，第三个参数响应回调
Mock.mock(new RegExp('countUserNum'), 'get', countUserNum)

// /设备总览 
function countDeviceNum() {
    const a = Mock.mock({
        success: true,
        data: {
            alarmNum: '@integer(50, 200)',
            offlineNum: '@integer(0, 50)',
            totalNum:'@integer(1000,3000)',
        }
    })
    a.data.onlineNum=a.data.totalNum-a.data.offlineNum


    return a
}

Mock.mock(new RegExp('countDeviceNum'), 'get', countDeviceNum)

// /设备总览 

function sbtx() {
    const a = Mock.mock({
        success: true,
        data: {
            "list|20": [
                {
                    provinceName: "@province()",
                    cityName: '@city()',
                    countyName: "@county()",
                    createTime: "@datetime('yyyy-MM-dd HH:mm:ss')",
                    deviceId: "6c512d754bbcd6d7cd86abce0e0cac58",
                    "gatewayno|+1": 10000,
                    "onlineState|1": [0, 1],
                }
            ]
        }
    })
    return a
}

// // 定义随机生成IP地址的函数
// function randomIP() {
//     const ipSegments = [];
//     for (let i = 0; i < 4; i++) {
//         ipSegments.push(Mock.mock('@integer(0, 255)'));
//     }
//     return ipSegments.join('.');
// }

// // 定义随机生成MAC地址的函数
// function randomMAC() {
//     const macSegments = [];
//     for (let i = 0; i < 6; i++) {
//         macSegments.push(Mock.mock('@string("0123456789ABCDEF", 2)'));
//     }
//     return macSegments.join(':');
// }
// function sbtx() {
//     const deviceNames = [
//         "Beijing Xiaomi Mobile Software",
//         "Personal Computer",
//         "CyberTAN Technology",
//         "Micro-Star Intl",
//         "Microsoft",
//         "Ruijie Networks",
//         "Huawei Technology",
//     ];
//     const a = Mock.mock({
//         success: true,
//         data: {
//             "list|20": [
//                 {
//                     "devicename": function () {
//                             return Mock.mock('@pick(' + JSON.stringify(deviceNames) + ')');
//                         },
//                     "deviceip": function(){
//                         const ipSegments = [];
//                         for (let i = 0; i < 4; i++) {
//                             ipSegments.push(Mock.mock('@integer(0, 255)'));
//                         }
//                         return ipSegments.join('.');
//                     },
//                     "devicemac": function(){
//                         const macSegments = [];
//                         for (let i = 0; i < 6; i++) {
//                             macSegments.push(Mock.mock('@string("0123456789ABCDEF", 2)'));
//                         }
//                         return macSegments.join(':');
//                     },
//                     "onlineState|1": 1,
//                 }
//             ]
//         }
//     })
//     return a
// }

Mock.mock(new RegExp('sbtx'), 'get', sbtx)



//中间地图

function centermap(options) {
    let params = parameteUrl(options.url)
    if (params.regionCode && params.regionCode != 'china') {
        const a = Mock.mock({
            success: true,
            data: {
                "dataList|30": [
                    {
                        name: "@city()",
                        value: '@integer(1, 1000)'
                    }
                ],
                regionCode: params.regionCode,//-代表中国
            }
        })
        return a
    } else {
        const a = Mock.mock({
            success: true,
            data: {
                "dataList|8": [
                    {
                        name: "@province()",
                        value: '@integer(1, 1000)'
                    }
                ],
                regionCode: 'china',
            }
        })
        return a
    }

}

Mock.mock(new RegExp('centermap'), 'get', centermap)

// 报警次数

function alarmNum() {
    const a = Mock.mock({
        success: true,
        data: {
            dateList:['2022-11', '2022-12', '2023-01', '2023-02', '2023-03',"2023-04"],
            "numList|6":[
                '@integer(0, 1000)'
            ],
            "numList2|6":[
                '@integer(0, 1000)'
            ]
        }
    })
    return a
}
Mock.mock(new RegExp('alarmNum'), 'get', alarmNum)

// 实时预警

function ssyj() {
    const a = Mock.mock({
        success: true,
        data: {
            "list|40":[{
                alertdetail: "@csentence(5,10)",
                "alertname|1": ["水浸告警","各种报警"],
                alertvalue: "@float(60, 200)",
                createtime: "2022-04-19 08:38:33",
                deviceid: null,
                "gatewayno|+1": 10000,
                phase: "A1",
                sbInfo: "@csentence(10,18)",
                "terminalno|+1": 100,
                provinceName: "@province()",
                cityName: '@city()',
                countyName: "@county()",
            }],
            
        }
    })
    return a
}
Mock.mock(new RegExp('ssyj'), 'get', ssyj)
//安装计划 
function installationPlan() {
    let num=  RandomNumBoth(26,32);
    const a = Mock.mock({
        ["category|"+num]:["@datetime('MM-dd')"],
        ["barData|"+num]:["@integer(10, 100)"],
    })
    let lineData=[],rateData=[];
    for (let index = 0; index < num; index++) {
        let lineNum = Mock.mock('@integer(0, 100)')+a.barData[index]
        lineData.push(lineNum)
        let rate = a.barData[index] / lineNum;
        rateData.push((rate*100).toFixed(0))
    }
    a.lineData=lineData
    a.rateData=rateData
    return {
        success: true,
        data:a
    }
}
Mock.mock(new RegExp('installationPlan'), 'get', installationPlan)




//报警排名 
function ranking() {
    const cities = ["传感器数据", "工业生产数据", "用户数据", "操作数据", "日志数据", "质量数据", "状态数据", "工业环境数据", "供应链数据", "市场数据"];

   //多生成几个避免重复 重复会报错
  let num =Mock.mock({"list|48":[{ value:"@integer(50,1000)",name:function() {
    // 从指定的城市列表中随机选择一个
    return cities[Math.floor(Math.random() * cities.length)];
}}]}).list
//   console.log(num);
  let newNum =[],numObj={}
  num.map(item=>{
    if(!numObj[item.name] && newNum.length<8){
        numObj[item.name] =true
        newNum.push(item)
    }
  })
  let arr = newNum.sort((a,b)=>{
    return b.value-a.value
  })
  let a ={
      success:true,
      data:arr
  }
  return a
}
Mock.mock(new RegExp('ranking'), 'get', ranking)
/**
 * @description: min ≤ r ≤ max  随机数
 * @param {*} Min
 * @param {*} Max
 * @return {*}
 */
function RandomNumBoth(Min,Max){
    var Range = Max - Min;
    var Rand = Math.random();
    var num = Min + Math.round(Rand * Range); //四舍五入
    return num;
}
/**
 * @description: 获取路径参数
 * @param {*} url
 * @return {*}
 */
function parameteUrl(url) {
    var json = {}
    if (/\?/.test(url)) {
        var urlString = url.substring(url.indexOf("?") + 1);
        var urlArray = urlString.split("&");
        for (var i = 0; i < urlArray.length; i++) {
            var urlItem = urlArray[i];
            var item = urlItem.split("=");
            console.log(item);
            json[item[0]] = item[1];
        }
        return json;
    }
    return {};
}
