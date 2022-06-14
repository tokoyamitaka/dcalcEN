<script lang="tsx">
  import { syncRef, useVModel } from "@vueuse/core"
  import { computed, PropType, ref } from "vue"
  import { defineComponent } from "vue"
  export default defineComponent({
    props: {
      modelValue: {
        type: [Number, String],
        default: () => 0
      },
      defaultValue: {
        type: Number,
        default: 0
      },
      min: {
        type: Number,
        default: 0
      },
      max: {
        type: Number,
        default: 100
      },

      incrText: {
        type: String,
        default: () => "+"
      },
      decrText: {
        type: String,
        default: () => "-"
      },
      disabled: {
        type: Boolean,
        default: false
      },
      actionClass: {
        type: [String, Array] as PropType<string | string[]>,
        default: () => "m-input-number__action"
      },
      textClass: {
        type: [String, Array] as PropType<string | string[]>,
        default: () => "m-input-number__text"
      },
      disableClass: {
        type: [String, Array] as PropType<string | string[]>,
        default: () => "m-input-number__disable"
      },
      enableClass: {
        type: [String, Array] as PropType<string | string[]>,
        default: () => "m-input-number__enable"
      }
    },
    setup(props, { slots, emit }) {
      const modelValue = useVModel(props, "modelValue")

      const count = ref(Number(props.modelValue ?? 0))
      format()

      syncRef(count, modelValue, { direction: "both" })

      const canIncr = computed(() => count.value < props.max)

      const canDecr = computed(() => count.value > props.min)

      function incr() {
        console.log("incr", canIncr.value, modelValue.value, count.value)
        if (canIncr.value) {
          count.value++
        }
      }

      function decr() {
        console.log("incr", canIncr.value, modelValue.value, count.value)
        if (canDecr.value) {
          count.value--
        }
      }

      function toMax() {
        count.value = props.max
      }

      function toMin() {
        count.value = props.min
      }

      function format() {
        let value = count.value
        value = Number(value.toString().replace(/^\d]g/, "")) ?? 0
        value = Math.min(props.max, value)
        value = Math.max(props.min, value)
        count.value = value || 0
      }

      return () => (
        <div class="flex items-center">
          <input
            disabled={props.disabled}
            onInput={format}
            onPaste={format}
            class={["text-center w-8 p-0 m-0 h-6 leading-6 text-hex-e9c556 bg-black bg-opacity-90"].concat(props.textClass)}
            v-model={count.value}
          ></input>
          <calc-button disabled={props.disabled} class={["h-6 leading-6 "].concat(props.actionClass).concat(canDecr.value ? props.enableClass : props.disableClass)} onClick={decr}>
            {slots.decr?.() ?? props.decrText}
          </calc-button>
          <calc-button disabled={props.disabled} class={["h-6 leading-6 incr-button"].concat(props.actionClass).concat(canIncr.value ? props.enableClass : props.disableClass)} onClick={incr}>
            {slots.incr?.() ?? props.incrText}
          </calc-button>
          <calc-button disabled={props.disabled} class={["h-6 leading-6 incr-button"].concat(props.actionClass).concat(canIncr.value ? props.enableClass : props.disableClass)} onClick={toMax}>
            &gt;&gt;
          </calc-button>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  input {
    outline: none;
    border: none;
  }

  .incr-button {
    background: linear-gradient(#a16228, #7c411a);

    &:hover {
      background: rgba(170, 51, 51, 0.5);
    }
    color: #b69260;
  }
</style>
