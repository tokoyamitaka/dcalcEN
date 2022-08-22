<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import item from "@/components/base/item"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { computed, defineComponent, PropType, reactive, renderList, renderSlot, watch } from "vue"

  export default defineComponent({
    props: {
      // 展示列表
      list: {
        type: Array as PropType<IEquipmentInfo[]>,
        default: () => []
      },
      // 按钮名称
      title: {
        type: String,
        default: ""
      },
      // 选中列表
      selected: {
        type: Array as PropType<ID[]>,
        default: () => []
      },
      showTips: {
        type: Boolean,
        default: true
      }
    },
    components: { EquipTips },

    setup(props, { emit, slots }) {
      const selected = reactive<ID[]>(props.selected)

      watch(props.selected, () => {
        selected.splice(0, selected.length, ...props.selected)
      })

      // const isSelectAll = computed(() => {
      //   const len = props.highlight.length || props.list.length
      //   return selected.length === len
      // })

      function changeState(id: ID) {
        return () => {
          // 二次点击
          if (selected.includes(id)) {
            selected.splice(selected.indexOf(id), 1)
          } else {
            // 移除同部位
            let cur_position = props.list.filter(a => a.id == id)?.[0].part
            let to_remove = props.list.filter(item => item.part == cur_position) ?? []
            to_remove.forEach(a => {
              if (selected.includes(a.id)) {
                selected.splice(selected.indexOf(a.id), 1)
              }
            })
            selected.push(id)
          }
          emit("update:selected", selected)
        }
      }

      return () => {
        return (
          <div>
            <div class="flex mb-1 w-full items-center">
              {renderSlot(slots, "header")}
              <calc-button class="flex-1">{props.title}</calc-button>
            </div>
            <div class="flex flex-wrap w-full">
              {renderList(props.list, equ => (
                <EquipTips class="item" eq={equ} canClick={true} showTips={props.showTips} active={selected.includes(equ.id)} onUpdate:active={changeState(equ.id)}></EquipTips>
              ))}
            </div>
          </div>
        )
      }
    }
  })
</script>
