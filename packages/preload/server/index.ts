const port: number = 17173

import child_process from "child_process"

let instance: child_process.ChildProcess

/**
 * 开启python的api服务
 * @returns
 */
export function startServer() {
  // TODO 启动python api 待改进 后续添加端口占用判断等
  if (process.platform == "win32") {
    instance = child_process.spawn(`python`, [`api/main.py`, `${port}`])
  } else {
    instance = child_process.spawn("python3", [`${__dirname}/../../api/main.py`, `${port}`])
  }
  if (instance) {
    console.log("server started.")
  }
}

/**
 * 关闭python的api服务
 * @returns
 */
export function stopServer() {
  // TODO 关闭python api
  if (instance) {
    instance.kill(0) && console.log("server stoped.")
    if (process.platform == "win32") {
      child_process.exec("taskkill /f /im python.exe")
    } else {
      child_process.exec("killall Python")
    }
  }
}
