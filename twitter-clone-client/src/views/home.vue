<template>
  <Header />
  <div class="">
    <router-view />
  </div>
</template>

<script lang="ts">
import Header from "../components/Header.vue";
export default {
  components: {
    Header,
  },
  setup() {
    return {};
  },
};
</script>

<style lang="scss" scoped></style>
