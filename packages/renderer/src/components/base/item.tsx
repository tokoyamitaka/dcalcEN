import { defineComponent, h, renderSlot } from "vue"
import { itemProps, useSelectionItem } from "@/components/hooks/selection/item"

export default defineComponent({
    name: "i-item",
    props: itemProps,
    setup(props, context) {
        const { itemClass, active, current, render } = useSelectionItem(props, context)

        function handleClick() {
            if (!!active) {
                active.value = current.value
            }
        }
        return () => (
            <div onClick={handleClick} class={itemClass.value}>
                {render()}
            </div>
        )
    }
})
