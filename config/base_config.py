# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  


# 基础配置
PLATFORM = "xhs"
KEYWORDS = "#独居女生安全"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持小红书
SORT_TYPE = "popularity_descending"
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持抖音
PUBLISH_TIME_TYPE = 0
CRAWLER_TYPE = "detail"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = True

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json
SAVE_DATA_OPTION = "csv"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 200

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认不开启爬评论
ENABLE_GET_COMMENTS = True

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 200000

XHS_SPECIFIED_NOTE_URL_LIST = ['https://www.xiaohongshu.com/explore/63b042f4000000001f025627?xsec_token=ABIa-9ii1kcVAmop87GYBUowvofPc4duLYoMuOhGiK3fQ=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/62877b93000000002103d8ae?xsec_token=ABoYtDDv43NElP8dIuaOcgxO-G4JumiHNhZUrcA9ZLor8=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6686c021000000000d00eb11?xsec_token=ABaoLpPQjoibOpsCE1HaJLyHfbR4INmqcvR1JYM5c40KA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6419c7d500000000120328a3?xsec_token=ABHTPdxXKUdtY7Pi3jD5_Eb7X_p99XM-Vztf_AB-fwh8I=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/63312fb00000000017020379?xsec_token=ABsRePtTkKtTvaohtsJFc1CAk3B8wPxo9xsg8YjsgTO5g=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65d15e3300000000070073c0?xsec_token=ABXDR4FvbCEeSIy-CbmNfC1K0reWsZAiF_-mEnKDROxrc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/665d5cd3000000001401bb9f?xsec_token=ABXHhVMhcDXSOAKA1zesYUMg_GOM-r0Q8xZBsX8bHqGmI=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64575a2e000000001203da94?xsec_token=ABEaWl47_NiJ4PBTD5nyKIIMqB5KxjRfVcI7Pd6h6fGM0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/647809d80000000013034141?xsec_token=ABKn4ptzjyuo_ms24OHl9EcBWdEo0U6SMHQQ9UBudDfYA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/668fcc2100000000250175f8?xsec_token=ABEBvN6UlBPsXHdQWp0simCK6LNTYhLOsCuVRWMj_X42M=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/628bd30e000000002103ba25?xsec_token=ABY-nIv0onLOmwNcNgGi6L1y6qnOl87_yV2pF1QKXeRA8=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65af8738000000002c03f93e?xsec_token=ABhrzZ3HCBlHqH-Xuy0FW4CRFmziX98tHBOQ007EsDIIo=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/667016c7000000000600717c?xsec_token=AB9Rog0px01-rcX0AfN674MeZFh2P2wmkCF3C0DQre7JQ=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65ae4b2e0000000011002593?xsec_token=ABfN6L-5sskSMmzb3hFqxDdh4ZyCHm1qn1E-8y0AUzGf8=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/656ca70e000000000503898c?xsec_token=ABVEvJTPZT6Ne_oFFT5sIpzCW40RhTt4nB0jLfuHD3ZII=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64f43b42000000001e02f81a?xsec_token=ABGgftWCIjSNhoqWoDlR7-fD0a9LkI4xvaZBQWPgr3YQY=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6603b73c0000000013027335?xsec_token=ABMfx57ZojvkqAjpUysIjnw9WVGuupYi51hZQcFLpq7to=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/62bd2de0000000002103db42?xsec_token=ABAuXekzDDIeCOqoGRUXR_gUEEHjporKWLcvkHK2UGMlI=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/60e3bb53000000000102b3bd?xsec_token=ABbQHrA2ksP8zQhzILUWSZqC2m5-8YB7mGTC20P2xmfnA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64aeb0a50000000015032552?xsec_token=ABrvIPU64OUyH2XKihvsx-7E8p8UsdRGe_iNmKp85tTkQ=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64fe6b74000000001e02f36f?xsec_token=AB_nW40-dJilGvXalLNtDVYtSJfvgb0BghV3wsnlg6Wdw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64954d1200000000140252f5?xsec_token=ABLcoX-VuVK4PDgn3al-gqtuXzMN9wDNZxpLusbxlb6l8=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66b7ad730000000009015137?xsec_token=ABqqZDxjw-X3Zr77exE1807tCQBsIZ913HBmWoWZZOUVU=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6620733500000000010063f6?xsec_token=ABCSuz5JpV5wEtoSnL7n2nGBuQA-pCCbKarwKHyif1ybA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66b84404000000001e01973b?xsec_token=AB1IMewA8oSpWGOqKoIa4eZdObuf73kW50uYGOUJSu8ps=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64faf0b4000000001e021ee9?xsec_token=ABQyiHBSUEBAHtUrGRfVsyiXE_k3OS71JoI1vcsylsVOc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6609725b000000000401b6af?xsec_token=AB3RWzY6rKNjCnlOeTghaEPP_9cYQuUfy-53kRSqbiYMM=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6572c1e0000000003a00af16?xsec_token=ABR1GrAAYyMVQyjimz8iGhaPc0tMKfWQMqB_KE6K2-BZc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65cd91ed000000000b022f8e?xsec_token=ABc7da5rccE-k9Ce2mPxXCB2QDLGR0TUApfSpZQdoqcyk=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64a587450000000015032989?xsec_token=ABG2N1r0NYyuGYpbMetdfH0d69kP5FlQJKYLJOzbj5J-8=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65d9c973000000000b016587?xsec_token=AB-ZhbBvxOCkDektIUvgHJ-1Y5gTC3C6G3GIt1wJGTPMA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66d1ddca000000001d038838?xsec_token=AB8MkQrCfBRf2syENyPxqMagjdhFz_9WArhde5-MfhK6U=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66c0c292000000001e01e63c?xsec_token=ABiDeAKkH7KTpJxuy_0sgAu7b1IiY_aa9Psgwaezknk9Q=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66b3ac320000000025033083?xsec_token=ABWyrejiwEXK-fRdf9oqC_EzXf_X7N1-2-9sKyTSVPbfw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66b5d01c000000000d030e24?xsec_token=ABkdImZX250Yy8fTYULjVZm1RDZ3pBmAYjg8ksR0ViovY=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66bb54e7000000000503ac11?xsec_token=ABvLu1LJy43fIxX1wYvQKXIdUgTKUBw6xkxd2SiBUx0aM=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66bbff58000000001e01e1a2?xsec_token=ABvLu1LJy43fIxX1wYvQKXIanp18ie4XI97zVPjZpp8T0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66b194fd0000000009014c21?xsec_token=AB0mDbeNVvDLjMEh1EtONP2nAlF38BmU1rPrDFKeTkGs0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66d418dc000000001f03b448?xsec_token=AB5iPbPtXPHF9jDGldmzWXL4QQjQng8er2bYeN93ikWew=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66ca79df000000001f01aacc?xsec_token=ABS13EnNSbwKeu32MOLYy0UOz93lvXgTNefhw_AiCUaTI=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66d4818e000000001d0176d1?xsec_token=AB5iPbPtXPHF9jDGldmzWXL_cXb_2ngHH5QU-sRLLlFf0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66c74a12000000001f03e9d0?xsec_token=ABl5_COMKW3duEyUrWYpFpo2LvVRNtPat92OmE0jr8z18=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66ce7fb7000000001d039081?xsec_token=ABgUhO_dkyoDkovv3JEnQc4N2JmuCsjxYK_mZu1E8zytA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64f479ff000000001e028df5?xsec_token=ABGgftWCIjSNhoqWoDlR7-fGsNWhezEPNQaMmvlruEDqo=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65cb5b8d000000000b014877?xsec_token=ABKxAxj9cOR1k6jqbx1nbEILCnvoPEzitrcfbR72vDO14=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/658c26ec000000000f01f187?xsec_token=ABtSImJ5eVbM3v9x8pR5vx3M74bWG56r7yARDPHA4hsNg=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66a5ca03000000000600ec26?xsec_token=ABcFbO1Vwp8LKQvL1wLg63gLqv3kZpfGCFYLHNx7NQaMc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64f722320000000013034b2f?xsec_token=ABBcIBeQELPq7tVYbm0fMu30kHrk712vwAv3E5Eyy4xaE=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66cec383000000001d01a8fd?xsec_token=ABgUhO_dkyoDkovv3JEnQc4HNJOPL0jObrZRZiMWsR4EE=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65015cf7000000001d015264?xsec_token=AB3TwYPAvKoPPgAhlD3Apj4SnwTOs9L_uBdhq8P-dmY5Q=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66cb1d40000000001d01b805?xsec_token=AB6Mgn6BsPz_HixWAR-A5n3Pyv6uWwRs5TF-u77VefJhw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/644531ba00000000070387ce?xsec_token=AB8CO5gFYwrNeqT-ssMyQXwEVykJKxTQhrEYIBek-IdqQ=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6325ef94000000001200d465?xsec_token=ABxCjyZqb7jU6FsBXK9dUA6rCtS593ap3_dsEW3M67bqk=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64622a6c000000001300ea06?xsec_token=ABXog9M6g3bhgxg1M1_sBysr4qRj8_d15QFVZZnFa-heQ=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66653865000000000d00c46c?xsec_token=ABYmfRekWRX7fIIgS6sR_VEkofnU_x-bw3quT5wKgM2yY=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65a4f052000000001d031772?xsec_token=ABG7elYSDkl2OGoc91FywRZGkEJjO8ykGmmm4T76O2Yh4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/647491f10000000027000dbc?xsec_token=ABqMQwTpIepKeTfFd4a821q9zpNHtxtUu935snzCyqQ6o=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64e33892000000000a01b28a?xsec_token=ABd_trLacoTVfzhNFdoJf1PBXWo10JWb9GcAC2gAGqaH0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/61ee6c6d000000000102ae1d?xsec_token=ABOXJCGF3C9q-pAxBRV9gGZV30F0MXEQbrCO23O3L8WeA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/630265fe000000001b02316e?xsec_token=AB3uE407ClWJn2r3vFGMFLyZOjdJDjC-M2yJObESlgQHE=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/627b759f000000000102dc1a?xsec_token=ABQU2DmQgFKrpH0aYJTsNexqvBNZx58vWN6erXh5paMh0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/62a6ea2b000000001b0342cc?xsec_token=ABq6kAGDSX4vGN0n9cLeSjUWBJ9vVWo6gZfxkGGB8i_wE=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6167cb9d000000000102d4eb?xsec_token=AB9wtHK2IsOX5Ek1nzYLxwhrlUbsnq3jV8TQUqTsoo_4w=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6443d6a9000000001303e027?xsec_token=ABPuvU0V9x7a8tp2HZY6c2Ia8n8Tg2ct5IwQ5lbcpByI4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64ef564e000000001e0321f1?xsec_token=ABY4wpTqz5jwKigZIoGRtn8XGkZSG1Ugas61lC85OJfu4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66a7ca4e000000000d033811?xsec_token=ABxuVLyZPUbvaDCCQ0fj5KOe-gnaTkX-4pAHTJFtXQy3g=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66065d2c000000001a00ff19?xsec_token=ABTfPMRZVH4uB9HIdOW3shaMmkH4xvppOyS4S9J8SBd7w=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/643539df0000000011013108?xsec_token=ABlmjkEGWwbXdKFVkaGtvKdadNAUgQ9e2oKq5IRKQZqUw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/612c8614000000002103b4f2?xsec_token=ABpVv83hJf0dJNOS_ykAdF91tNM6NBVJqhdvKnMlTdGMs=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/659d5c330000000018029689?xsec_token=AB4dxrSDKh5mMRY_E_P5OlhZGvdeATP6Wumy4R4uSbNwc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66057819000000000d00e851?xsec_token=ABSfzSOsM6eYNtdhR_ZVppmn5N64DLkQUB7HBBSB598AY=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64dcaf35000000000c03514d?xsec_token=ABmzSDnJFKCUdM05a9C2xoCvHS5ulqDgBnn81gjkIgUs0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66978f7b000000000d00d430?xsec_token=AB9rfcqMS5ogS1Oa8tnminOkMMbiX8QZW1Ak7qTIRqmIE=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65fa3f2400000000140068cc?xsec_token=ABXjiPuz-ntGWmCZc34lg4VijwNt5jWZ1vBuF9CcqJnOs=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65b7484f000000002d00342b?xsec_token=ABnuEHMpFlAL6VztaLDOo8onTOB8ggOwmy1wb09n_MfVw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6209385a0000000021037a71?xsec_token=ABISVO7bw2rrnGD1JOKTZGhLt0TZi-pJ1DjK_hXwlYWY4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64f6a157000000001e03ccc9?xsec_token=AB9lvY-I_ru_tpbXBzYYlCtP8kMxPDqR_RkAAoPX6plF4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6679339e000000001c0343f2?xsec_token=ABtGdzfuc5TuB-i8E2_w8Ubc5W1xxuNgQQNp3ajassL2s=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64d715c4000000000a01bd0e?xsec_token=ABAh9fVIwUO_CklOc31BEovbjCqFhFTs99cU_Mi3uoV2M=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/63356582000000001c031bae?xsec_token=ABAZyYOx2r60vEDqPCVpQ5X-Ac8PO7qaRbi8AUp5DRCg0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6699e3310000000025014260?xsec_token=ABkUBJGucoJtcEZLb56EpjdaBdkR5s0vZDQYOv2kZL8hw=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6426f0e1000000000800fc35?xsec_token=ABfp_ov23Q-UQlZIMqOHONyqXY690h2EhqJ1XtjRE1TDc=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/669e34c20000000027013368?xsec_token=ABsHAB7mfjqcvtDvNav7_wB1r3qlAoJnjDGUUMXEhoVXg=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/63ef4730000000001301722b?xsec_token=ABHQbQDZuRbO2Byg3FCxz0Mo8V5jkBwv5l5ROJTgZ5eJo=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/668bc60a000000002500613b?xsec_token=ABYhpuVOKA6LufNzjjZBvtEHaZeXFv1pUoR6gYQ6rYG5Q=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/660a82a4000000001a017a52?xsec_token=AB65jVM5jlfTMzc4uuZR-9mLhSJqcYeYzqAzYjPSUO_uo=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/64ebca57000000000c036a1e?xsec_token=ABD6Yr3NFKpCWLR1nqy8X2U3WsYGxnu_z7tWYOVeGbWxs=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/669e1e360000000027018761?xsec_token=ABsHAB7mfjqcvtDvNav7_wB5sqoPBYWtBkk0PIxOw_pmY=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/667a603e000000001c0363bb?xsec_token=ABAN3l8yI0bFks8Hds8kLuutSXuEvb8_nXZm5-ZbShgB4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65dec648000000000b00c456?xsec_token=ABdPE6b9Iy8A6OUY1Djwc3wposVpF_dsNcOfJANtjm4GI=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66794d00000000001f007b0b?xsec_token=ABtGdzfuc5TuB-i8E2_w8UbRyYtNbCuhzXpCWSgk_wOeM=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66a9cea7000000000600e94a?xsec_token=ABBXATrn20-yqLxgWP2FOSmfFt06MEN4nEgxKpxlaP0MA=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66cc3296000000001f03e535?xsec_token=ABVC1JR71Y-kU9XAIuBiegSSr2kK3EjV1wi7mrtcG8-cM=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/66d3e086000000001d01487e?xsec_token=AB9HbTAOB0mXtKWIeEl8DYt85TqbmstvLd087ffed6L8Y=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65eb36fd0000000004003acb?xsec_token=ABTgGRWUkkrRcx22hVq9AiEL2OQm4tkSFhJ4DV_qFkcY0=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6684fd130000000005007b5e?xsec_token=ABfD8uBL2iwNcsGIeQe0V_7_tCVOf3NZ8521cNAZYg2Q4=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/6363106f000000000801142f?xsec_token=ABFznfKBT_S-Vn4aLJjRBJhzQ864XAI9ycTGe9NPQG4tg=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/61ac8507000000002103f296?xsec_token=ABiKkrMb8Y93rrlIfNwXKonIbzsJGQLVuc647qHdbiUpk=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/63520ded000000001402afce?xsec_token=ABxNakP0soEzz5yUN8vKJvWL89TMBltMMwq5kWDdFXZQM=&xsec_source=pc_search', 'https://www.xiaohongshu.com/explore/65eb06a0000000000b00fab0?xsec_token=ABTgGRWUkkrRcx22hVq9AiEHY6m0WKHzotzsKmjpeJ8j4=&xsec_source=pc_search']

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233"
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = [
    "3xf8enb8dbj6uig",
    "3x6zz972bchmvqe"
]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定weibo创作者ID列表
WEIBO_CREATOR_ID_LIST = [
    "5533390220",
    # ........................
]

# 指定贴吧需要爬取的帖子列表
TIEBA_SPECIFIED_ID_LIST = [

]

# 指定贴吧名称列表，爬取该贴吧下的帖子
TIEBA_NAME_LIST = [
    # "盗墓笔记"
]

TIEBA_CREATOR_URL_LIST = [
    "https://tieba.baidu.com/home/main/?id=tb.1.7f139e2e.6CyEwxu3VJruH_-QqpCi6g&fr=frs",
    # ........................
]

# 指定小红书创作者ID列表
XHS_CREATOR_ID_LIST = [
    "63e36c9a000000002703502b",
    # ........................
]

# 指定Dy创作者ID列表(sec_id)
DY_CREATOR_ID_LIST = [
    "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE",
    # ........................
]

# 指定bili创作者ID列表(sec_id)
BILI_CREATOR_ID_LIST = [
    "20813884",
    # ........................
]

# 指定快手创作者ID列表
KS_CREATOR_ID_LIST = [
    "3x4sm73aye7jq7i",
    # ........................
]

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = True
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    '零几': '年份',  # 将“零几”识别为一个整体
    '高频词': '专业术语'  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"
