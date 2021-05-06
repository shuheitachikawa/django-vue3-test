<template>
  <div>
    <div class="mx-auto pt-10 max-w-xl">
      <div class="mb-5">
        <form @submit.prevent="send">
          <div class="flex">
            <input v-model="tweet" type="text" class="border mr-4" />
            <button type="submit">投稿</button>
          </div>
        </form>
      </div>
      <ul>
        <li v-for="tweet in tweets" :key="tweet.id" class="mb-4">
          <div class="">
            <p>日時：{{ timestamp(tweet.created_at) }}</p>
            <div class="">
              <span>内容：</span><input v-model="tweet.content" type="text" />
            </div>
            <button
              type="button"
              class="border mr-2"
              @click="updateTweet(tweet)"
            >
              上書き
            </button>
            <button type="button" class="border" @click="deleteTweet(tweet.id)">
              削除
            </button>
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
import { inject } from "vue";

export default {
  setup() {
    const tweet = ref("");
    const store = useStore();

    // 一覧取得
    store.dispatch("listTweet");

    // 投稿
    const send = async (): Promise<void> => {
      try {
        const payload = {
          content: tweet.value,
        };
        store.dispatch("postTweet", payload);
        tweet.value = "";
      } catch (e) {
        console.log(e);
      }
    };

    // タイムスタンプ(pluginsからinject)
    const timestamp = inject("timestamp");

    return {
      tweet,
      send,
      tweets: computed(() => store.getters.tweets),
      updateTweet: (payload: Tweet): Promise<void> =>
        store.dispatch("updateTweet", payload),
      deleteTweet: (id: string): Promise<void> =>
        store.dispatch("deleteTweet", id),
      timestamp,
    };
  },
};
</script>

<style lang="scss" scoped></style>
