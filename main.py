from enum import Enum, unique



@unique
class EDiagrams(Enum):
    Kun = 0b000   # 坤
    Gen = 0b001   # 艮
    Kan = 0b010   # 坎
    Xun = 0b011   # 巽
    Zhen = 0b100  # 震
    Li = 0b101    # 离
    Dui = 0b110   # 兑
    Qian = 0b111  # 乾


#纯卦数据结构
class DiagramInfo:
    def __init__(self, *, name, meaning, description):
        self.name = name
        self.meaning = meaning
        self.description = description

    def __repr__(self):
        return f"DiagramInfo(name='{self.name}', meaning='{self.meaning}', description='{self.description}')"


# 使用类 DiagramInfo 存储八卦信息，每个参数一行
diagrams_info = {
    EDiagrams.Kun: DiagramInfo(
        name="坤",
        meaning="地",
        description="坤卦象征地，柔顺，厚德。"
    ),
    EDiagrams.Gen: DiagramInfo(
        name="艮",
        meaning="山",
        description="艮卦象征山，止息，稳定。"
    ),
    EDiagrams.Kan: DiagramInfo(
        name="坎",
        meaning="水",
        description="坎卦象征水，险难，智慧。"
    ),
    EDiagrams.Xun: DiagramInfo(
        name="巽",
        meaning="风",
        description="巽卦象征风，顺从，扩散。"
    ),
    EDiagrams.Zhen: DiagramInfo(
        name="震",
        meaning="雷",
        description="震卦象征雷，动荡，创新。"
    ),
    EDiagrams.Li: DiagramInfo(
        name="离",
        meaning="火",
        description="离卦象征火，光明，文明。"
    ),
    EDiagrams.Dui: DiagramInfo(
        name="兑",
        meaning="泽",
        description="兑卦象征泽，喜悦，柔和。"
    ),
    EDiagrams.Qian: DiagramInfo(
        name="乾",
        meaning="天",
        description="乾卦象征天，刚健，创造。"
    )
}

class SixtyFourDiagramInfo:
    def __init__(self, *, name, statement, meaning, description):
        self.name = name
        self.statement = statement  # 卦辞
        self.meaning = meaning      # 含义
        self.description = description

    def __repr__(self):
        return (f"SixtyFourDiagramInfo(name='{self.name}', "
                f"statement='{self.statement}', meaning='{self.meaning}', "
                f"description='{self.description}')")


#结合上下纯卦获得六十四卦的二进制
def combineDiagrams(shang, xia):
    return (xia.value << 3) | shang.value


