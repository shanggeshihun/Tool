# _*_coding:utf-8 _*_
# @Time     :2020/10/26 0026   上午 12:23
# @Author   : Antipa
# @File     :resourceStr_classify.py
# @Theme    :PyCharm

type_keywod_dict={
    '钱包（区块链）':'公钥,币种,私钥,节点,钱包,手续费,矿工,账户,托管账户,节点,内存,区块',
    '交易所（虚拟货币）':'持仓,收盘,开盘,手续费,交易所,平仓,K线,挖矿,钱包,充币,提币,银行卡,交易账户,返佣,分红,以太坊,冻结,邀请码,涨跌,区块,白皮书',
    '钱包+手机银行':'持卡人证件号|持卡人身份证号|身份证,预留手机,银行理财,借记卡,签约账户,银行卡|银行卡号|银行卡管理|绑定银行卡号,储蓄卡,提现,转账,银行账号,银行预留|绑定手机|预留手机,云闪付,身份证背面,跨行转账,我的贷款,安全键盘,指纹识别,储蓄账户,收款,支付,限额,转账,快捷支付,手机银行,网上银行,刷卡交易,POS机,信用卡,持卡人,磁条卡,日限额,月限额',
    '贷款+p2p':'已还金额, 提前还款, 担保人|保险人, 车押标, 待收金额, 银行托管, 出借, 房押标, 已还期数, 收益率, 已垫付, 银行存管|存管账户|存管银行, 逾期|逾期罚息|逾期天数|逾期金额, 等额本息, 贷款, 等额本金, 还款日|还款利息|还款计划|还款方式, 待放款, 还款中,投标|散标, 分期金额, 担保标, 债权|债权转让, 存管账户|银行存管|存管银行, 账单利息, 期数, 年化收益, 利息|利息总额|利息复投, 银行卡, 在投金额|投资, 信用标, 还款本金|本金, 冻结|冻结金额, 持卡人签名, 年利率|收益|回报率|年化利率',
    '保险+理财':'赔案金额,理赔,保单,保险人,保费,续保,保险,超速,事故,投标,回款,银行存管|存管账户|存管银行,预留手机,理赔,债权原价,加息,保险,还款日|还款利息|还款计划|还款方式,收款账户,金融资产,银行流水,金融资产,私募,公募,调仓,基金,资金监管',
    '区块链挖矿':'邀请人|邀请码,交易哈希,矿机,节点,静态收益,直推加速,收币,提币,算力,提币,邀请码,挂单,充币,开户,USDT,持币生息,年化收益,分红,结息,认证,认购,释放,锁仓,转账,兑换,转锁,数字资产,充币,糖果',
    '股票+期货+贵金属':'赚钱,散户,分红,K线,跌停,涨停,港股,美股,A股,中概股,抄底,轻仓,大盘云图,持仓,平仓,开仓,交仓,期货,开户,追缴,私募,股票,资产负债,分红,期货,换手率,市盈率,债券,黄金,白银,贵金属,挂单',
    '区块链理财':'算力,智能合约,挖矿,区块,已放款,已认证,已还款,白皮书,币圈,币种列表,白皮书,收益曲线,兑换,USDT,冲币,提币,持币,增仓,做空,溢价,短线掘金,盯盘',
    '系统办公+生活服务':'采购商,库存,销售,客户,利润,出纳,资产负债,仓管,利润表,供应商,代理商,商圈,身份验证,发票抬头,经销商,招商,批发',
    '社交聊天':'禁言,群管理,退群|退出群,群公告,群收费,群助手,群聊,群号,群设置,工会,认证,管理员,玩伴,周榜,日榜,连麦,打赏,贡献榜,视频聊,语音聊,粉丝,师徒,约聊,交友',
    '生活服务':'物业缴费,业主,燃气费,电费,水费,小区,押金,租赁,租住,合同,租金,司机,预约专享,呼叫出租车,联系师傅,乘客,行程已关闭,里程费,调节费,取消叫车,调度费,顺风车',
    '隐私生活':'拍摄,相册,拍照,自拍,相机,滤镜,重新拍照',
    '虚拟货币+区块链游戏':'活跃度,糖果,卷轴,交易手续费,实名认证,世界|鼠|牛|虎|兔|龙|蛇|马|羊|猴|鸡|狗|猪|鱼|猫|宠|汪|喵|养,区块',
    '零撸资金盘':'分红|佣金,分红羊|分红龙,永久分红',
    '电商购物+直播':'缴纳,权益金,升级,现金券,分红,引荐,打赏,主播榜'
}

keyword_list=[]
for k,v in type_keywod_dict.items():
    keyword_list.extend(v.split(','))
keyword_set=set(keyword_list)
print(keyword_set)

for kw in keyword_set:
    print(kw.strip())