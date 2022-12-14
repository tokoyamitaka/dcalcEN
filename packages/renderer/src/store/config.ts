import api from "@/api"
import { IResultInfo, ISkillInfo } from "@/api/character/type"
import { ICharacterSet } from "@/api/info/type"
import { toMap, toObj } from "@/utils"
import { defineStore } from "pinia"
import { useBasicInfoStore } from "."

interface ConfigState extends ICharacterSet {
  name: string
  alter: string
  token: string
  _configlist: string[] | undefined
}

export const useConfigStore = defineStore("config", {
  state: (): ConfigState => {
    return {
      name: "set",
      alter: "",
      carry_type: "",
      attack_attribute: 0,
      skill_set: [],
      forge_set: {},
      dress_set: {},
      single_set: [],
      equip_list: [],
      fusion_list: [],
      wisdom_list: [],
      myths_list: [],
      lv110_list: [],
      consumable_list: [],
      weapons_list: [],
      trigger_set: {},
      skill_que: [],
      title_list: [],
      pet_list: [],
      token: "",
      _configlist: undefined,
      customize: {},
      rune_set: [],
      talisman_set: [],
      buff_ratio: 0,
      hotkey_set: [],
      monster: 0,
      individuation: []
    }
  },
  getters: {
    config_list(state) {
      if (!state._configlist) {
        api.getConfigList().then(res => (state._configlist = res))
      }
      state._configlist?.push("新建存档")
      return state._configlist
    },
    equ_sort(state) {
      let temp: number[][] = []
      const equs = useBasicInfoStore().equipment_list
      const parts = ["称号", "宠物", "武器", "上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
      const lists = [...state.wisdom_list, ...state.myths_list, ...state.lv110_list, ...this.weapons_list, ...this.pet_list, ...this.title_list]
      parts.forEach(part => {
        temp.push(equs.filter(a => a.part == part && lists.includes(a.id as number)).map(a => a.id as number) ?? [])
      })
      return temp
    },
    data(state) {
      return {
        single_set: state.single_set,
        equip_list: this.equ_sort,
        fusion_list: state.fusion_list,
        carry_type: state.carry_type,
        attack_attribute: state.attack_attribute,
        skill_set: state.skill_set,
        forge_set: state.forge_set,
        dress_set: state.dress_set,
        trigger_set: state.trigger_set,
        skill_que: state.skill_que.map((r, id) => {
          return {
            ...r,
            id: id
          }
        }),
        wisdom_list: state.wisdom_list,
        myths_list: state.myths_list,
        title_list: state.title_list,
        pet_list: state.pet_list,
        weapons_list: state.weapons_list,
        lv110_list: state.lv110_list,
        consumable_list: state.consumable_list,
        customize: state.customize,
        rune_set: state.rune_set,
        talisman_set: state.talisman_set,
        buff_ratio: Number(state.buff_ratio),
        hotkey_set: state.hotkey_set,
        monster: state.monster,
        individuation: state.individuation
      }
    }
  },
  actions: {
    async load() {
      // console.log(this.name)
      await api.getConfig(this.name).then(res => {
        const data = toMap(res, ["trigger_set", "customize", "buff_ratio", "dress_set"]) as ICharacterSet
        // data.dress_set = Object.entries(data.dress_set)
        this.$patch(data)
      })
    },
    async switch(name: string) {
      await this.save()
      this.name = name
      await api.switchConfig(this.name)
    },
    async save() {
      toObj(this.data)
      // for (let key in this.data) {
      //   console.log(typeof this.data[key])
      //   // Object.defineProperty(temp, key, {
      //   //   writable: true,
      //   //   enumerable: true,
      //   //   configurable: true
      //   // })
      // }
      // let temp = {}

      // for (let key in this.data) {
      //   Object.defineProperty(temp, key, {
      //     writable: true,
      //     enumerable: true,
      //     configurable: true
      //   })
      // }
      // await api.saveConfig(this.name, this.data)
    },
    async set(name: string, item: Record<string, any>) {
      this[name] = item
    },
    async calc(single: boolean = false): Promise<IResultInfo> {
      if (single && this.data.single_set.length < 1) {
        return { id: undefined, role: "delear", equips: [], name: "", alter: "", skills: {}, total_data: [], info: undefined, skills_passive: undefined, jade: undefined, equips_forget: {} }
      }
      return await api.calc(
        {
          setInfo: toObj(this.data),
          setName: this.name
        },
        single
      )
    },
    getSkill(skill: string) {
      return this.skill_set.find(item => item.name == skill)
    },
    setForge(part: string, key: string, value: any) {
      if (!this.forge_set[part]) {
        this.forge_set[part] = new Map<string, any>()
      }
      let map = this.forge_set[part]
      map.set(key, value)
    },
    getForge(part: string, key: string) {
      if (this.forge_set[part]) {
        let map = this.forge_set[part]
        return map.get(key)
      }
    },
    setDress(part: string, id: number, option: string) {
      this.dress_set[part] = { id, option }
    },
    getDress(part: string) {
      return this.dress_set[part]
    },

    addSingle(id: ID, toggle = false) {
      const basicStore = useBasicInfoStore()
      const newEquip = basicStore.getEquip(id)
      if (!newEquip) {
        return
      }
      if (toggle) {
        const index = this.single_set.indexOf(id)
        if (index > -1) {
          this.single_set.splice(index, 1)
          return
        }
      }
      this.single_set.push(id)
      this.trimSingle()
    },

    importSingle(ids: ID[]) {
      const basicStore = useBasicInfoStore()
      ids = ids.filter(id => basicStore.equiment_ids.includes(id))
      if (ids.length == 0) {
        return
      }
      this.single_set.push(...ids)
      this.trimSingle()
    },

    trimSingle() {
      const basicStore = useBasicInfoStore()
      const map = new Map<string, ID>()
      for (let id of this.single_set) {
        const equip = basicStore.getEquip(id)
        if (equip) {
          map.set(equip.part, id)
        }
      }
      this.single_set = [...map.values()].sort((a, b) => Number(a) - Number(b))
    },
    addSkillQueue(skill: ISkillInfo) {
      this.skill_que.push({ name: skill.name, mode: skill.mode?.[0] ?? "", modes: skill.mode })
    }
  }
})