class ESixtyFourDiagrams(Enum):
    Qian_Qian = combineDiagrams(EDiagrams.Qian, EDiagrams.Qian)   # 乾为天
    Kun_Kun = combineDiagrams(EDiagrams.Kun, EDiagrams.Kun)       # 坤为地
    Kan_Zhen = combineDiagrams(EDiagrams.Kan, EDiagrams.Zhen)     # 水雷屯
    Gen_Kan = combineDiagrams(EDiagrams.Gen, EDiagrams.Kan)       # 山水蒙
    Kan_Qian = combineDiagrams(EDiagrams.Kan, EDiagrams.Qian)     # 水天需
    Qian_Kan = combineDiagrams(EDiagrams.Qian, EDiagrams.Kan)     # 天水讼
    Kun_Kan = combineDiagrams(EDiagrams.Kun, EDiagrams.Kan)       # 地水师
    Kan_Kun = combineDiagrams(EDiagrams.Kan, EDiagrams.Kun)       # 水地比
    Xun_Qian = combineDiagrams(EDiagrams.Xun, EDiagrams.Qian)     # 风天小畜
    Qian_Dui = combineDiagrams(EDiagrams.Qian, EDiagrams.Dui)     # 天泽履
    Kun_Qian = combineDiagrams(EDiagrams.Kun, EDiagrams.Qian)     # 地天泰
    Qian_Kun = combineDiagrams(EDiagrams.Qian, EDiagrams.Kun)     # 天地否
    Qian_Li = combineDiagrams(EDiagrams.Qian, EDiagrams.Li)       # 天火同人
    Li_Qian = combineDiagrams(EDiagrams.Li, EDiagrams.Qian)       # 火天大有
    Kun_Gen = combineDiagrams(EDiagrams.Kun, EDiagrams.Gen)       # 地山谦
    Zhen_Kun = combineDiagrams(EDiagrams.Zhen, EDiagrams.Kun)     # 雷地豫
    Dui_Zhen = combineDiagrams(EDiagrams.Dui, EDiagrams.Zhen)     # 泽雷随
    Gen_Xun = combineDiagrams(EDiagrams.Gen, EDiagrams.Xun)       # 山风蛊
    Kun_Dui = combineDiagrams(EDiagrams.Kun, EDiagrams.Dui)       # 地泽临
    Xun_Kun = combineDiagrams(EDiagrams.Xun, EDiagrams.Kun)       # 风地观
    Li_Zhen = combineDiagrams(EDiagrams.Li, EDiagrams.Zhen)       # 火雷噬嗑
    Gen_Li = combineDiagrams(EDiagrams.Gen, EDiagrams.Li)         # 山火贲
    Gen_Kun = combineDiagrams(EDiagrams.Gen, EDiagrams.Kun)       # 山地剥
    Kun_Zhen = combineDiagrams(EDiagrams.Kun, EDiagrams.Zhen)     # 地雷复
    Qian_Zhen = combineDiagrams(EDiagrams.Qian, EDiagrams.Zhen)   # 天雷无妄
    Gen_Qian = combineDiagrams(EDiagrams.Gen, EDiagrams.Qian)     # 山天大畜
    Gen_Zhen = combineDiagrams(EDiagrams.Gen, EDiagrams.Zhen)     # 山雷颐
    Dui_Xun = combineDiagrams(EDiagrams.Dui, EDiagrams.Xun)       # 泽风大过
    Kan_Kan = combineDiagrams(EDiagrams.Kan, EDiagrams.Kan)       # 坎为水
    Li_Li = combineDiagrams(EDiagrams.Li, EDiagrams.Li)           # 离为火
    Dui_Gen = combineDiagrams(EDiagrams.Dui, EDiagrams.Gen)       # 泽山咸
    Zhen_Xun = combineDiagrams(EDiagrams.Zhen, EDiagrams.Xun)     # 雷风恒
    Qian_Gen = combineDiagrams(EDiagrams.Qian, EDiagrams.Gen)     # 天山遁
    Zhen_Qian = combineDiagrams(EDiagrams.Zhen, EDiagrams.Qian)   # 雷天大壮
    Li_Kun = combineDiagrams(EDiagrams.Li, EDiagrams.Kun)         # 火地晋
    Kun_Li = combineDiagrams(EDiagrams.Kun, EDiagrams.Li)         # 地火明夷
    Xun_Li = combineDiagrams(EDiagrams.Xun, EDiagrams.Li)         # 风火家人
    Li_Dui = combineDiagrams(EDiagrams.Li, EDiagrams.Dui)         # 火泽睽
    Kan_Gen = combineDiagrams(EDiagrams.Kan, EDiagrams.Gen)       # 水山蹇
    Zhen_Kan = combineDiagrams(EDiagrams.Zhen, EDiagrams.Kan)     # 雷水解
    Gen_Dui = combineDiagrams(EDiagrams.Gen, EDiagrams.Dui)       # 山泽损
    Xun_Zhen = combineDiagrams(EDiagrams.Xun, EDiagrams.Zhen)     # 风雷益
    Dui_Qian = combineDiagrams(EDiagrams.Dui, EDiagrams.Qian)     # 泽天夬
    Qian_Xun = combineDiagrams(EDiagrams.Qian, EDiagrams.Xun)     # 天风垢
    Dui_Kun = combineDiagrams(EDiagrams.Dui, EDiagrams.Kun)       # 泽地萃
    Kun_Xun = combineDiagrams(EDiagrams.Kun, EDiagrams.Xun)       # 地风升
    Dui_Kan = combineDiagrams(EDiagrams.Dui, EDiagrams.Kan)       # 泽水困
    Kan_Xun = combineDiagrams(EDiagrams.Kan, EDiagrams.Xun)       # 水风井
    Dui_Li = combineDiagrams(EDiagrams.Dui, EDiagrams.Li)         # 泽火革
    Li_Xun = combineDiagrams(EDiagrams.Li, EDiagrams.Xun)         # 火风鼎
    Zhen_Zhen = combineDiagrams(EDiagrams.Zhen, EDiagrams.Zhen)   # 震为雷
    Gen_Gen = combineDiagrams(EDiagrams.Gen, EDiagrams.Gen)       # 艮为山
    Xun_Gen = combineDiagrams(EDiagrams.Xun, EDiagrams.Gen)       # 风山渐
    Zhen_Dui = combineDiagrams(EDiagrams.Zhen, EDiagrams.Dui)     # 雷泽归妹
    Zhen_Li = combineDiagrams(EDiagrams.Zhen, EDiagrams.Li)       # 雷火丰
    Li_Gen = combineDiagrams(EDiagrams.Li, EDiagrams.Gen)         # 火山旅
    Xun_Xun = combineDiagrams(EDiagrams.Xun, EDiagrams.Xun)       # 巽为风
    Dui_Dui = combineDiagrams(EDiagrams.Dui, EDiagrams.Dui)       # 兑为泽
    Xun_Kan = combineDiagrams(EDiagrams.Xun, EDiagrams.Kan)       # 风水涣
    Kan_Dui = combineDiagrams(EDiagrams.Kan, EDiagrams.Dui)       # 水泽节
    Xun_Dui = combineDiagrams(EDiagrams.Xun, EDiagrams.Dui)       # 风泽中孚
    Zhen_Gen = combineDiagrams(EDiagrams.Zhen, EDiagrams.Gen)     # 雷山小过
    Kan_Li = combineDiagrams(EDiagrams.Kan, EDiagrams.Li)         # 水火既济
    Li_Kan = combineDiagrams(EDiagrams.Li, EDiagrams.Kan)         # 火水未济


