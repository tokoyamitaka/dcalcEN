import { IDetailsInfo, IEquipmentInfo } from "../info/type"

export interface ICharacterInfo extends IDetailsInfo {
  name: string
  alter: string
  character: string
  role: "delear" | "buffer"
  weapon_types: string[]
  carry_type_list: string[]
  armor?: string
  armor_mastery: string[]
  buff_ratio: number
  skills: ISkillInfo[]
  rune: string[]
  talisman?: string[]
  individuation: IIndividuation[]
  config: string
  clothes_coat: string[]
  clothes_pants: string[]
  platinum: string[]
  version: string
  char_optiopns: {
    name: string
    option: string[]
  }[]
}

export interface ISkillInfo {
  name: string
  type: number
  need_level: number
  level_master: number
  level_max: number
  cooldown: number
  current_level: number
  data: number
  tp_max?: number
  tp_level?: number
  mode?: string[]
}

export interface IIndividuation {
  type: string
  value: string
  items: string[]
  row?: number
  column?: number
  key?: number
}

export interface IBufferSkillInfo {
  name: string
  level: number
  data: number[]
}

export interface IDelearSkillInfo {
  name: string
  level: number
  cd: number
  cd_o: number
  rate: number
  mp: number
  cosume_cube_frag: number
  damage: number
  count: number
  atk_rate: number
}

export interface IRankList {
  id: string
  rank: number[][][]
  setInfo: any
  token: string
}

export type IAnyResultInfo = IResultInfo<"buffer"> | IResultInfo<"delear">

export interface IResultInfo<R = "delear" | "buffer"> {
  id: ID
  name: string
  alter: string
  role: R

  token?: string
  forget_set?: Record<string, Map<string, any>>
  equips_forget: any
  skills: Record<string, R extends "buffer" ? IBufferSkillInfo : IDelearSkillInfo>
  skills_passive: any
  equips: IEquipmentInfo[]

  info: any
  total_data: number[]
  jade?: {
    id: number
    name: string
    damage: number
  }[]
}
