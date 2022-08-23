<script lang="tsx">
  import { defineComponent, renderSlot } from "vue"
  import { switchProps, useSwitch } from "@/components/hooks/swtich/swtich"

  export default defineComponent({
    name: "i-checkbox",
    components: {},
    props: {
      ...switchProps,
      label: {
        type: String
      },
      disabled: {
        type: Boolean,
        default: false
      }
    },

    setup(props, context) {
      const { toggle, switchClass } = useSwitch(
        () => ({
          ...props,
          class: "i-checkbox text-xs h-auto cursor-pointer",
          checkedClass: "checked"
        }),
        context
      )

      const { slots } = context

      return () => (
        <div
          onClick={() => {
            if (!props.disabled) return toggle()
          }}
          class={["flex", switchClass.value]}
        >
          <span class={!props.disabled ? "i-checkbox-icon" : "i-checkbox-icon-disable"}></span>
          <div class={["i-checkbox-label h-auto"]}>{props.label ?? renderSlot(slots, "default")}</div>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .i-checkbox {
    display: flex;
    align-items: center;
    &.checked {
      .i-checkbox-icon {
        background-image: url("./img/checkbox_checked.png");
      }
    }

    .i-checkbox-icon {
      width: 12px;
      min-width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("./img/checkbox_uncheck.png");
    }

    .i-checkbox-icon-disable {
      width: 12px;
      min-width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("./img/checkbox_disable.png");
    }

    &:hover:not(.checked) {
      .i-checkbox-icon {
        background-image: url("./img/checkbox_hover.png");
      }
    }

    .i-checkbox-label {
      line-height: 24px;
      color: #937639;
    }
  }
</style>