sixty_four_diagrams_info = {
    ESixtyFourDiagrams.Qian_Qian: SixtyFourDiagramInfo(
        name="乾为天",
        statement="元亨利贞。",
        meaning="强健",
        description="乾卦象征强健和积极向上，代表创造力和领导力。"
    ),
    ESixtyFourDiagrams.Kun_Kun: SixtyFourDiagramInfo(
        name="坤为地",
        statement="元亨，利牝马之贞。",
        meaning="顺从",
        description="坤卦象征顺从和包容，代表接纳和滋养。"
    ),
    ESixtyFourDiagrams.Li_Li: SixtyFourDiagramInfo(
        name="离为火",
        statement="亨，柔蓉，故小人道而无行。",
        meaning="光明",
        description="离卦象征光明和分离，提醒保持清晰的目标。"
    ),
    ESixtyFourDiagrams.Xun_Xun: SixtyFourDiagramInfo(
        name="巽为风",
        statement="亨，柔蓉，故小人道而无行。",
        meaning="顺应",
        description="巽卦象征风，表示适应变化的能力。"
    ),
    ESixtyFourDiagrams.Dui_Dui: SixtyFourDiagramInfo(
        name="兑为泽",
        statement="亨，利贞。",
        meaning="喜悦",
        description="兑卦象征喜悦与交流，代表愉快的合作。"
    ),
    ESixtyFourDiagrams.Zhen_Zhen: SixtyFourDiagramInfo(
        name="震为雷",
        statement="亨。震来虩虩，笑言哑哑。",
        meaning="震动",
        description="震卦象征雷电，表示动荡和惊恐的情景。"
    ),
    ESixtyFourDiagrams.Gen_Gen: SixtyFourDiagramInfo(
        name="艮为山",
        statement="艮其背，不获其身。",
        meaning="止步",
        description="艮卦象征山，代表静止和克制。"
    ),
    ESixtyFourDiagrams.Kan_Kan: SixtyFourDiagramInfo(
        name="坎为水",
        statement="亨，利贞。",
        meaning="危险",
        description="坎卦象征水，提醒小心谨慎，避免危险。"
    ),
    ESixtyFourDiagrams.Li_Gen: SixtyFourDiagramInfo(
        name="火山旅",
        statement="亨，利贞，故小人之道。",
        meaning="旅行",
        description="旅卦象征旅行，表示探索新领域和自我发现。"
    ),
    ESixtyFourDiagrams.Kan_Li: SixtyFourDiagramInfo(
        name="水火既济",
        statement="亨，利贞。",
        meaning="相辅",
        description="既济卦象征相辅相成，表示和谐共生。"
    ),
    ESixtyFourDiagrams.Xun_Kan: SixtyFourDiagramInfo(
        name="风水涣",
        statement="亨，利见大人。",
        meaning="涣散",
        description="涣卦象征分散，提醒团结、理顺关系。"
    ),
    ESixtyFourDiagrams.Dui_Gen: SixtyFourDiagramInfo(
        name="泽山困",
        statement="亨，小畜之志。",
        meaning="困境",
        description="困卦象征困境，提醒应对困难和挫折。"
    ),
    ESixtyFourDiagrams.Zhen_Gen: SixtyFourDiagramInfo(
        name="雷山小过",
        statement="亨，利贞。",
        meaning="小过",
        description="小过卦象征轻微失误，提醒稳中求进。"
    ),
    ESixtyFourDiagrams.Kun_Xun: SixtyFourDiagramInfo(
        name="地风升",
        statement="元亨，利见大人。",
        meaning="上升",
        description="升卦象征提升，表示通过奋斗取得进步。"
    ),
    ESixtyFourDiagrams.Li_Kun: SixtyFourDiagramInfo(
        name="火地晋",
        statement="康侯用锡马蕃庶，昼日三接。",
        meaning="进步",
        description="晋卦象征进步，表示积极努力。"
    ),
    ESixtyFourDiagrams.Gen_Xun: SixtyFourDiagramInfo(
        name="山风蛊",
        statement="亨，利贞。",
        meaning="腐化",
        description="蛊卦象征治理，表示面对旧有问题和解决腐败。"
    ),
    ESixtyFourDiagrams.Qian_Gen: SixtyFourDiagramInfo(
        name="天山遁",
        statement="亨，小利贞。",
        meaning="遁隐",
        description="遁卦象征退隐，表示隐忍和躲避。"
    ),
    ESixtyFourDiagrams.Xun_Dui: SixtyFourDiagramInfo(
        name="风泽中孚",
        statement="豚鱼吉，利涉大川。",
        meaning="诚信",
        description="中孚卦象征诚实，表示言行一致、言出必行。"
    ),
    ESixtyFourDiagrams.Dui_Li: SixtyFourDiagramInfo(
        name="泽火革",
        statement="己日乃孚，元亨利贞。",
        meaning="改革",
        description="革卦象征革新，表示摆脱旧事物、迎接新生。"
    ),
    ESixtyFourDiagrams.Zhen_Xun: SixtyFourDiagramInfo(
        name="雷风恒",
        statement="亨，无咎，利贞。",
        meaning="恒久",
        description="恒卦象征持久和坚定，提醒坚持不懈并有耐心。"
    ),
    ESixtyFourDiagrams.Kun_Gen: SixtyFourDiagramInfo(
        name="地山谦",
        statement="亨，君子有终。",
        meaning="谦虚",
        description="谦卦象征谦逊，提醒保持低调、包容和克己。"
    ),
    ESixtyFourDiagrams.Dui_Qian: SixtyFourDiagramInfo(
        name="泽天夬",
        statement="亨，利见大人。",
        meaning="决断",
        description="夬卦象征果断，提醒做出明智决策。"
    ),
    ESixtyFourDiagrams.Kun_Li: SixtyFourDiagramInfo(
        name="地火明夷",
        statement="利艰贞。",
        meaning="受难",
        description="明夷卦象征暗淡，提醒面对困境要保持冷静与坚韧。"
    ),
    ESixtyFourDiagrams.Qian_Li: SixtyFourDiagramInfo(
        name="天火同人",
        statement="亨，王假之。",
        meaning="团结",
        description="同人卦象征团结，强调合作与共赢。"
    ),
    ESixtyFourDiagrams.Zhen_Li: SixtyFourDiagramInfo(
        name="雷火丰",
        statement="亨，王假之。",
        meaning="丰盛",
        description="丰卦象征繁荣昌盛，表示丰收与成就。"
    ),
    ESixtyFourDiagrams.Xun_Li: SixtyFourDiagramInfo(
        name="风火家人",
        statement="亨，王假之。",
        meaning="家庭",
        description="家人卦象征家庭和睦，代表温暖和支持。"
    ),
    ESixtyFourDiagrams.Zhen_Kun: SixtyFourDiagramInfo(
        name="雷地豫",
        statement="利建侯行师。",
        meaning="愉悦",
        description="豫卦象征愉悦，代表安心。"
    ),
    ESixtyFourDiagrams.Xun_Qian: SixtyFourDiagramInfo(
        name="风天小畜",
        statement="亨，利贞。",
        meaning="小有所蓄",
        description="小畜卦象征小有所蓄，提醒保持克制。"
    ),
    ESixtyFourDiagrams.Gen_Qian: SixtyFourDiagramInfo(
        name="山天大畜",
        statement="亨，利贞。",
        meaning="大有所蓄",
        description="大畜卦象征大有所蓄，强调积累和资源管理。"
    ),
    ESixtyFourDiagrams.Kan_Xun: SixtyFourDiagramInfo(
        name="水风井",
        statement="亨，利贞。",
        meaning="井水",
        description="井卦象征水源，代表滋养和支持。"
    ),
    ESixtyFourDiagrams.Li_Xun: SixtyFourDiagramInfo(
        name="火风鼎",
        statement="亨，利贞。",
        meaning="鼎盛",
        description="鼎卦象征鼎盛与发展，表示持久的成就。"
    ),
    ESixtyFourDiagrams.Dui_Xun: SixtyFourDiagramInfo(
        name="泽风大过",
        statement="亨，利贞。",
        meaning="过量",
        description="大过卦象征过量，提醒适度与节制。"
    ),
    ESixtyFourDiagrams.Qian_Xun: SixtyFourDiagramInfo(
        name="天风随",
        statement="亨，利见大人。",
        meaning="随和",
        description="随卦象征随和，代表适应变化与接受。"
    ),
    ESixtyFourDiagrams.Kan_Gen: SixtyFourDiagramInfo(
        name="水山蹇",
        statement="亨，利贞。",
        meaning="阻碍",
        description="蹇卦象征阻碍，提醒应对困难与挑战。"
    ),
    ESixtyFourDiagrams.Li_Kan: SixtyFourDiagramInfo(
        name="火水未济",
        statement="亨，利贞。",
        meaning="未济",
        description="未济卦象征未完结，提醒保持耐心与准备。"
    ),
    ESixtyFourDiagrams.Xun_Gen: SixtyFourDiagramInfo(
        name="风山渐",
        statement="亨，利贞。",
        meaning="渐进",
        description="渐卦象征渐进，提醒稳步前行与逐步发展。"
    ),
    ESixtyFourDiagrams.Li_Dui: SixtyFourDiagramInfo(
        name="火泽睽",
        statement="亨，利贞。",
        meaning="分裂",
        description="睽卦象征分裂，提醒寻求和谐与团结。"
    ),
ESixtyFourDiagrams.Kan_Zhen: SixtyFourDiagramInfo(
        name="水雷屯",
        statement="亨，利贞。",
        meaning="屯有阻碍",
        description="屯卦象征阻碍，提醒人们在面对困难时要保持耐心和坚持。"
    ),
    ESixtyFourDiagrams.Gen_Kan: SixtyFourDiagramInfo(
        name="山水蒙",
        statement="亨，柔蓄而志行。",
        meaning="蒙昧",
        description="蒙卦象征蒙昧与学习，鼓励人们从错误中吸取教训，逐步成长。"
    ),
    ESixtyFourDiagrams.Kan_Qian: SixtyFourDiagramInfo(
        name="水天需",
        statement="亨，利用行人。",
        meaning="需索",
        description="需卦象征需求，表示在紧急情况下要懂得适应环境，寻求帮助。"
    ),
    ESixtyFourDiagrams.Qian_Kan: SixtyFourDiagramInfo(
        name="天水讼",
        statement="亨，故小人不利于大人。",
        meaning="讼争",
        description="讼卦象征争执，提醒人们在处理纷争时要保持公正和理智。"
    ),
    ESixtyFourDiagrams.Kun_Kan: SixtyFourDiagramInfo(
        name="地水师",
        statement="亨，柔克刚。",
        meaning="师出",
        description="师卦象征进攻与行动，提醒人们在行动前应做好充分准备。"
    ),
    ESixtyFourDiagrams.Kan_Kun: SixtyFourDiagramInfo(
        name="水地比",
        statement="亨，兄弟和而利。",
        meaning="比和",
        description="比卦象征和谐，强调团结与合作的重要性。"
    ),
    ESixtyFourDiagrams.Qian_Dui: SixtyFourDiagramInfo(
        name="天泽履",
        statement="亨，利见小人。",
        meaning="履行",
        description="履卦象征行动与责任，强调在做出承诺后应履行自己的责任。"
    ),
    ESixtyFourDiagrams.Kun_Qian: SixtyFourDiagramInfo(
        name="地天泰",
        statement="亨，天时利。",
        meaning="泰和",
        description="泰卦象征和谐与安定，表示大环境适合发展与合作。"
    ),
    ESixtyFourDiagrams.Qian_Kun: SixtyFourDiagramInfo(
        name="天地否",
        statement="亨，天地不交。",
        meaning="否决",
        description="否卦象征隔绝与否定，提醒人们在冲突中保持冷静和理智。"
    ),
    ESixtyFourDiagrams.Li_Qian: SixtyFourDiagramInfo(
        name="天火同人",
        statement="亨，利见大人。",
        meaning="同心",
        description="同人卦象征团结，强调在共同目标下的合作与支持。"
    ),
    ESixtyFourDiagrams.Dui_Zhen: SixtyFourDiagramInfo(
        name="泽雷随",
        statement="亨，柔和则志行。",
        meaning="随和",
        description="随卦象征随和，代表适应变化与接受。"
    ),
    ESixtyFourDiagrams.Kun_Dui: SixtyFourDiagramInfo(
        name="地泽临",
        statement="亨，利见贤人。",
        meaning="临近",
        description="临卦象征靠近，强调面对他人应保持谦和与真诚。"
    ),
    ESixtyFourDiagrams.Xun_Kun: SixtyFourDiagramInfo(
        name="风地观",
        statement="亨，利见士。",
        meaning="观察",
        description="观卦象征观察与了解，提醒人们在行动前要仔细观察环境。"
    ),
    ESixtyFourDiagrams.Li_Zhen: SixtyFourDiagramInfo(
        name="火雷噬嗑",
        statement="亨，利贞。",
        meaning="噬嗑",
        description="噬嗑卦象征解决与化解，表示在困境中寻找解决方案。"
    ),
    ESixtyFourDiagrams.Gen_Li: SixtyFourDiagramInfo(
        name="山火贲",
        statement="亨，利见士。",
        meaning="装饰",
        description="贲卦象征美化与装饰，强调在生活中应注重外在与内在的和谐。"
    ),
    ESixtyFourDiagrams.Gen_Kun: SixtyFourDiagramInfo(
        name="山地剥",
        statement="亨，利贞。",
        meaning="剥落",
        description="剥卦象征损失与剥离，提醒人们在生活中要保持警惕，防止损失。"
    ),
    ESixtyFourDiagrams.Kun_Zhen: SixtyFourDiagramInfo(
        name="地雷复",
        statement="亨，利贞。",
        meaning="复苏",
        description="复卦象征复苏与重生，表示在逆境中寻找机会与希望。"
    ),
    ESixtyFourDiagrams.Qian_Zhen: SixtyFourDiagramInfo(
        name="天雷无妄",
        statement="亨，利贞。",
        meaning="无妄",
        description="无妄卦象征意外与惊喜，提醒人们在生活中保持开放的心态。"
    ),
    ESixtyFourDiagrams.Gen_Zhen: SixtyFourDiagramInfo(
        name="山雷颐",
        statement="亨，利贞。",
        meaning="颐养",
        description="颐卦象征滋养与保护，强调对他人和自身的关爱与呵护。"
    ),
    ESixtyFourDiagrams.Zhen_Qian: SixtyFourDiagramInfo(
        name="雷天大壮",
        statement="亨，利见大人。",
        meaning="壮大",
        description="大壮卦象征壮大与增强，表示在适当的时机采取行动。"
    ),
    ESixtyFourDiagrams.Zhen_Kan: SixtyFourDiagramInfo(
        name="雷水解",
        statement="亨，利贞。",
        meaning="解脱",
        description="解卦象征解脱与释放，强调在困境中找到解脱的途径。"
    ),
    ESixtyFourDiagrams.Gen_Dui: SixtyFourDiagramInfo(
        name="山泽损",
        statement="亨，利见贤人。",
        meaning="损失",
        description="损卦象征损失与减少，提醒人们在决策时要慎重。"
    ),
    ESixtyFourDiagrams.Xun_Zhen: SixtyFourDiagramInfo(
        name="风雷益",
        statement="亨，利见士。",
        meaning="益处",
        description="益卦象征增益与提升，表示在合适的时机采取行动能带来好处。"
    ),
    ESixtyFourDiagrams.Dui_Kun: SixtyFourDiagramInfo(
        name="泽地困",
        statement="亨，利贞。",
        meaning="困扰",
        description="困卦象征困扰与局限，提醒人们在面对困境时要保持清醒和冷静。"
    ),
    ESixtyFourDiagrams.Dui_Kan: SixtyFourDiagramInfo(
        name="泽水困",
        statement="亨，利贞。",
        meaning="困境",
        description="困境卦象征在绝境中要寻求突破，强调机智与灵活应对。"
    ),
    ESixtyFourDiagrams.Zhen_Dui: SixtyFourDiagramInfo(
        name="雷泽归妹",
        statement="亨，利见大人。",
        meaning="归属",
        description="归妹卦象征归属与联合，强调在团体中应相互支持与帮助。"
    ),
    ESixtyFourDiagrams.Kan_Dui: SixtyFourDiagramInfo(
        name="水泽节",
        statement="亨，利贞。",
        meaning="节制",
        description="节卦象征节制与控制，提醒人们在生活中要懂得适可而止。"
    )
}


