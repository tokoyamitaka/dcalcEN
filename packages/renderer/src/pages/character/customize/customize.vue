<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore } from "@/store"
  import EquipIcon from "@/components/internal/equip/eq-icon.vue"
  import EquipInfo from "@/components/internal/equip/eq-info.vue"
  import { padding, rarityClass } from "@/utils"
  import { computed, defineComponent, onMounted, onUnmounted, reactive, ref, renderList, watch } from "vue"

  export interface IJadeUpgrade {
    id: number
    name: string
    damage: number
    percent: string
    color: string
  }

  type FilterFunction = (e: IEquipmentInfo) => boolean

  export default defineComponent({
    async setup() {
      const configStore = useConfigStore()
      const basicStore = useBasicInfoStore()
      const detailsStore = useDetailsStore()
      const characterStore = useCharacterStore()

      const filter = ref<FilterFunction | null>()

      const props_public = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
      // 首饰
      const props_jewels = [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
      // 防具
      const props_armors = [
        128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164
      ]
      // 特殊装备
      const props_specials = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]

      const colspans = ref([false, true, true])

      const equips = computed(() => {
        let list = basicStore.equipment_list.filter(item => item.alternative.length > 0) ?? [] ?? []
        list = list.filter(r => {
          return r.name.includes(keyword.value.trim())
        })
        if (!!filter.value && filter.value instanceof Function) {
          list = list.filter(filter.value)
        }
        return list
      })

      const show_list = computed(() => {
        const start = (pagination.page - 1) * pagination.pageSize
        const end = start + pagination.pageSize
        return equips.value.slice(start, end)
      })

      function reset() {
        keyword.cache = ""
        keyword.value = ""
        pagination.page = 1
      }

      const selectEquip = ref<ID>()
      const selectEquipProps = ref<number[]>([0, 0, 0, 0])
      const selectPropsCheckedList = ref<Record<string, boolean>>({})

      const keyword = reactive({
        value: "",
        cache: ""
      })

      function chooseEqu(equ: IEquipmentInfo) {
        return (event: Event) => {
          event.preventDefault()
          colspans.value = [false, true, true]
          selectEquip.value = equ.id
          selectEquipProps.value = configStore.customize[equ.id ?? ""] ?? [0, 0, 0, 0]
          alternative_list(equ.id).forEach(a => (selectPropsCheckedList.value[a] = selectEquipProps.value.indexOf(a) >= 0))
        }
      }

      const pagination = reactive({
        page: 1,
        pageSize: 14
      })

      const total = computed(() => equips.value.length)
      const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

      watch(total_page, () => {
        pagination.page = 1
      })

      function search() {
        keyword.value = keyword.cache
        pagination.page = 0
      }

      function alternative_list(id: ID, type = -1) {
        let temp = equips.value.filter(item => item.id == id)?.[0]?.alternative ?? []
        // 共有词条
        if (type == 2) {
          temp = temp.filter(a => props_public.indexOf(a) >= 0)
        }
        // 部位专属词条
        if (type == 1) {
          temp = temp.filter(a => props_armors.indexOf(a) >= 0 || props_jewels.indexOf(a) >= 0 || props_specials.indexOf(a) >= 0)
        }
        // 专属词条
        if (type == 0) {
          temp = temp.filter(a => props_public.indexOf(a) < 0 && props_armors.indexOf(a) < 0 && props_jewels.indexOf(a) < 0 && props_specials.indexOf(a) < 0)
        }
        return temp
      }

      function chooseProp(id: number) {
        return (event: Event) => {
          event.stopPropagation()
          let index = selectEquipProps.value.indexOf(id)
          if (index < 0) index = selectEquipProps.value.indexOf(0)
          else id = 0
          if (index >= 0) selectEquipProps.value[index] = id
          configStore.customize[selectEquip.value as number] = selectEquipProps.value
        }
      }

      const entry = (index: number) => {
        return basicStore.entry_list?.[index]
      }

      const singleRef = ref<HTMLElement | null>(null)

      return () => (
        <div class="flex singleset" ref={singleRef}>
          <div class="flex flex-col m-7px mb-0 w-full">
            <div class=" w-full">
              <div class="w-full pb-1.5">
                <div class="bg-hex-000000/45 py-2 px-2 justify-between items-center">
                  <div class="flex space-x-2 mb-2 items-center ">
                    <calc-autocomplete onEnter={search} placeholder="请输入名称搜索" class="flex-1 !h-5" v-model={keyword.cache}></calc-autocomplete>
                    <calc-button onClick={search} title="搜索" class="ml-2" icon="search"></calc-button>
                    <calc-button onClick={reset} title="重置" class="ml-4" icon="reset"></calc-button>
                  </div>
                </div>
              </div>
              <div class="flex h-142  w-full">
                <div class="h-full bg-hex-0d0d0d mx-2px w-25%">
                  <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-2.5rem)]">
                    {renderList(show_list.value, item => {
                      return (
                        <calc-item value={item.id} onClick={chooseEqu(item)} class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border">
                          <div class="h-full w-full top-0 left-0 absolute mask"></div>
                          <EquipIcon eq={item}></EquipIcon>
                          <span class={["text-xs", "ml-4", rarityClass(item.rarity ?? "")]}>{item.name}</span>
                          <span class={["h-4 w-6"]}></span>
                        </calc-item>
                      )
                    })}
                    {renderList(pagination.pageSize - show_list.value.length, i => (
                      <div class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border"></div>
                    ))}
                  </calc-selection>
                  <calc-pagination v-model:page={pagination.page} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
                </div>

                <div class="h-full bg-hex-0d0d0d w-75% s-left">
                  {selectEquip.value && (
                    <>
                      <div class="h-10% w-full overflow-y-hidden !max-w-100%">
                        <EquipInfo eid={selectEquip.value} />
                      </div>
                      <div class="flex h-89%">
                        <div class="flex flex-col h-full w-60% overflow-y-auto !max-w-60%" style="border-right:1px solid #303030">
                          <div>
                            {renderList(["专属", "部位", "公共"], (type, index) => {
                              const alternative = alternative_list(selectEquip.value, index)
                              if (alternative.length > 0)
                                return (
                                  <>
                                    <div onClick={() => (colspans.value[index] = !colspans.value[index])} class="text-hex-3e8848 m-10px">{` < 随机属性池 - ${type}属性 > - 共计${padding(
                                      alternative.length,
                                      2
                                    )}条 点击${colspans.value[index] ? "展开" : "折叠"}`}</div>
                                    <div class={["transition-all", "ease-out-in", "h-auto", "overflow-hidden"].concat(!colspans.value[index] ? [""] : ["max-h-0"])}>
                                      {renderList(alternative, item => {
                                        const entry_info = entry(item)
                                        const disabled = computed(() => selectEquipProps.value.indexOf(item) < 0 && selectEquipProps.value.filter(a => a == 0)?.length == 0)
                                        return (
                                          <div class="m-5px ml-10px mr-10px h-auto">
                                            <div class="flex items-center w-100%">
                                              <calc-checkbox v-model={selectPropsCheckedList.value[item]} class="!h-auto" disabled={disabled.value} onClick={chooseProp(item)}>
                                                {() => (
                                                  <>
                                                    <div class={["flex ml-10px", disabled.value ? "text-hex-5b5b5b" : "text-hex-8a6f36"]}>
                                                      <div>攻击强化:{entry_info?.attack}</div>
                                                      <div class="ml-25px">Buff量:{entry_info?.buff}</div>
                                                    </div>
                                                    {renderList(entry_info?.props, prop => (
                                                      <div class={["ml-10px", disabled.value ? "text-hex-5b5b5b" : "text-hex-b1a785"]}>{prop}</div>
                                                    ))}
                                                  </>
                                                )}
                                              </calc-checkbox>
                                            </div>
                                          </div>
                                        )
                                      })}
                                    </div>
                                  </>
                                )
                            })}
                          </div>
                        </div>
                        <div class="flex flex-col h-full w-40% overflow-y-auto !max-w-40%" style="line-height:22px">
                          <div class="m-10px">
                            <div class="text-hex-4aa256">{" <成长属性> "}</div>

                            {renderList(selectEquipProps.value, (propID, index) => {
                              if (propID == 0)
                                return (
                                  <>
                                    <div class="flex items-center">
                                      <div class="prop-icon"></div>
                                      <div class="text-hex-b59834 ml-8px">{`属性 ${index + 1} - Lv1`}</div>
                                    </div>
                                    <div class="ml-20px text-hex-5b5b5b">随机属性，请在左侧进行选择</div>
                                  </>
                                )
                              else {
                                const entry_info = entry(propID)
                                return (
                                  <>
                                    <div class="flex items-center">
                                      <div class="prop-icon"></div>
                                      <div class="text-hex-b59834 ml-8px">{`属性 ${index + 1} - Lv1`}</div>
                                    </div>
                                    <div class="text-hex-8a6f36 ml-20px">
                                      <div>攻击强化 {entry_info?.attack}</div>
                                      <div>Buff量 {entry_info?.buff}</div>
                                    </div>
                                    {renderList(entry_info?.props, prop => (
                                      <div class={["ml-20px", "text-hex-b1a785"]}>{prop}</div>
                                    ))}
                                  </>
                                )
                              }
                            })}
                          </div>
                        </div>
                      </div>
                    </>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .calc-tags-input {
    .calc-tag {
      text-decoration: underline;
      text-underline-offset: 2px;
      color: #ffb400 !important;

      &:hover {
        color: #fff000 !important;
      }
    }
  }

  .i-checkbox {
    display: flex;
    align-items: flex-start;
    .i-checkbox-icon {
      margin-top: 5px;
    }
    .i-checkbox-icon-disable {
      margin-top: 5px;
    }
    .i-checkbox-label {
      line-height: 22px;
    }
  }
</style>

<style lang="scss" scoped>
  .prop-icon {
    content: "";
    display: inline-block;
    width: 12px;
    height: 12px;
    background-image: url(@/assets/img/icon/switch.png);
  }
  .equip-line {
    border: 1px solid transparent;
    background-image: url("@/assets/img/dictionary_line.png");
    background-repeat: no-repeat;
    background-size: 100% 100%;
    &:hover {
      .mask {
        background-image: url("@/assets/img/hover_mask.png");
        background-repeat: no-repeat;
        background-size: 100% 100%;
      }
    }

    &-selected {
      border: 1px solid #ffb400;
    }
  }

  .singleset {
    .equ {
      display: flex;
      flex-wrap: wrap;
      padding: 5px;
      background-color: rgba(0, 0, 0, 0.45);
      .equ-item {
        width: 30px;
        height: 30px;
        background-color: rgba(0, 0, 0, 0.5);
        border: 1px solid #1a1a1a;
        margin-right: 4px;
        margin-bottom: 4px;

        // &:hover {
        //   width: 30px;
        //   height: 30px;
        //   z-index: 3;
        //   background-image: url(@/assets/img/item_hover.png);
        //   background-size: 100% 100%;
        // }
      }
    }

    .s-left {
      .approved-form {
        width: calc(100% - 23px);
      }
    }
  }
</style>
