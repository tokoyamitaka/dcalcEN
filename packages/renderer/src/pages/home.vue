<script lang="tsx">
  import api from "@/api"
  import { IAlterInfo } from "@/api/info/type"
  import { useDialog } from "@/components/hooks/dialog"
  import { useOpenWindow } from "@/hooks/open"
  import { useAppStore } from "@/store"
  import { defineComponent, onMounted, renderList } from "vue"
  import Update from "./update.vue"

  function sub_icon(sub: number) {
    return {
      backgroundImage: `url(/images/adventure/sub/${sub}.png)`
    }
  }

  function job_icon(child: IAlterInfo) {
    return {
      filter: !(child.open || import.meta.env.DEV) ? `grayscale(100%)` : ``,
      backgroundImage: `url(/images/adventure/jobs/${child.name}.png)`
    }
  }

  export default defineComponent(async () => {
    const appStore = useAppStore()

    const { alert, show } = useDialog()
    const openUrl = useOpenWindow()

    // 获取角色相关信息，判定是否开放
    function choose_job(child: IAlterInfo) {
      return async () => {
        if (child.comment == "首页") {
          openUrl("https://dcalc.gitee.io/dnfcalculating_110/#/")
          return
        }
        if (child.comment == "设置") {
          openUrl("/set", { width: 600, height: 500 })
          return
        }
        if (ignores.includes(child.name)) {
          return
        }
        // if (child.open || child.url) {
        //   await openUrl()
        // } else {
        //   await alert({
        //     content: "未开放的角色!"
        //   })
        // }
        if (ignores.includes(child.name)) {
          return
        }
        if (child.name == "sponsor") {
          openUrl(child.url ?? "")
          return
        }
        if (child.open || import.meta.env.DEV) {
          const options = child.options ?? []
          if (options.length > 0) {
            await show({
              content: "请选择打开版本",
              action: () => {
                return (
                  <div class="flex pb-2 items-center justify-around">
                    {renderList(options, option =>
                      !option.class ? (
                        <calc-button onClick={() => openUrl("/character", { query: { alter: child.name, version: option.name }, width: 1100, height: 750 })}>{option.title}</calc-button>
                      ) : (
                        <calc-button onClick={() => openUrl("/character", { query: { alter: option.class ?? "", version: option.name }, width: 1100, height: 750 })}>{option.title}</calc-button>
                      )
                    )}
                  </div>
                )
              }
            })
            return
          }
          openUrl("/character", { query: { alter: child.name }, width: 1100, height: 750 })
        } else {
          await alert({
            content: "未开放的角色!"
          })
        }
      }
      // router.push("/character/" + alter)
    }

    onMounted(window.removeLoading)

    const adventure = await api.adventures().then(r => r.data)

    const ignores = ["empty"]

    // function getName(name: string) {
    //   return ignores.includes(name) ? "" : name
    // }

    return () => (
      <div class="bg-cover bg-no-repeat h-auto min-h-full pt-8 pb-12 pl-4 home" style="background-image: url('/images/adventure/bg.jpg')">
        <Update />
        {renderList(adventure, (job, index) => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative" style="background-image: url('/images/adventure/flash.png')">
              <div class="bg-center bg-no-repeat h-22.5 w-30" style={sub_icon(index)}></div>
            </div>
            {renderList(job.children, (child, j) => (
              <div onClick={choose_job(child)} class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
                {child.open && child.name != "sponsor" && (
                  <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute hover:bg-hex-ffd7002e" style="background-image: url('/images/adventure/border.png')"></div>
                )}
                <div class="text-xs text-center text-white w-full bottom-9.6 justify-center absolute" style="letter-spacing:10px;text-indent:10px;z-index:999">
                  {child.comment}
                </div>
                <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">{child.title}</div>
                <div class="bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden " style={job_icon(child)}></div>
              </div>
            ))}
          </div>
        ))}
      </div>
    )
  })
</script>

<style lang="scss">
  .home {
    // background-image: url($path + "bg.jpg");
    background-size: 100% 100%;

    // .job-icon-box {
    //   // background-image: url($path + "flash.png");
    // }

    // .job-box {
    //   .job-border {
    //     // background-image: url($path + "border.png");
    //   }
    // }
  }
</style>
