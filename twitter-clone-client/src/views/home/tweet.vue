<template>
  <div>
    <div class="mx-auto pt-10 max-w-xl">
      <div class="mb-5">
        <form @submit.prevent="send">
          <div class="flex">
            <input type="text" class="border mr-4" />
            <button type="submit">投稿</button>
          </div>
        </form>
      </div>
      <ul>
        <li v-for="tweet in tweets" :key="tweet.id" class="mb-4">
          <div class="">
            <p>日時：{{ tweet.created_at }}</p>
            <p>内容：{{ tweet.content }}</p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, reactive } from "vue";
import { computed } from "vue";
import { useStore } from "vuex";
import { Tweet } from "../../types/task";

export default {
  setup() {
    const store = useStore();
    store.dispatch("listTweet");
    const send = async (): Promise<void> => {
      const tweet: Tweet = {
        id: "1",
        content: "テスト投稿",
        created_at: "3232323",
        updated_at: "aaaaaaa",
      };
      store.commit("addTweet", tweet);
      await console.log("送信！！！！！");
      store.commit("increment");
    };
    return {
      send,
      tweets: computed(() => store.getters.tweets),
    };
  },
};
</script>

<style lang="scss" scoped></style>
