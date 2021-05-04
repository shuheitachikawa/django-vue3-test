<template>
  <div>
    <div class="mx-auto pt-10 max-w-xl">
      <h1>{{ count }}</h1>
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
            <p>名前：{{ tweet.user.name }}</p>
            <p>日時：{{ tweet.created_at }}</p>
            <p>内容：{{ tweet.content }}</p>
            <button class="mr-2">いいね</button
            ><span>({{ tweet.good.length }})</span>
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
    const send = async (): Promise<void> => {
      const tweet: Tweet = {
        id: "1",
        content: "テスト投稿",
        created_at: "3232323",
        user: {
          name: "石田",
        },
        good: [],
      };
      store.commit("addTweet", tweet);
      await console.log("送信！！！！！");
      store.commit("increment");
    };
    return {
      send,
      tweets: computed(() => store.getters.tweets),
      count: computed(() => store.getters.count),
    };
  },
};
</script>

<style lang="scss" scoped></style>