def getDiagramName(diagram):
    info = diagrams_info[diagram]
    if info:
        return info.name + "为" + info.meaning
    else:
        return False


def getSixtyFourDiagramName(diagram):
    if not sixty_four_diagrams_info.__contains__(diagram):
        return False
    info = sixty_four_diagrams_info[diagram]
    if info:
        return info.name
    else:
        return False


#将六十四卦分离为上下纯卦
def sepSixtyFourDiagrams(origin):
    shang = EDiagrams(origin.value & 0b000111)
    xia = EDiagrams((origin.value & 0b111000) >> 3)
    return shang, xia


#根据本卦获取互卦
def getHuDiagram(ben):
    shang = EDiagrams(ben.value & 0b001110 >> 1)
    xia = EDiagrams(ben.value & 0b011100 >> 2)
    return ESixtyFourDiagrams(combineDiagrams(shang, xia))

#根据本卦和爻动获取变卦
def getBianDiagram(ben, yao):
    y = rotate_right(0b000001, yao, 6)
    return ESixtyFourDiagrams(ben.value ^ y)


#二进制数循环右移
def rotate_right(value, bits, total_bits):
    return (value >> bits) | (value << (total_bits - bits) & ((1 << total_bits) - 1))


def main():
    for name, member in ESixtyFourDiagrams.__members__.items():
        shang, xia = sepSixtyFourDiagrams(member)
        shang = getDiagramName(shang)
        xia = getDiagramName(xia)
        print("\n")
        print("枚举:" + name + "\n上：" + shang + " 下：" + xia)
        sixtyFourName = getSixtyFourDiagramName(member)
        print("本卦：" + sixtyFourName)

        hu = getHuDiagram(member)
        huName = getSixtyFourDiagramName(hu)
        print("互卦：" + huName)

        for i in range(6):
            yao = i + 1
            bian = getBianDiagram(member, yao)
            bianName = getSixtyFourDiagramName(bian)
            print(str(yao) + "爻变卦： " + bianName)




main()
