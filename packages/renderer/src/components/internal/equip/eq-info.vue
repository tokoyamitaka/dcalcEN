<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore } from "@/store"
  import { rarityClass, formatStr } from "@/utils"
  import { asyncComputed } from "@vueuse/core"
  import { computed, defineComponent, PropType, reactive, renderList, watch } from "vue"

  import EqIcon from "./eq-icon.vue"

  interface Status {
    id: number
    label: string
    num: number
    isRate: boolean
    info: string
  }

  interface BadgeItem {
    type: number
    props: string[]
  }

  type classNames = (id: number) => string | string[] | undefined

  export default defineComponent({
    name: "info-dialog",
    components: { EqIcon },
    props: {
      eid: {
        type: [Number, String] as PropType<ID>
      },
      simple: {
        type: Boolean,
        default: false
      },
      colums: {
        type: Boolean,
        default: false
      },
      small: {
        type: Boolean,
        default: false
      },
      forget: {
        type: Object,
        default: () => {}
      },
      pps: {
        type: Array,
        default: () => []
      },
      withTransform: {
        type: Boolean,
        default: false
      },
      isShow: {
        type: [Boolean, Object],
        default: false
      }
    },
    setup(props, { emit, slots }) {
      const basicStore = useBasicInfoStore()

      const equip = asyncComputed(async () => {
        if (props.eid != undefined) {
          let temp = await basicStore.get_equipment_detail(props.eid)
          if (props.withTransform) loadTransform(temp)
          return temp
        }
      })

      function renderStatus(rowClass?: classNames, spanClass?: classNames, withTransform?: boolean) {
        return ({ id, label, num, isRate }: Status, indexForStatus: number) => {
          let array: JSX.Element[] = []

          array.push(<span style={num ? "margin-right: 5px" : undefined}>{label}</span>)
          const rowClassNames = rowClass?.(id)
          const spanClassNames = spanClass?.(id)
          if (num) {
            let text: any = num
            if (isRate) {
              text = (num * 100).toFixed()
              text = (num > 0 ? "+" : "") + `${text}%`
            }
            //array.push(<span class={spanClassNames}>{text}</span>)
            array.push(<span>{text}</span>)
          }

          let result: JSX.Element = <div class={[rowClassNames]}>{array}</div>
          if (withTransform) {
            let nameIndex = propNames.findIndex(x => x == label)
            if (nameIndex > -1 && (transform.refine > 0 || transform.reinforce > 0)) {
              let arr = setTransform(nameIndex)
              array = array.concat(arr)

              let beforeArr = []
              // ??????????????????
              for (var i = nameIndex - 1; i >= 0; i--) {
                if (isWithTransform(i)) {
                  let name = propNames[i]
                  let index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                  if (index >= 0) {
                    break
                  } else {
                    let tArr = setTransform(i, name)
                    beforeArr.push(<div class={[rowClassNames]}>{tArr}</div>)
                  }
                }
              }
              let arrterArr = []
              // ??????????????? ??????????????????
              if (indexForStatus == equip.value.prop.base.length - 1) {
                for (let i = nameIndex + 1; i < propNames.length; i++) {
                  if (isWithTransform(i)) {
                    let name = propNames[i]
                    let index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                    if (index < 0) {
                      let tArr = setTransform(i, name)
                      arrterArr.push(<div class={[rowClassNames]}>{tArr}</div>)
                    }
                  }
                }
              }
              result = (
                <div>
                  {beforeArr}
                  <div class={[rowClassNames]}>{array}</div>
                  {arrterArr}
                </div>
              )
            }
          }
          return result
        }
      }

      function isWithTransform(i: number) {
        return transform.reinforceInfo.strengthen[i] > 0 || transform.reinforceInfo.reinforce[i] > 0 || transform.reinforceInfo.refine[i] > 0
      }

      function setTransform(index: number, name?: string) {
        let array: JSX.Element[] = []
        if (transform.reinforceInfo.strengthen[index] > 0) {
          // ??????
          if (name) {
            array.push(<span class="advanced">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="advanced">
                {transform.reinforceInfo.strengthen[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="advanced">
                +{transform.reinforceInfo.strengthen[index]}
              </span>
            )
          }
        }
        if (transform.reinforceInfo.reinforce[index] > 0) {
          // ??????
          if (name && transform.reinforceInfo.strengthen[index] <= 0) {
            array.push(<span class="artifact">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="artifact">
                {transform.reinforceInfo.reinforce[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="artifact">
                +{transform.reinforceInfo.reinforce[index]}
              </span>
            )
          }
        }
        if (transform.reinforceInfo.refine[index] > 0) {
          // ??????
          if (name && transform.reinforceInfo.strengthen[index] <= 0 && transform.reinforceInfo.reinforce[index] <= 0) {
            array.push(<span class="rare">{name}</span>)
            array.push(
              <span style="margin-left: 5px" class="rare">
                {transform.reinforceInfo.refine[index]}
              </span>
            )
          } else {
            array.push(
              <span style="margin-left: 5px" class="rare">
                +{transform.reinforceInfo.refine[index]}
              </span>
            )
          }
        }
        return array
      }

      const effectClass = function (id: number) {
        if (id > 13) {
          return "strong"
        }
      }

      const growthClass = function (id: number) {
        const classNames = []

        if (id == 100) {
          classNames.push("yellow")
        } else if (id == 102) {
          classNames.push("strong")
        }
        if (id > 100) {
          classNames.push("paddleft")
        }
        if (id >= 1000) {
          classNames.push("suiji-props")
          if (id > 1000) {
            classNames.push("yellow")
          } else {
            classNames.push("gey")
          }
        }
        return classNames
      }

      const characterStore = useCharacterStore()

      const is_buffer = computed(() => characterStore.is_buffer)

      const sum_buffer = computed(() => {
        let s = 0
        if (transform.growthBuffers && transform.growthBuffers.length > 0) {
          let a = equip.value.prop.growthProps

          for (let i = 0; i < transform.growthBuffers.length; i++) {
            let item = a == null ? null : a[i]
            s += transform.growthBuffers[i] ?? item?.buffer ?? 0
          }
        }
        if (s == 0) {
          for (let i = 0; i < 4; i++) {
            let item = equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null
            s += item?.buffer ?? 0
          }
        }

        return s
      })

      const sum_attack = computed(() => {
        let s = 0
        if (transform.growthBuffers && transform.growthBuffers.length > 0) {
          let a = equip.value.prop.growthProps

          for (let i = 0; i < transform.growthBuffers.length; i++) {
            let item = a == null ? null : a[i]
            s += transform.growthAttacks[i] ?? item?.attack ?? 0
          }
        }
        if (s == 0) {
          for (let i = 0; i < 4; i++) {
            let item = equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null
            s += item?.attack ?? 0
          }
        }
        return s
      })

      const propNames = ["??????", "??????", "??????", "??????", "???????????????", "???????????????", "???????????????"]
      const badgeNames = ["?????????????????????", "?????????????????????", "?????????????????????", "?????????????????????", "?????????????????????"]
      const badgeClass = ["kong-baijin", "kong-red", "kong-green", "kong-blue", "kong-yellow"]
      const eqBagdes = {
        ??????: 2,
        ??????: 2,
        ??????: 4,
        ??????: 4,
        ??????: 1,
        ??????: 1,
        ???: 3,
        ??????: 3,
        ????????????: 0,
        ?????????: 0
      }

      const transform = reactive({
        enchanting: [] as string[], //["?????????????????? +30"], // ??????
        reinforce: 0, // 18, // ?????????????????????
        type: 1,
        refine: 0, //8, // ??????
        reinforceInfo: {
          reinforce: [0, 0, 0, 0, 0, 0, 0], //[0, 91, 91, 0, 0, 0, 0], //??????
          strengthen: [0, 0, 0, 0, 0, 0, 0], //[29, 29, 0, 29, 0, 0, 0], //??????
          refine: [0, 0, 0, 0, 0, 0, 0], //[0, 0, 0, 0, 0, 0, 539]// ??????
          refineSW: 0 //[0, 0, 0, 0, 0, 0, 539]// ??????
        },
        growthLvs: [1, 1, 1, 1], // ????????????
        growthAttacks: [0, 0, 0, 0], // ????????????
        growthBuffers: [0, 0, 0, 0], // ????????????
        badges: [] as BadgeItem[] //[ { type: 1,  props: [ "?????? +30", ] }, { type: 2,  props: [ "??????+30 ??????+3%", ] }, { type: 3,  props: [ "?????? +20", ] },
        //{ type: 4,  props: [ "?????? +15", ] }, { type: 0,  props: [  "??????+8 [????????????]??????Lv+1", ] }, ], // ??????
      })
      function loadTransform(eq: any) {
        if (props.forget) {
          if (props.forget.info) {
            transform.growthLvs = props.forget.info["??????????????????"] ?? [1, 1, 1, 1]
            transform.growthAttacks = props.forget.data["attack"] ?? [0, 0, 0, 0]
            transform.growthBuffers = props.forget.data["buffer"] ?? [0, 0, 0, 0]
            transform.reinforce = props.forget.info["????????????"] ?? 0
            transform.refine = props.forget.info["????????????"] ?? 0
            transform.enchanting = props.forget.info["??????"] ?? []

            transform.type = props.forget.info["????????????"] ?? 1

            // ????????????
            transform.badges = []
            if (eq && eq.position) {
              let types = eq.position.split("(")
              let type = types[0]
              let position = type
              if (types.length > 1) {
                position = types[1].split(")")[0]
              }
              let bgs = props.forget.info["??????"] ?? []
              for (var b of bgs) {
                if (b) {
                  transform.badges.push({
                    type: eqBagdes[position] ?? 0,
                    props: [b]
                  })
                }
              }
            }

            // ????????????????????????
            transform.reinforceInfo.reinforce = [0, 0, 0, 0, 0, 0, 0]
            transform.reinforceInfo.strengthen = [0, 0, 0, 0, 0, 0, 0]
            if (transform.reinforce > 0) {
              if (transform.type == 1 && props.forget.data["????????????"] && props.forget.data["????????????"].length > 0) {
                // ??????
                for (var i = 0; i < props.forget.data["????????????"].length; i++) {
                  transform.reinforceInfo.reinforce[i] = props.forget.data["????????????"][i]
                }
              }
              if (props.forget.data["????????????"] && props.forget.data["????????????"].length > 0) {
                for (var i = 0; i < props.forget.data["????????????"].length; i++) {
                  transform.reinforceInfo.strengthen[i] = props.forget.data["????????????"][i]
                }
              }
              if (props.forget.data["???????????????"] && props.forget.data["???????????????"].length > 0) {
                for (var i = 0; i < props.forget.data["???????????????"].length; i++) {
                  transform.reinforceInfo.strengthen[i + 4] = props.forget.data["???????????????"][i]
                }
              }
            }
            // ????????????????????????
            transform.reinforceInfo.refine = [0, 0, 0, 0, 0, 0, 0]
            transform.reinforceInfo.refineSW = 0
            if (transform.refine > 0) {
              let dz = props.forget.data["????????????"]
              if (dz && dz.length > 0) {
                transform.reinforceInfo.refine[6] = dz[0]
              }
              if (dz && dz.length > 1) {
                transform.reinforceInfo.refineSW = dz[1]
              }
            }
          }
        }
      }

      function formatProp(strs: string[], template: string, i: number, withleft: boolean) {
        if (props.forget && props.forget.data && props.forget.data.params && props.forget.data.params.length > i && props.forget.data.params[i] && template) {
          let params = props.forget.data.params[i]
          let nums = []
          for (var x of params) {
            nums.push("<span class='" + classForNum(i) + "'>+" + x + "</span>")
          }
          let str = formatStr(template, nums)
          strs = str.split("<br>")
          return renderList(strs, s => (
            <div class={["strong"].concat([withleft ? "paddleft" : ""])}>
              <span v-html={s}></span>
            </div>
          ))
        } else {
          return renderList(strs, s => (
            <div class={["strong"].concat([withleft ? "paddleft" : ""])}>
              <span>{s}</span>
            </div>
          ))
        }
      }

      watch(props, () => {
        if (props.isShow) {
          loadTransform(equip.value) // ??????????????????
        }
      })

      const iconBages = computed(() => {
        let x = transform.badges && transform.badges.length > 0 ? { color: [transform.badges[0]?.type, transform.badges[1]?.type], num: transform.badges.length } : null
        return x
      })

      function classForNum(i: number) {
        let c = (transform.growthLvs[i] ?? 1) <= 20 ? "" : transform.growthLvs[i] <= 50 ? "advanced" : transform.growthLvs[i] < 80 ? "rare" : transform.growthLvs[i] == 100 ? "epic" : "artifact"
        return c
      }

      function renderLevel(i: number, left: boolean) {
        let a = equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null
        return is_buffer.value ? (
          <div class={["text-hex-8a6f36"].concat(left ? "paddleft" : "")}>
            <span style="margin-right: 10px;">Buff???</span>
            <span class={classForNum(i)}>{transform.growthBuffers[i] || a?.buffer || 0}</span>
          </div>
        ) : (
          <div class={["text-hex-8a6f36"].concat(left ? "paddleft" : "")}>
            <span style="margin-right: 10px;">????????????</span>
            <span class={classForNum(i)}>{transform.growthAttacks[i] || a?.attack || 0}</span>
          </div>
        )
      }

      return () => {
        if (!equip.value) {
          return <div></div>
        }
        return (
          <div class={["approved-form"].concat([props.colums ? "with-colums" : ""])}>
            <div class="epic title" style="display: flex">
              <eq-icon eq={equip.value} badges={iconBages.value}></eq-icon>
              <div class="eq-name" style="width: 100%; margin-left: 8px">
                <div>
                  <span style="display: flex" class={rarityClass(equip.value.rarity)}>
                    {transform.reinforce > 0 ? <span style="margin-right: 4px">+{transform.reinforce}</span> : <span></span>}
                    {transform.refine > 0 ? <span>({transform.refine})</span> : <span></span>}
                    <span>{equip.value.name}</span>
                  </span>
                </div>
                <div class="eq-name yellow" style="width: 100%; text-align: right">
                  <span>{equip.value.position}</span>
                </div>
              </div>
            </div>
            {transform.badges && transform.badges.length > 0 ? (
              <div>
                <div class="hr"></div>
                <div style="display: flex">
                  {renderList(transform.badges, (bs, i) => (
                    <div style={i > 0 ? "margin-left: 20px" : ""}>
                      <div class={badgeClass[bs.type]}>[{badgeNames[bs.type]}]</div>
                      {renderList(bs.props, b => (
                        <div>{b}</div>
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div></div>
            )}
            <div class="hr"></div>
            {transform.reinforce > 0 || transform.refine > 0 ? (
              <span>
                {transform.reinforce > 0 ? (
                  <span style="margin-right: 5px">
                    {transform.type == 1 ? (
                      <span>
                        <span class="advanced">+{transform.reinforce} ??????</span>/<span class="artifact">??????</span>
                      </span>
                    ) : (
                      <span class="advanced">+{transform.reinforce} ??????</span>
                    )}
                  </span>
                ) : (
                  <span></span>
                )}
                {transform.refine > 0 ? (
                  <span style="margin-right: 5px" class="rare">
                    +{transform.refine} ??????
                  </span>
                ) : (
                  <span></span>
                )}
                <span>????????????</span>
              </span>
            ) : (
              <span></span>
            )}
            {equip.value.prop.base.map(renderStatus(undefined, undefined, true))}
            <div class="hr"></div>
            <div class="green"> &lt;??????&gt; </div>
            {transform.enchanting != null && transform.enchanting.length > 0 ? (
              <div class="enchanting" style="margin-top:6px">
                {renderList(transform.enchanting, e => (
                  <div>{e.replace("(", " +").replace(")", "")}</div>
                ))}
              </div>
            ) : (
              <div class="gey">?????????????????????</div>
            )}
            {equip.value.prop.effect && equip.value.prop.effect.length > 0 && (
              <div>
                <div class="hr"></div>
                {equip.value.prop.effect.map(renderStatus(effectClass))}
              </div>
            )}
            {transform.reinforceInfo.refineSW > 0 ? (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;????????????????????????&gt; </div>
                <div class="rare">??????/??????/??????/?????? +{transform.reinforceInfo.refineSW}</div>
              </div>
            ) : (
              <span></span>
            )}

            {(sum_attack.value > 0 || sum_buffer.value > 0 || (props.pps != null && props.pps.length > 0)) && (
              <div>
                <div class="hr"></div>
                <div class="green"> &lt;????????????&gt; </div>
                {!props.simple && <div>{is_buffer.value ? <div>???????????????Buff??? {sum_buffer.value}</div> : <div class="text-hex-8a6f36">??????????????????????????? {sum_attack.value}</div>}</div>}
              </div>
            )}
            {props.pps != null && props.pps.length > 0
              ? renderList(props.pps, (x: any, i: number) =>
                  x != null ? (
                    <div class="suiji-props" style="padding-top: 5px">
                      <div class="yellow">
                        ?????? {i + 1} - Lv{transform.growthLvs[i]}
                      </div>
                      {renderLevel(i, false)}
                      {formatProp(x.props, x.template, i)}
                    </div>
                  ) : (
                    <div class="suiji-props gey">
                      <div class="yellow">
                        ?????? {i + 1} - Lv{transform.growthLvs[i]}
                      </div>
                      <span>???????????? [????????????] ??????????????????</span>
                    </div>
                  )
                )
              : renderList(equip.value.prop.growthProps, (p, i: number) => (
                  <div style="padding-bottom: 5px">
                    {p.props && p.props.length > 0 ? (
                      <>
                        <div class="yellow">
                          <span>
                            ?????? {i + 1} - Lv{transform.growthLvs[i] || 1}
                          </span>
                        </div>
                        {renderLevel(i, true)}
                        {formatProp(p.props, p.template, i, true)}
                      </>
                    ) : (
                      <div class="paddleft suiji-props gey">
                        <span>????????????</span>
                      </div>
                    )}
                  </div>
                ))}
          </div>
        )
      }
    }
  })
</script>
<style src="./eq-info.scss" scoped></style>
