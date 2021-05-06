import dayjs from "dayjs";
export default {
  install (app, dateTime) {
    const timestamp = () => dayjs(dateTime).format("YYYY年MM月DD日-HH時mm分");
    // app.config.globalProperties.$timestamp = timestamp
    app.provide('timestamp', timestamp)
  }
}